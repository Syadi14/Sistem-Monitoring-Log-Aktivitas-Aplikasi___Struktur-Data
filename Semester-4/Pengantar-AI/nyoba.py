import sys
import os
 
# Pastikan path ke aima-python tersedia
# Jika belum install: pip install aima3
# atau clone: https://github.com/aimacode/aima-python
try:
    from logic import PropKB, expr, pl_resolution
except ImportError:
    print("ERROR: Modul 'logic' dari aima-python tidak ditemukan.")
    print("Install dengan: pip install aima3")
    print("Atau clone: git clone https://github.com/aimacode/aima-python")
    sys.exit(1)
 
 
# ============================================================
# HELPER
# ============================================================
 
def get_neighbors(x, y, size=4):
    """Kembalikan tetangga valid (atas, bawah, kiri, kanan) dalam grid size x size."""
    nbrs = []
    if x > 1:    nbrs.append((x-1, y))
    if x < size: nbrs.append((x+1, y))
    if y > 1:    nbrs.append((x, y-1))
    if y < size: nbrs.append((x, y+1))
    return nbrs
 
 
# ============================================================
# 1. BANGUN KNOWLEDGE BASE
# ============================================================
 
def build_wumpus_kb():
    """
    Membangun KB Wumpus World dari fakta gambar.
 
    Notasi propositional:
      P_x_y  = ada PIT di (x,y)
      W_x_y  = ada Wumpus di (x,y)
      B_x_y  = ada Breeze di (x,y)
      S_x_y  = ada Stench di (x,y)
      G_x_y  = ada Gold di (x,y)
      OK_x_y = sel (x,y) aman (tidak PIT dan tidak Wumpus)
    """
    kb   = PropKB()
    all_cells = [(x, y) for x in range(1, 5) for y in range(1, 5)]
 
    print("=" * 60)
    print("  WUMPUS WORLD — Mendefinisikan Fakta KB")
    print("=" * 60)
 
    # ---------- PIT ----------
    pits = [(3, 4), (4, 3), (3, 2)]
    print(f"\n🕳️  PIT berada di: {pits}")
    for (x, y) in pits:
        kb.tell(expr(f'P_{x}_{y}'))
    for (x, y) in all_cells:
        if (x, y) not in pits:
            kb.tell(expr(f'~P_{x}_{y}'))
 
    # ---------- WUMPUS ----------
    wumpus_cells = [(2, 3), (2, 4)]   # dari gambar: dua sel bergambar monster
    # Secara logika standar Wumpus World ada 1 Wumpus; gunakan (2,3) sebagai posisi utama
    wumpus = (2, 3)
    print(f"👹 Wumpus berada di: {wumpus}")
    kb.tell(expr(f'W_{wumpus[0]}_{wumpus[1]}'))
    for (x, y) in all_cells:
        if (x, y) != wumpus:
            kb.tell(expr(f'~W_{x}_{y}'))
 
    # ---------- BREEZE: sel bersebelahan dengan PIT ----------
    print("💨 Breeze = sel yang bersebelahan dengan PIT")
    for (x, y) in all_cells:
        nbrs = get_neighbors(x, y)
        if any(n in pits for n in nbrs):
            kb.tell(expr(f'B_{x}_{y}'))
        else:
            kb.tell(expr(f'~B_{x}_{y}'))
 
    # ---------- STENCH: sel bersebelahan dengan Wumpus ----------
    print("💀 Stench = sel yang bersebelahan dengan Wumpus")
    for (x, y) in all_cells:
        nbrs = get_neighbors(x, y)
        if (wumpus[0], wumpus[1]) in nbrs:
            kb.tell(expr(f'S_{x}_{y}'))
        else:
            kb.tell(expr(f'~S_{x}_{y}'))
 
    # ---------- GOLD ----------
    gold = (1, 4)   # Sel aman di pojok kiri atas
    print(f"🏆 Gold/Totem berada di: {gold}")
    kb.tell(expr(f'G_{gold[0]}_{gold[1]}'))
    for (x, y) in all_cells:
        if (x, y) != gold:
            kb.tell(expr(f'~G_{x}_{y}'))
 
    # ---------- OK: sel aman ----------
    safe_cells = []
    for (x, y) in all_cells:
        if (x, y) not in pits and (x, y) != (wumpus[0], wumpus[1]):
            kb.tell(expr(f'OK_{x}_{y}'))
            safe_cells.append((x, y))
        else:
            kb.tell(expr(f'~OK_{x}_{y}'))
    print(f"✅ Sel aman (OK): {safe_cells}")
    print()
 
    return kb, pits, wumpus, gold
 
 
