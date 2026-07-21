#pragma once
#include <vector>
#include "../log.h"

// Baseline: stores logs in insertion order
// All operations are O(n) — used to show why better structures matter
class VectorStore {
public:
    void              insert(const Log& log);
    std::vector<Log>  searchByLevel(const std::string& level) const;
    std::vector<Log>  searchByModule(const std::string& module) const;
    std::vector<Log>  searchByTimeRange(const std::string& from, const std::string& to) const;
    int               deleteOlderThan(const std::string& cutoff);
    size_t            size() const;
    size_t            memoryUsage() const;

private:
    std::vector<Log> data;
};
