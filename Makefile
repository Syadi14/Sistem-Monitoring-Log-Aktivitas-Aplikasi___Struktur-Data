CXX      = g++
CXXFLAGS = -std=c++17 -O2 -Wall -Iinc
SRCDIR   = src
BINDIR   = bin

SOURCES  = $(SRCDIR)/main.cpp \
           $(SRCDIR)/file_handler.cpp \
           $(SRCDIR)/ds/vector_store.cpp \
           $(SRCDIR)/ds/hashmap_store.cpp \
           $(SRCDIR)/ds/bst_store.cpp \
           $(SRCDIR)/benchmark.cpp \
           $(SRCDIR)/generate_data.cpp

TARGET   = $(BINDIR)/logmon

all: $(BINDIR) $(TARGET)

$(BINDIR):
	mkdir -p $(BINDIR)

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(TARGET)

clean:
	rm -rf $(BINDIR)

.PHONY: all clean
