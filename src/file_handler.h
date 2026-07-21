#pragma once
#include <vector>
#include <string>
#include "log.h"

// Handles all CSV read/write for log persistence
class FileHandler {
public:
    static std::vector<Log> loadFromCSV(const std::string& filepath);
    static void             saveToCSV(const std::string& filepath, const std::vector<Log>& logs);
};
