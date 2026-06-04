#pragma once
#include <string>

struct Log {
    int         id;
    std::string timestamp;  // format: "YYYY-MM-DD HH:MM:SS"
    std::string level;      // "INFO", "WARNING", "ERROR"
    std::string module;     // "AUTH", "API", "DB", "PAYMENT", etc.
    std::string message;
};
