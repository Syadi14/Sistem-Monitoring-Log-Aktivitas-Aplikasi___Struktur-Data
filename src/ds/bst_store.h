#pragma once
#include <vector>
#include <string>
#include "../log.h"

// Hand-written BST sorted by "timestamp_id" key
// Average O(log n) insert/search/delete; O(n) worst-case on fully sorted input
class BSTStore {
public:
    BSTStore() : root(nullptr), count_(0) {}
    ~BSTStore() { clear(root); }

    BSTStore(const BSTStore&)            = delete;
    BSTStore& operator=(const BSTStore&) = delete;

    BSTStore(BSTStore&& o) noexcept : root(o.root), count_(o.count_) {
        o.root = nullptr; o.count_ = 0;
    }
    BSTStore& operator=(BSTStore&& o) noexcept {
        if (this != &o) {
            clear(root);
            root = o.root; count_ = o.count_;
            o.root = nullptr; o.count_ = 0;
        }
        return *this;
    }

    void             insert(const Log& log);
    std::vector<Log> searchByTimeRange(const std::string& from, const std::string& to) const;
    int              deleteOlderThan(const std::string& cutoff);
    size_t           size() const { return count_; }
    size_t           memoryUsage() const;

private:
    struct Node {
        std::string key;   // "timestamp_id"
        Log         log;
        Node*       left  = nullptr;
        Node*       right = nullptr;
    };

    Node*  root;
    size_t count_;

    void   insertNode(Node*& node, const std::string& key, const Log& log);
    void   rangeSearch(Node* node, const std::string& from, const std::string& toEnd,
                       std::vector<Log>& result) const;
    void   collectAll(Node* node, std::vector<Log>& out) const;
    void   clear(Node* node);
    size_t nodeBytes(Node* node) const;
};
