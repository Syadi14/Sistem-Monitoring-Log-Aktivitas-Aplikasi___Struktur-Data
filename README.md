<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/2880a4be-be8f-45a7-91ef-72aa992638cb" />Cara Menjalankan

# 1. Terminal Lokal (Windows — WSL / Linux / macOS)

### Pastikan g++ dan make sudah terinstal.

## Windows (via WSL):
Buka WSL, lalu masuk ke direktori project
cd /mnt/c/path/to/log-monitoring-system

## Build & jalankan
make && ./bin/logmon

## Linux / macOS:
Ubuntu/Debian: sudo apt install g++ make
macOS:         brew install gcc make

cd path/to/log-monitoring-system
make && ./bin/logmon

---
# 2. Terminal VS Code

1. Buka folder project: File → Open Folder → pilih log-monitoring-system
2. Buka terminal: Terminal → New Terminal (atau Ctrl + `)
3. Jalankan:

mingw32-make
./bin/logmon


▎ Catatan Windows: Perintah di atas menggunakan PowerShell (mingw32-make via MSYS2). Jika menggunakan Git Bash atau WSL, gunakan: make && ./bin/logmon

---
# 3. Terminal GitHub Codespace

1. Di GitHub → klik Code → Codespaces → Create codespace on main
2. Tunggu environment selesai di-build
3. Di terminal yang terbuka otomatis, jalankan:

make && ./bin/logmon
