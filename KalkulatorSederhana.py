#Nama : Imam Fauji Sugiarta
#NIM : 672021039

def menu():
    print("Program Kalkulator sederhana")
    print("============================")
    print("Pilih Operasi Hitung!")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")
    print("5. Exit")

menu()
input_menu = int(input("Input Operasi Hitung yang diinginkan : "))
while input_menu !=0:
    if input_menu == 1:
        jml1 = int(input("Masukan bilangan pertama : "))
        jml2 = int(input("Masukan bilangan Kedua : "))
        jumlah = jml1 + jml2
        print ("Hasil Jumlah ",jml1," + ",jml2," Adalah = ", jumlah)
        #Penjumlahan
    elif input_menu == 2:
        krg1 = int(input("Masukan bilangan pertama : "))
        krg2 = int(input("Masukan bilangan Kedua : "))
        kurang = krg1 - krg2
        print ("Hasil Pengurangan ",krg1," - ",krg2," Adalah = ", kurang)
        #Pengurangan
    elif input_menu == 3:
        bagi1 = int(input("Masukan bilangan pertama : "))
        bagi2 = int(input("Masukan bilangan Kedua : "))
        pembagian = bagi1/bagi2
        print ("Hasil Pembagian ",bagi1," : ",bagi2," Adalah = ", pembagian)
        #Pembagian
    elif input_menu == 4:
        kali1 = int(input("Masukan bilangan pertama : "))
        kali2 = int(input("Masukan bilangan Kedua : "))
        perkalian = kali1*kali2
        print ("Hasil Perkalian ",kali1," x ",kali2," Adalah = ", perkalian)
        #Perkalian
    elif input_menu == 5:
        exit()
    else:
        print("Input tidak ada!")

    print()
    menu()
    input_menu = int(input("Input Operasi Hitung yang diinginkan : "))

