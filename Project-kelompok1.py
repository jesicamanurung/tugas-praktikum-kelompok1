print('        ITH COFFEE       ')
print('===========================')

nama = input('Nama Pelanggan    : ')
tanggal = input('Tanggal Pembelian : ')
print('===========================')
print('     =====MENU=====    ')
print('1. Coffee                Rp.25000')
print('2. Matcha                Rp.18000')
print('3. Milkshake             Rp.15000')
print('4. Es Teh                Rp.10000')
print('     =====MENU=====    ')
h = []
menu_dict = {1: 25000, 2: 18000, 3: 15000, 4: 10000}

menu_pesanan = int(input('Masukan Menu Pesanan (nomor menu) : '))
harga = menu_dict.get(menu_pesanan, 0)

while harga == 0:
    print('===Menu tidak tersedia, silahkan pilih menu lainnya ===')
    menu_pesanan = int(input('Masukan Menu Pesanan (nomor menu) : '))
    harga = menu_dict.get(menu_pesanan, 0)

jumlah_pembelian = int(input('Masukan Jumlah Pembelian : '))
for _ in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input('Apakah ada pesanan yang ingin ditambah/dikurangi? tambah/kurang/tidak: ')
    if jawab == 'tambah':
        tambah = int(input('Masukan Menu Pesanan: '))
        harga_tambahan = menu_dict.get(tambah, 0)

        while harga_tambahan == 0:
            print('===Menu tidak tersedia, silahkan pilih menu lainnya ===')
            tambah = int(input('Masukan Menu Pesanan (nomor menu) : '))
            harga_tambahan = menu_dict.get(tambah, 0)

        jumlah_tambahan = int(input('Masukkan Jumlah Pembelian : '))
        for _ in range(jumlah_tambahan):
            h.append(harga_tambahan)
        c = jumlah_tambahan + jumlah_pembelian
        print('Total Pesanan: ', c)
        bayar = sum(h)
        uang = int(input('Uang Tunai Pembeli : Rp.'))
        kembalian = uang - bayar
        print('Kembalian : Rp.', kembalian)
        break
    elif jawab == 'kurang':
        kurang = int(input('Berapa jumlah yang dikurangkan? :'))
        if kurang <= jumlah_pembelian:
            for _ in range(kurang):
                h.pop()
            c = jumlah_pembelian - kurang
            print('Total Pesanan: Rp.', c)
            bayar = sum(h)
            uang = int(input('Uang Tunai Pembeli : Rp.'))
            kembalian = uang - bayar
            print('Kembalian : Rp.', kembalian)
            break
        else:
            print('Jumlah yang dikurangkan melebihi jumlah pesanan.')
    else:
        bayar = sum(h)
        c = jumlah_pembelian
        print(' Total Pesanan :', c)
        print(' Total Pembayaran : Rp.{}'.format(bayar))
        uang = int(input('Uang Tunai Pembeli : Rp.'))
        kembalian = uang - bayar
        print('Kembalian : Rp.', kembalian)
        break

print('===========S T R U K============')
print('Nama\t\t\t:', nama)
print('Tanggal Pembelian\t:', tanggal)
print('Jumlah Pesanan\t\t:', c)
print('Total Pembayaran\t: Rp.', bayar)
print('Dibayar\t\t\t: Rp.', uang)
print('Kembalian\t\t: Rp.', kembalian)
