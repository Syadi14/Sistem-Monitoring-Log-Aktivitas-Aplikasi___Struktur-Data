#include "benchmark.h"
#include "ds/vector_store.h"
#include "ds/hashmap_store.h"
#include "ds/bst_store.h"
#include <chrono>
#include <iostream>
#include <iomanip>
#include <sstream>

using Clock = std::chrono::high_resolution_clock;
using Ms    = std::chrono::duration<double, std::milli>;

static double elapsed(Clock::time_point start) {
    return Ms(Clock::now() - start).count();
}

static std::string toKB(size_t bytes) {
    std::ostringstream ss;
    ss << std::fixed << std::setprecision(2) << (bytes / 1024.0) << " KB";
    return ss.str();
}

void runBenchmark(const std::vector<Log>& logs) {
    std::cout << "\n========== BENCHMARK (" << logs.size() << " logs) ==========\n";

    const int W0 = 22, W = 16;
    auto header = [&](const std::string& label) {
        std::cout << std::left
                  << std::setw(W0) << label
                  << std::setw(W)  << "Vector"
                  << std::setw(W)  << "HashMap"
                  << std::setw(W)  << "BST"
                  << "\n" << std::string(W0 + W * 3, '-') << "\n";
    };

    // ── INSERT ──────────────────────────────────────────────────
    header("--- Insert all ---");
    VectorStore vs; HashMapStore hm; BSTStore bst;

    auto t = Clock::now();
    for (const auto& l : logs) vs.insert(l);
    double vsIns = elapsed(t);

    t = Clock::now();
    for (const auto& l : logs) hm.insert(l);
    double hmIns = elapsed(t);

    t = Clock::now();
    for (const auto& l : logs) bst.insert(l);
    double bstIns = elapsed(t);

    std::cout << std::setw(W0) << "Time (ms)"
              << std::setw(W)  << vsIns
              << std::setw(W)  << hmIns
              << std::setw(W)  << bstIns << "\n";
    std::cout << std::setw(W0) << "Memory (after insert)"
              << std::setw(W)  << toKB(vs.memoryUsage())
              << std::setw(W)  << toKB(hm.memoryUsage())
              << std::setw(W)  << toKB(bst.memoryUsage()) << "\n\n";

    // ── SEARCH by level ─────────────────────────────────────────
    header("--- Search by level ---");
    t = Clock::now(); vs.searchByLevel("ERROR");  double vsLvl = elapsed(t);
    t = Clock::now(); hm.searchByLevel("ERROR");  double hmLvl = elapsed(t);

    std::cout << std::setw(W0) << "Time (ms)"
              << std::setw(W)  << vsLvl
              << std::setw(W)  << hmLvl
              << std::setw(W)  << "N/A" << "\n\n";

    // ── SEARCH by time range ─────────────────────────────────────
    header("--- Search time range ---");
    t = Clock::now(); vs.searchByTimeRange("2024-06-01 00:00:00", "2024-06-30 23:59:59"); double vsT = elapsed(t);
    t = Clock::now(); bst.searchByTimeRange("2024-06-01 00:00:00", "2024-06-30 23:59:59"); double bstT = elapsed(t);

    std::cout << std::setw(W0) << "Time (ms)"
              << std::setw(W)  << vsT
              << std::setw(W)  << "N/A"
              << std::setw(W)  << bstT << "\n\n";

    // ── DELETE old logs ──────────────────────────────────────────
    header("--- Delete old logs ---");
    t = Clock::now(); vs.deleteOlderThan("2024-06-01 00:00:00");  double vsDel = elapsed(t);
    t = Clock::now(); bst.deleteOlderThan("2024-06-01 00:00:00"); double bstDel = elapsed(t);

    std::cout << std::setw(W0) << "Time (ms)"
              << std::setw(W)  << vsDel
              << std::setw(W)  << "N/A"
              << std::setw(W)  << bstDel << "\n";
    std::cout << std::setw(W0) << "Memory (after delete)"
              << std::setw(W)  << toKB(vs.memoryUsage())
              << std::setw(W)  << "N/A"
              << std::setw(W)  << toKB(bst.memoryUsage()) << "\n\n";

    std::cout << "N/A = operation not applicable to that structure\n";
    std::cout << std::string(W0 + W * 3, '=') << "\n";
}
