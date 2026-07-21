#pragma once
#include <unordered_map>
#include <map>
#include <vector>
#include <string>
#include "../log.h"

// Two hash maps: one indexed by level, one by module
// Search by level or module → O(1) average
class HashMapStore {
public:
    void              insert(const Log& log);
    std::vector<Log>  searchByLevel(const std::string& level) const;
    std::vector<Log>  searchByModule(const std::string& module) const;
    int               deleteOlderThan(const std::string& cutoff);
    std::map<std::string, int> statsPerLevel() const;
    size_t            size() const;
    size_t            memoryUsage() const;

private:
    std::unordered_map<std::string, std::vector<Log>> byLevel;   // "ERROR" → [Log, ...]
    std::unordered_map<std::string, std::vector<Log>> byModule;  // "AUTH"  → [Log, ...]
    size_t count = 0;
};
