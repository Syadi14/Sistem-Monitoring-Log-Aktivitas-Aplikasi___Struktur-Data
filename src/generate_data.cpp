#include "generate_data.h"
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <sstream>

// Returns a random timestamp between 2024-01-01 and 2024-12-31
static std::string randomTimestamp() {
    int month  = (rand() % 12) + 1;
    int day    = (rand() % 28) + 1;
    int hour   = rand() % 24;
    int minute = rand() % 60;
    int second = rand() % 60;

    std::ostringstream oss;
    oss << "2024-"
        << std::setw(2) << std::setfill('0') << month  << "-"
        << std::setw(2) << std::setfill('0') << day    << " "
        << std::setw(2) << std::setfill('0') << hour   << ":"
        << std::setw(2) << std::setfill('0') << minute << ":"
        << std::setw(2) << std::setfill('0') << second;
    return oss.str();
}

void generateDummyLogs(const std::string& filepath, int n) {
    srand(static_cast<unsigned>(time(nullptr)));

    const char* levels[]   = { "INFO", "WARNING", "ERROR" };
    const char* modules[]  = { "AUTH", "API", "DB", "PAYMENT", "CACHE", "SCHEDULER" };
    const char* messages[] = {
        "User login successful",
        "Request timeout after 5000ms",
        "Database connection failed",
        "Payment processed successfully",
        "Cache miss on key user_session",
        "Scheduled job started",
        "Invalid token received",
        "Query executed in 120ms",
        "Retry attempt 3 of 5",
        "Service restarted"
    };

    std::ofstream file(filepath);
    if (!file.is_open()) {
        std::cerr << "[Generator] Cannot write to " << filepath << "\n";
        return;
    }

    file << "id,timestamp,level,module,message\n";
    for (int i = 1; i <= n; i++) {
        file << i                                      << ","
             << randomTimestamp()                      << ","
             << levels[rand() % 3]                     << ","
             << modules[rand() % 6]                    << ","
             << messages[rand() % 10]                  << "\n";
    }

    std::cout << "[Generator] Created " << n << " dummy logs in " << filepath << "\n";
}
