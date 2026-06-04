#pragma once
#include <vector>
#include "log.h"

// Runs insert/search/delete on all three structures with the given dataset
// and prints a time comparison table
void runBenchmark(const std::vector<Log>& logs);
