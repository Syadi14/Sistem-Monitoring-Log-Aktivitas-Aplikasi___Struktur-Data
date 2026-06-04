#include <iostream>
#include <string>
#include <vector>
#include <limits>
#include <algorithm>

#include "log.h"
#include "file_handler.h"
#include "generate_data.h"
#include "benchmark.h"
#include "ds/vector_store.h"
#include "ds/hashmap_store.h"
#include "ds/bst_store.h"

const std::string DATA_FILE = "data/logs.csv";

// ─── Helpers ────────────────────────────────────────────────────────────────

static void printLog(const Log& l) {
    std::cout << "[" << l.id << "] "
              << l.timestamp << " | "
              << l.level     << " | "
              << l.module    << " | "
              << l.message   << "\n";
}

static void printLogs(const std::vector<Log>& logs) {
    if (logs.empty()) { std::cout << "  (no results)\n"; return; }
    for (const auto& l : logs) printLog(l);
    std::cout << "  Total: " << logs.size() << " log(s)\n";
}

static void clearInput() {
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

static int levelPriority(const std::string& level) {
    if (level == "INFO")    return 0;
    if (level == "WARNING") return 1;
    return 2; // ERROR
}

// ─── Main ───────────────────────────────────────────────────────────────────

int main() {
    std::cout << "=== Log Monitoring System ===\n";

    // Load all logs from CSV into memory
    std::vector<Log> allLogs = FileHandler::loadFromCSV(DATA_FILE);

    // Load all three data structures
    VectorStore  vs;
    HashMapStore hm;
    BSTStore     bst;

    for (const auto& log : allLogs) {
        vs.insert(log);
        hm.insert(log);
        bst.insert(log);
    }

    int choice = 0;
    while (true) {
        std::cout << "\n--- MENU ---\n"
                  << "1.  Insert new log\n"
                  << "2.  Search by time range\n"
                  << "3.  Search by level (INFO/WARNING/ERROR)\n"
                  << "4.  Search by module\n"
                  << "5.  Show all ERROR logs\n"
                  << "6.  Delete logs before timestamp\n"
                  << "7.  Statistics (count per level)\n"
                  << "8.  Run benchmark (compare all structures)\n"
                  << "9.  Generate new dummy dataset\n"
                  << "10. Show all data\n"
                  << "0.  Save & exit\n"
                  << "Choice: ";
        std::cin >> choice;
        clearInput();

        if (choice == 0) break;

        switch (choice) {

        case 1: {
            Log l;
            std::cout << "Timestamp (YYYY-MM-DD HH:MM:SS): "; std::getline(std::cin, l.timestamp);
            std::cout << "Level (INFO/WARNING/ERROR): ";       std::getline(std::cin, l.level);
            std::cout << "Module: ";                           std::getline(std::cin, l.module);
            std::cout << "Message: ";                          std::getline(std::cin, l.message);
            l.id = static_cast<int>(allLogs.size()) + 1;

            allLogs.push_back(l);
            vs.insert(l);
            hm.insert(l);
            bst.insert(l);
            std::cout << "Inserted log #" << l.id << "\n";
            break;
        }

        case 2: {
            // Collect unique dates from loaded logs
            std::vector<std::string> dates;
            for (const auto& log : allLogs) {
                std::string date = log.timestamp.substr(0, 10);
                if (std::find(dates.begin(), dates.end(), date) == dates.end())
                    dates.push_back(date);
            }
            std::sort(dates.begin(), dates.end());

            std::cout << "\nAvailable dates:\n";
            for (int i = 0; i < (int)dates.size(); i++)
                std::cout << "  " << i + 1 << ". " << dates[i] << "\n";

            int fromIdx, toIdx;
            std::cout << "From (select number): "; std::cin >> fromIdx; clearInput();
            std::cout << "To   (select number): "; std::cin >> toIdx;   clearInput();

            if (fromIdx < 1 || fromIdx > (int)dates.size() ||
                toIdx   < 1 || toIdx   > (int)dates.size()) {
                std::cout << "Invalid choice.\n"; break;
            }

            std::string from = dates[fromIdx - 1] + " 00:00:00";
            std::string to   = dates[toIdx   - 1] + " 23:59:59";
            std::cout << "\n[BST result]\n";
            printLogs(bst.searchByTimeRange(from, to));
            break;
        }

        case 3: {
            std::cout << "\nSelect log level:\n"
                      << "  1. INFO\n"
                      << "  2. WARNING\n"
                      << "  3. ERROR\n"
                      << "Choice: ";
            int lvlChoice; std::cin >> lvlChoice; clearInput();

            std::string level;
            if      (lvlChoice == 1) level = "INFO";
            else if (lvlChoice == 2) level = "WARNING";
            else if (lvlChoice == 3) level = "ERROR";
            else { std::cout << "Invalid choice.\n"; break; }

            std::cout << "\n[HashMap result]\n";
            printLogs(hm.searchByLevel(level));
            break;
        }

        case 4: {
            // Collect unique modules from loaded logs
            std::vector<std::string> modules;
            for (const auto& log : allLogs) {
                if (std::find(modules.begin(), modules.end(), log.module) == modules.end())
                    modules.push_back(log.module);
            }
            std::sort(modules.begin(), modules.end());

            std::cout << "\nAvailable modules:\n";
            for (int i = 0; i < (int)modules.size(); i++)
                std::cout << "  " << i + 1 << ". " << modules[i] << "\n";

            int modIdx;
            std::cout << "Choice: "; std::cin >> modIdx; clearInput();

            if (modIdx < 1 || modIdx > (int)modules.size()) {
                std::cout << "Invalid choice.\n"; break;
            }

            std::cout << "\n[HashMap result]\n";
            printLogs(hm.searchByModule(modules[modIdx - 1]));
            break;
        }

        case 5: {
            std::cout << "\n[HashMap — ERROR logs]\n";
            printLogs(hm.searchByLevel("ERROR"));
            break;
        }

        case 6: {
            std::string cutoff;
            std::cout << "Delete all logs before (YYYY-MM-DD HH:MM:SS): ";
            std::getline(std::cin, cutoff);

            vs.deleteOlderThan(cutoff);
            hm.deleteOlderThan(cutoff);
            int removed = bst.deleteOlderThan(cutoff);

            allLogs.erase(
                std::remove_if(allLogs.begin(), allLogs.end(),
                    [&cutoff](const Log& l) { return l.timestamp < cutoff; }),
                allLogs.end());

            std::cout << "Deleted " << removed << " log(s) from all stores.\n";
            break;
        }

        case 7: {
            std::cout << "\n--- Statistics ---\n";
            auto stats = hm.statsPerLevel();
            for (const auto& [lvl, cnt] : stats)
                std::cout << "  " << lvl << ": " << cnt << " log(s)\n";
            break;
        }

        case 8: {
            runBenchmark(allLogs);
            break;
        }

        case 9: {
            int n;
            std::cout << "How many logs to generate? "; std::cin >> n; clearInput();
            generateDummyLogs(DATA_FILE, n);
            allLogs = FileHandler::loadFromCSV(DATA_FILE);
            vs = VectorStore();  hm = HashMapStore();  bst = BSTStore();
            for (const auto& log : allLogs) { vs.insert(log); hm.insert(log); bst.insert(log); }
            std::cout << "Dataset reloaded.\n";
            break;
        }

        case 10: {
            std::cout << "\nSort by:\n"
                      << "  1. Date & time (chronological)\n"
                      << "  2. Level (INFO -> WARNING -> ERROR)\n"
                      << "  3. Module (A -> Z)\n"
                      << "Choice: ";
            int sortChoice; std::cin >> sortChoice; clearInput();

            std::vector<Log> sorted = allLogs;

            if (sortChoice == 1) {
                std::sort(sorted.begin(), sorted.end(), [](const Log& a, const Log& b) {
                    return a.timestamp < b.timestamp;
                });
                std::cout << "\n[All logs - sorted by date & time]\n";
            } else if (sortChoice == 2) {
                std::sort(sorted.begin(), sorted.end(), [](const Log& a, const Log& b) {
                    int pa = levelPriority(a.level), pb = levelPriority(b.level);
                    return pa != pb ? pa < pb : a.timestamp < b.timestamp;
                });
                std::cout << "\n[All logs - sorted by level: INFO -> WARNING -> ERROR]\n";
            } else if (sortChoice == 3) {
                std::sort(sorted.begin(), sorted.end(), [](const Log& a, const Log& b) {
                    return a.module != b.module ? a.module < b.module : a.timestamp < b.timestamp;
                });
                std::cout << "\n[All logs - sorted by module A -> Z]\n";
            } else {
                std::cout << "Invalid choice.\n"; break;
            }

            printLogs(sorted);
            break;
        }

        default:
            std::cout << "Invalid choice.\n";
        }
    }

    FileHandler::saveToCSV(DATA_FILE, allLogs);
    std::cout << "Goodbye.\n";
    return 0;
}