# ============================================================
# 2. ask_if_true
# ============================================================
 
def ask_if_true(kb, query_str):
    """
    Tanya KB apakah query pasti True menggunakan resolusi propositional.
    Returns: True | False | 'Unknown'
    """
    q = expr(query_str)
    if pl_resolution(kb, q):
        return True
    if pl_resolution(kb, expr(f'~{query_str}')):
        return False
    return 'Unknown'
 
 
def ask_and_print(kb, query_str, description=""):
    """Tanya KB dan cetak hasilnya secara rapi."""
    result = ask_if_true(kb, query_str)
    icon = "✅" if result is True else ("❌" if result is False else "❓")
    desc = f"  ← {description}" if description else ""
    print(f"      {icon} ask_if_true('{query_str}') => {result}{desc}")
    return result
 
 
# ============================================================
# 3. VISUALISASI GRID
# ============================================================
 
def print_grid(pits, wumpus, gold):
    """Cetak peta Wumpus World ke terminal."""
    sym = {}
    for (x, y) in pits:
        sym[(x, y)] = 'PIT '
    sym[(wumpus[0], wumpus[1])] = 'WMP '
    sym[gold] = 'GOLD'
    sym[(1, 1)] = 'AGT '
 
    print("=" * 50)
    print("  PETA WUMPUS WORLD")
    print("=" * 50)
    for row in range(4, 0, -1):
        line = f"  {row} |"
        for col in range(1, 5):
            cell = sym.get((col, row), '    ')
            line += f" {cell} |"
        print(line)
        print("    +" + "------+" * 4)
    print("        1      2      3      4")
    print("  Keterangan: AGT=Agent  WMP=Wumpus  PIT=Lubang  GOLD=Emas")
    print()
 
 
# ============================================================
# 4. AGENT: TEMUKAN GOLD
# ============================================================
 
def agent_find_gold(kb, gold):
    """
    Simulasi agent menemukan gold dengan langkah-langkah
    dan verifikasi tiap sel menggunakan ask_if_true.
 
    Rute aman:
      Pergi  : (1,1) → (1,2) → (1,3) → (1,4)
      Pulang : (1,4) → (1,3) → (1,2) → (1,1)
    """
    print("=" * 60)
    print("  AGENT MENCARI GOLD — Step by Step")
    print("=" * 60)
 
    route_to_gold = [(1, 1), (1, 2), (1, 3), (1, 4)]
    route_home    = [(1, 3), (1, 2), (1, 1)]
 
    print("\n📍 Rute pergi  : (1,1) → (1,2) → (1,3) → (1,4)")
    print("🔄 Rute pulang : (1,4) → (1,3) → (1,2) → (1,1)\n")
 
    gold_grabbed = False
 
    # ----- Perjalanan ke Gold -----
    for step, (x, y) in enumerate(route_to_gold):
        print(f"{'─'*55}")
        print(f"  LANGKAH {step + 1}: Agent tiba di ({x}, {y})")
        print(f"{'─'*55}")
 
        # Verifikasi keamanan sel saat ini
        print("  🔎 Mengecek kondisi sel ini:")
        ask_and_print(kb, f'OK_{x}_{y}', "sel aman?")
        ask_and_print(kb, f'P_{x}_{y}',  "ada PIT?")
        ask_and_print(kb, f'W_{x}_{y}',  "ada Wumpus?")
        ask_and_print(kb, f'B_{x}_{y}',  "ada Breeze (PIT dekat)?")
        ask_and_print(kb, f'S_{x}_{y}',  "ada Stench (Wumpus dekat)?")
 
        # Cek apakah Gold ada di sini
        gold_here = ask_and_print(kb, f'G_{x}_{y}', "ada Gold di sini?")
        if gold_here is True:
            print(f"\n  🎉 GOLD DITEMUKAN di ({x},{y})! Agent mengambil Gold!")
            kb.retract(expr(f'G_{x}_{y}'))
            kb.tell(expr(f'~G_{x}_{y}'))
            gold_grabbed = True
            print("  📝 KB diperbarui: Gold sudah diambil.\n")
            break
 
        # Cek sel berikutnya sebelum melangkah
        if step < len(route_to_gold) - 1:
            nx, ny = route_to_gold[step + 1]
            print(f"\n  🧭 Mengecek sel berikutnya ({nx},{ny}) sebelum melangkah:")
            ok_next = ask_and_print(kb, f'OK_{nx}_{ny}', f"({nx},{ny}) aman?")
            ask_and_print(kb, f'P_{nx}_{ny}',  f"ada PIT di ({nx},{ny})?")
            ask_and_print(kb, f'W_{nx}_{ny}',  f"ada Wumpus di ({nx},{ny})?")
            if ok_next is True:
                print(f"  ➡️  ({nx},{ny}) aman — Agent melangkah maju.\n")
            else:
                print(f"  ⛔ ({nx},{ny}) BERBAHAYA — Agent berhenti!\n")
                break
        print()
 
    # ----- Perjalanan Pulang -----
    if gold_grabbed:
        print("=" * 60)
        print("  AGENT PULANG MEMBAWA GOLD")
        print("=" * 60)
        for step, (x, y) in enumerate(route_home):
            print(f"\n  PULANG LANGKAH {step + 1}: Agent di ({x},{y})")
            ask_and_print(kb, f'OK_{x}_{y}', "sel aman untuk dilalui?")
 
        print("\n" + "=" * 60)
        print("  🏠 Agent tiba di (1,1) dengan SELAMAT!")
        print("  🏆 Misi SUKSES: Gold/Totem berhasil dibawa pulang!")
        print("=" * 60)
    else:
        print("❌ Agent gagal menemukan Gold.")
 
 
