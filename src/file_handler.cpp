#include "file_handler.h"
#include <fstream>
#include <sstream>
#include <iostream>

// Reads logs.csv → vector<Log>
// CSV format: id,timestamp,level,module,message
std::vector<Log> FileHandler::loadFromCSV(const std::string& filepath) {
    std::vector<Log> logs;
    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "[FileHandler] Could not open: " << filepath << "\n";
        return logs;
    }

    std::string line;
    std::getline(file, line); // skip header row

    while (std::getline(file, line)) {
        if (line.empty()) continue;

        std::stringstream ss(line);
        std::string token;
        Log log;

        try {
            std::getline(ss, token,        ','); log.id = std::stoi(token);
        } catch (...) {
            std::cerr << "[FileHandler] Skipping malformed line: " << line << "\n";
            continue;
        }
        std::getline(ss, log.timestamp, ',');
        std::getline(ss, log.level,     ',');
        std::getline(ss, log.module,    ',');
        std::getline(ss, log.message);  // read remainder — preserves commas in messages

        logs.push_back(log);
    }

    std::cout << "[FileHandler] Loaded " << logs.size() << " logs from " << filepath << "\n";
    return logs;
}

// Writes vector<Log> → logs.csv (overwrites)
void FileHandler::saveToCSV(const std::string& filepath, const std::vector<Log>& logs) {
    std::ofstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "[FileHandler] Could not write to: " << filepath << "\n";
        return;
    }

    file << "id,timestamp,level,module,message\n";
    for (const auto& log : logs) {
        file << log.id        << ","
             << log.timestamp << ","
             << log.level     << ","
             << log.module    << ","
             << log.message   << "\n";
    }

    std::cout << "[FileHandler] Saved " << logs.size() << " logs to " << filepath << "\n";
}
