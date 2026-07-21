#include "hashmap_store.h"

// O(1) amortized — just appends to two buckets
void HashMapStore::insert(const Log& log) {
    byLevel[log.level].push_back(log);
    byModule[log.module].push_back(log);
    count++;
}

// O(1) lookup — returns the entire bucket for that level
std::vector<Log> HashMapStore::searchByLevel(const std::string& level) const {
    auto it = byLevel.find(level);
    if (it == byLevel.end()) return {};
    return it->second;
}

// O(1) lookup — returns the entire bucket for that module
std::vector<Log> HashMapStore::searchByModule(const std::string& module) const {
    auto it = byModule.find(module);
    if (it == byModule.end()) return {};
    return it->second;
}

// Rebuilds both maps keeping only logs with timestamp >= cutoff
int HashMapStore::deleteOlderThan(const std::string& cutoff) {
    size_t before = count;
    std::unordered_map<std::string, std::vector<Log>> newByLevel;
    std::unordered_map<std::string, std::vector<Log>> newByModule;
    size_t newCount = 0;
    for (const auto& [lvl, logs] : byLevel) {
        for (const auto& log : logs) {
            if (log.timestamp >= cutoff) {
                newByLevel[log.level].push_back(log);
                newByModule[log.module].push_back(log);
                newCount++;
            }
        }
    }
    byLevel  = std::move(newByLevel);
    byModule = std::move(newByModule);
    count    = newCount;
    return static_cast<int>(before - count);
}

// Returns count per level (INFO, WARNING, ERROR)
std::map<std::string, int> HashMapStore::statsPerLevel() const {
    std::map<std::string, int> stats;
    for (const auto& [lvl, logs] : byLevel)
        stats[lvl] = static_cast<int>(logs.size());
    return stats;
}

size_t HashMapStore::size() const { return count; }

// Logs are stored twice (once per index), so memory is ~2x a single copy
size_t HashMapStore::memoryUsage() const {
    size_t total = 0;
    for (const auto& [k, v] : byLevel)  total += v.capacity() * sizeof(Log);
    for (const auto& [k, v] : byModule) total += v.capacity() * sizeof(Log);
    return total;
}
