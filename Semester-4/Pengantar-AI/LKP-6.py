from aima3.logic import *

KB = PropKB()

# Wumpus
KB.tell(expr("W23"))
# Pit
KB.tell(expr("P34"))
KB.tell(expr("P43"))
KB.tell(expr("P32"))
# Totem
KB.tell(expr("T24"))
# Stench
KB.tell(expr("S13"))
KB.tell(expr("S22"))
KB.tell(expr("S33"))
KB.tell(expr("S24"))
# Breeze
KB.tell(expr("B44"))
KB.tell(expr("B42"))
KB.tell(expr("B31"))

KB.tell(expr("Safe11"))
print("Fakta berhasil dimasukkan.\n")

#ask_if_true
print("Apakah posisi (1,1) aman?")
print(KB.ask_if_true(expr("Safe11")))

print("\nApakah ada Wumpus di (2,3)?")
print(KB.ask_if_true(expr("W23")))

print("\nApakah ada Pit di (3,2)?")
print(KB.ask_if_true(expr("P32")))

print("\nApakah ada Totem di (2,4)?")
print(KB.ask_if_true(expr("T24")))

#program utamanya
print("\nAgent Mencari Totem")
path_to_totem = [
(1,1),
(1,2),
(1,3),
(1,4),
(2,4)
]

for step in path_to_totem:
    print("Agent bergerak ke:", step)