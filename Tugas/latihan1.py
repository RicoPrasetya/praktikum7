print("Nama : Rico Prasetya")
print("NIM  : 312210425")

daftarkontak = {"Nama": "Nomer Telepon"}
kontak = {'Ari': '081267888', 'Dina': '087677776'}

# print
print("============================")
print("|   # Nama   |Nomor Telepon|")
print("============================")
print("|   # Ari    |  ", kontak['Ari'], '|')
print("|   # Dina   |  ", kontak['Dina'], '|')
print("============================")
print()

# Tampilkan kontaknya Ari
print("# Tampilkan kontaknya Ari")
print("===========================")
print("|    Ari     | ", kontak['Ari'], '|')
print("===========================")
print()

# Tambah kontak baru dengan nama Riko, nomor 087654544
print("# Tambah kontak baru dengan nama Riko, nomor 087654544")
kontak['Riko'] = '087654544'
print("===========================")
print("|    Riko    | ", kontak['Riko'], '|')
print("===========================")
print()

# Ubah kontak Dina dengan nomor baru 088999776
print("# Ubah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print("===========================")
print("|    Dina    | ", kontak['Dina'], '|')
print("===========================")
print()

# Tampilkan semua Nama
print("# Tampilkan semua Nama")
print("==================================")
print(kontak.keys())
print("==================================")
print()

# Tampilkan semua Nomor
print("# Tampilkan semua Nomor")
print("====================================================")
print(kontak.values())
print("====================================================")
print()

# Tampilkan daftar Nama dan nomornya
print("# Tampilkan daftar Nama dan nomornya")
print("================================================================================")
print(kontak.items())
print("================================================================================")
print()

# Menghapus kontak Dina
print("# Hapus kontak Dina")
print("=========================================================")
kontak.pop('Dina')
print(kontak.items())
print("=========================================================")