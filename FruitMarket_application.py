# Soal 1
a = input(f'Masukkan 5 film kesukaan anda dipisahkan dengan koma: ')
b = input(f'Masukkan 5 film kesukaan teman anda dipisahkan dengan koma: ')
c = a.split(',')
d = b.split(',')
e = set(c)
f = set(d)

z = (e.intersection(f))
persentase = (len(z)/len (e))*100
print(f' kesukaan film kalian yang sama sebesar {persentase}%')


# Soal 2

data = [['Index','Nama','Stock','Harga'], ['Apel',20, 10000], ['Jeruk', 15, 15000], ['Anggur', 25, 20000]]
cart = [['Nama', 'Qty','Harga']]
print("Selamat Datang di Pasar Buah")
print()
print('List Menu')
print('1. Menampilkan Daftar Buah \n2. Menambahkan Buah \n3. Menghapus Buah \n4. Membeli Buah')
print('5. Exit Program')
pilih = int(input(f'Masukkan angka menu yang ingin dijalankan: '))
print()
while pilih in range(1,6):
    while pilih == 1:
        #Menampilkan daftar buah
        print('Daftar Buah')
        print()
        from tabulate import tabulate
        print(tabulate(data, headers= "firstrow", showindex="always"))
        print()
        print("Selamat Datang di Pasar Buah")
        print('List Menu')
        print('1. Menampilkan Daftar Buah \n2. Menambahkan Buah \n3. Menghapus Buah \n4. Membeli Buah')
        print('5. Exit Program')
        pilih = int(input(f'Masukkan angka menu yang ingin dijalankan: '))
    while pilih == 2:
        #Menambahkan buah
        buahBaru = input('Masukkan nama buah: ')
        stockBaru = int(input('Masukkan jumlah stock: '))
        hargaBaru = int(input('Masukkan harga buah: '))
        print()
        dataBaru = [buahBaru, stockBaru, hargaBaru]
        data.append(dataBaru)
        print('Daftar Buah')
        from tabulate import tabulate
        print(tabulate(data, headers= "firstrow", showindex="always"))
        print()
        print("Selamat Datang di Pasar Buah")
        print('List Menu')
        print('1. Menampilkan Daftar Buah \n2. Menambahkan Buah \n3. Menghapus Buah \n4. Membeli Buah')
        print('5. Exit Program')
        pilih = int(input(f'Masukkan angka menu yang ingin dijalankan: '))
    while pilih == 3:
        # Menghapus buah
        print('Daftar Buah')
        from tabulate import tabulate
        print(tabulate(data, headers= "firstrow", showindex="always"))
        hapusbuah = int(input('Masukkan index buah yang ingin dihapus: '))
        for i in range(len(data)- 1):
            if i == hapusbuah:
                del data[i + 1]
        from tabulate import tabulate
        print(tabulate(data, headers= "firstrow", showindex="always"))
        print()
        print("Selamat Datang di Pasar Buah")
        print('List Menu')
        print('1. Menampilkan Daftar Buah \n2. Menambahkan Buah \n3. Menghapus Buah \n4. Membeli Buah')
        print('5. Exit Program')
        pilih = int(input(f'Masukkan angka menu yang ingin dijalankan: '))
    while pilih == 4:
        # Membeli buah
        print('Daftar Buah')
        from tabulate import tabulate
        print(tabulate(data, headers= "firstrow", showindex="always"))
        beli = int(input('Masukkan index buah yang ingin dibeli: '))
        stockbuah = int(input('Masukkan jumlah buah yang ingin dibeli: '))
        print()
        if stockbuah > data[beli +1][1]:
            print(f'Stock kurang, stock {data[beli+1][0]} sisa {data[beli+1][1]}')
            from tabulate import tabulate
            print(tabulate(cart, headers = "firstrow"))
            break
        elif stockbuah < data[beli + 1][1]:
            data[beli + 1][1] -= stockbuah
            databeli = data[beli + 1].copy()
            keranjang = (databeli)
            keranjang[1] = stockbuah
            cart.append(keranjang)           
            from tabulate import tabulate
            print(tabulate(cart, headers = "firstrow"))
            total = 0
            for i in range(len(cart)):
                if i >= 1:
                    x = cart[i][1]
                    y = cart[i][2]
                    xy = (x*y)
                    total += xy
            print(f"Total belanja sebesar Rp {total}")
        print()
        againlagi = str(input('Apakah anda ingin melanjutkan belanja? (Ya/Tidak)')).title()
        if againlagi == 'Tidak':
            uang = int(input('Masukkan jumlah uang: '))
            if uang < total:
                print(f'Transaksi anda dibatalkan uangnya kurang sebesar {total-uang}')
            elif uang == total:
                print('Terima kasih')
            elif uang > total:
                print(f'Terima kasih \n Uang kembali anda: {uang-total}')
        else:
            continue
    while pilih == 5:
        print('Exit Program')
        break