# ============================================================
# 5. QUERY TAMBAHAN
# ============================================================
 
def additional_queries(kb):
    """Pertanyaan-pertanyaan tambahan untuk demonstrasi ask_if_true."""
    print("\n" + "=" * 60)
    print("  PERTANYAAN TAMBAHAN KE KB (ask_if_true)")
    print("=" * 60 + "\n")
 
    queries = [
        # PIT
        ("P_3_4",  "PIT di (3,4)?"),
        ("P_4_3",  "PIT di (4,3)?"),
        ("P_3_2",  "PIT di (3,2)?"),
        ("P_1_1",  "PIT di (1,1) [start]?"),
        ("P_1_4",  "PIT di (1,4) [gold cell]?"),
        # Wumpus
        ("W_2_3",  "Wumpus di (2,3)?"),
        ("W_1_1",  "Wumpus di (1,1)?"),
        # Breeze
        ("B_2_1",  "Breeze di (2,1)?"),
        ("B_1_1",  "Breeze di (1,1)?"),
        ("B_4_2",  "Breeze di (4,2)?"),
        # Stench
        ("S_1_3",  "Stench di (1,3)?"),
        ("S_2_2",  "Stench di (2,2)?"),
        ("S_3_3",  "Stench di (3,3)?"),
        # Gold
        ("G_1_4",  "Gold di (1,4)?"),
        ("G_2_4",  "Gold di (2,4)?"),
        # OK
        ("OK_1_2", "(1,2) aman?"),
        ("OK_1_3", "(1,3) aman?"),
        ("OK_1_4", "(1,4) aman?"),
        ("OK_2_3", "(2,3) aman?"),
        ("OK_3_4", "(3,4) aman?"),
        ("OK_4_3", "(4,3) aman?"),
    ]
 
    for (q, desc) in queries:
        result = ask_if_true(kb, q)
        icon = "✅" if result is True else ("❌" if result is False else "❓")
        print(f"  {icon} {desc:<35} ask_if_true('{q}') => {result}")
 
 
# ============================================================
# MAIN
# ============================================================
 
if __name__ == '__main__':
    # 1. Bangun KB dari fakta dunia
    kb, pits, wumpus, gold = build_wumpus_kb()
 
    # 2. Tampilkan peta
    print_grid(pits, wumpus, gold)
 
    # 3. Agent cari gold step by step
    agent_find_gold(kb, gold)
 
    # 4. Pertanyaan tambahan
    additional_queries(kb)
 