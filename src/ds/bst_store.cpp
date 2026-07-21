#include "bst_store.h"

// key = "timestamp_id" — unique even when two logs share the same timestamp
void BSTStore::insert(const Log& log) {
    std::string key = log.timestamp + "_" + std::to_string(log.id);
    insertNode(root, key, log);
}

void BSTStore::insertNode(Node*& node, const std::string& key, const Log& log) {
    if (!node) {
        node = new Node{key, log};
        count_++;
        return;
    }
    if (key < node->key)
        insertNode(node->left, key, log);
    else if (key > node->key)
        insertNode(node->right, key, log);
    else
        node->log = log;  // duplicate key: update in place, don't increment
}

// Pruned in-order traversal — skips branches that cannot contain range results
void BSTStore::rangeSearch(Node* node, const std::string& from, const std::string& toEnd,
                           std::vector<Log>& result) const {
    if (!node) return;
    if (node->key > from)
        rangeSearch(node->left, from, toEnd, result);
    if (node->key >= from && node->key <= toEnd)
        result.push_back(node->log);
    if (node->key < toEnd)
        rangeSearch(node->right, from, toEnd, result);
}

std::vector<Log> BSTStore::searchByTimeRange(const std::string& from, const std::string& to) const {
    std::vector<Log> result;
    // "~" (ASCII 126) sorts after all digits/letters, capturing every ID at the boundary timestamp
    rangeSearch(root, from, to + "~", result);
    return result;
}

// Collect all logs, then rebuild keeping only those with key >= cutoff
int BSTStore::deleteOlderThan(const std::string& cutoff) {
    std::vector<Log> all;
    collectAll(root, all);

    size_t before = count_;
    clear(root);
    root   = nullptr;
    count_ = 0;

    for (const auto& log : all) {
        std::string key = log.timestamp + "_" + std::to_string(log.id);
        if (key >= cutoff)
            insertNode(root, key, log);
    }

    return static_cast<int>(before - count_);
}

void BSTStore::collectAll(Node* node, std::vector<Log>& out) const {
    if (!node) return;
    collectAll(node->left, out);
    out.push_back(node->log);
    collectAll(node->right, out);
}

void BSTStore::clear(Node* node) {
    if (!node) return;
    clear(node->left);
    clear(node->right);
    delete node;
}

// Each node: the Node struct + heap storage for the key string
size_t BSTStore::nodeBytes(Node* node) const {
    if (!node) return 0;
    return sizeof(Node) + node->key.size()
         + nodeBytes(node->left) + nodeBytes(node->right);
}

size_t BSTStore::memoryUsage() const { return nodeBytes(root); }
