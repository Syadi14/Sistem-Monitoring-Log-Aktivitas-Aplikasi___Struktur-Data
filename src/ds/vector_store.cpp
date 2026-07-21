#include "vector_store.h"
#include <algorithm>

void VectorStore::insert(const Log& log) {
    data.push_back(log);
}

// Scans entire vector — O(n)
std::vector<Log> VectorStore::searchByLevel(const std::string& level) const {
    std::vector<Log> result;
    for (const auto& l : data)
        if (l.level == level) result.push_back(l);
    return result;
}

std::vector<Log> VectorStore::searchByModule(const std::string& module) const {
    std::vector<Log> result;
    for (const auto& l : data)
        if (l.module == module) result.push_back(l);
    return result;
}

std::vector<Log> VectorStore::searchByTimeRange(const std::string& from, const std::string& to) const {
    std::vector<Log> result;
    for (const auto& l : data)
        if (l.timestamp >= from && l.timestamp <= to) result.push_back(l);
    return result;
}

// Removes matching entries and shifts remaining — O(n)
int VectorStore::deleteOlderThan(const std::string& cutoff) {
    int before = static_cast<int>(data.size());
    data.erase(
        std::remove_if(data.begin(), data.end(),
            [&](const Log& l){ return l.timestamp < cutoff; }),
        data.end()
    );
    return before - static_cast<int>(data.size());
}

size_t VectorStore::size() const { return data.size(); }

// capacity() reflects actual allocated memory, not just size()
size_t VectorStore::memoryUsage() const {
    return data.capacity() * sizeof(Log);
}
