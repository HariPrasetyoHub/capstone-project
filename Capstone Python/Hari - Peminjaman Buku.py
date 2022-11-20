database = {
            '2022110001':
            {'customer'     : 'Beri',
             'bookName'     : 'Harry Potter 1',
             'borrowDate'   : '15/11/2022',
             'returnDate'   : '17/11/2022' },
            
            '2022110002':
            {'customer'     : 'James',
             'bookName'     : 'Narnia Chronicle',
             'borrowDate'   : '15/11/2022',
             'returnDate'   : '18/11/2022' },

            '2022110003':          
            {'customer'     : 'Aerith',
             'bookName'     : 'Final Fantasy VII',
             'borrowDate'   : '17/11/2022',
             'returnDate'   : 'Belum dikembalikan' },

             '2022110004':          
            {'customer'     : 'Stark',
             'bookName'     : 'Marvel Comic Vol.1',
             'borrowDate'   : '18/11/2022',
             'returnDate'   : 'Belum dikembalikan'}
             }

def readData():    
    while True:
        inputReadData = input('''    

MENU 1 - MENAMPILKAN DATA
         1. Semua data peminjaman buku
         2. Cari data berdasarkan nomor ID peminjaman
         9. Kembali ke Menu Utama
         > Masukkan angka MENU 1 untuk menampilkan data:''')

        if inputReadData == '1':
            if database == {} :
                print('\n!! TIDAK ADA DATA PEMINJAMAM BUKU !!')
            else:
                print('\n\n___DATA PEMINJAMAN BUKU___\n\nNOMOR ID \t|NAMA PEMINJAM \t|JUDUL BUKU\t\t|TANGGAL PINJAM\t|TANGGAL KEMBALI') 
                for i in database.keys():
                    print(i,'\t|{}     \t|{}  \t|{}\t|{}'.format(database[i]['customer'],database[i]['bookName'],database[i]['borrowDate'],database[i]['returnDate']))
                    
        elif inputReadData == '2':
            if database == {} :
                print('\n!! TIDAK ADA DATA PEMINJAMAM BUKU !!')
                
            else:
                inputReadNomorID = input('\nMasukkan Nomor ID yang ingin dicari:')             
                if inputReadNomorID in database:
                    print('\n\nNOMOR ID PEMINJAMAN: {}\n\nNAMA PEMINJAM \t|JUDUL BUKU\t\t|TANGGAL PINJAM\t|TANGGAL KEMBALI'.format(inputReadNomorID))
                    print('{}     \t|{}  \t|{}\t|{}\n'.format(database[inputReadNomorID]['customer'],database[inputReadNomorID]['bookName'],database[inputReadNomorID]['borrowDate'],database[inputReadNomorID]['returnDate']))
                else:
                    print('\n!! DATA TIDAK DITEMUKAN, SILAHKAN PERIKSA KEMBALI !!')
        elif inputReadData == '9': 
            break
        else:
            print('\n!! Menu Tidak Ditemukan. Periksa Kembali Pilihan Anda !!')

def addData():
    while True:
        inputAddData = input('''    
MENU 2 - MENAMBAH DATA BARU
         1. Menambah data baru
         9. Kembali ke Menu Utama
         > Masukkan angka MENU 2 untuk menambah data baru:''')
        if inputAddData == '1':
                addNomorID = input('\nMasukkan Nomor ID baru\t:')
                if addNomorID in database:
                    print('\n!! NOMOR ID SUDAH ADA, SILAHKAN PERIKSA KEMBALI !!')
                    
                else:
                    addCustomer = input('Masukkan nama peminjam\t:')
                    addBookName = input('Masukkan judul buku\t:') 
                    addBorrowDate = input('Masukkan tanggal pinjan (DD/MM/YYYY)\t:')
                    while True:
                        addQuestion = input('Apakah Anda ingin menyimpan data tersebut? (Y/N):').lower()
                        if addQuestion == 'y': 
                            database[addNomorID]= { 'customer' : addCustomer,
                                                    'bookName'  : addBookName,
                                                    'borrowDate'   : addBorrowDate,
                                                    'returnDate'   : 'Belum dikembalikan'}
                            print('\n* Data Baru Sudah Tersimpan * \n')
                            break
                        elif addQuestion == 'n':
                            break
                        else: 
                            print('Jawab dengan "Y" atau "N"')
                    
        elif inputAddData == '9': 
            break
        else:
            print('\n!! Menu Tidak Ditemukan. Periksa Kembali Pilihan Anda !!\n')

def updateData():
    while True:
        inputUpdateData = input('''    
MENU 3 - UPDATE DATA 
         1. Update data berdasarkan Nomor ID Peminjaman
         9. Kembali ke Menu Utama
         > Masukkan angka MENU 3 untuk Update data:''')
        if inputUpdateData == '1':

            updateNomorID = input('\n> Masukkan Nomor ID yang akan di-update:')
            if updateNomorID not in database:
                print('\n!! NOMOR ID TIDAK DITEMUKAN, SILAHKAN PERIKSA KEMBALI !!')
            else:
                print('\n\nNOMOR ID PEMINJAMAN: {}\n\nNAMA PEMINJAM \t|JUDUL BUKU\t\t|TANGGAL PINJAM\t|TANGGAL KEMBALI'.format(updateNomorID))
                print('{}     \t|{}  \t|{}\t|{}\n'.format(database[updateNomorID]['customer'],database[updateNomorID]['bookName'],database[updateNomorID]['borrowDate'],database[updateNomorID]['returnDate']))
            
                updateColumn = input(
            '''Kolom yang dapat di-Update
                1. Nama Peminjam
                2. Judul Buku
                3. Tanggal Pinjam
                4. Tanggal Kembali
                5. Tidak jadi meng-update data
                > Masukkan angka kolom yang ingin di-Update:''')
                if updateColumn == '1':
                    updateCustomer = input('\nMasukkan Update Nama Peminjam:')
                    while True:
                        updateCustomerQuestion = input('\nApakah Anda yakin ingin mengganti Nama Peminjam ({}) >>>>> ({})? (Y/N):'.format(database[updateNomorID]['customer'],updateCustomer)).lower()
                        if updateCustomerQuestion == 'y':
                            database[updateNomorID]= {'customer' : updateCustomer,                                  #Ter-Update
                                                    'bookName'  : database[updateNomorID]['bookName'],         #Tidak di-Update
                                                    'borrowDate'   : database[updateNomorID]['borrowDate'],    #Tidak di-Update
                                                    'returnDate'   : database[updateNomorID]['returnDate']}    #Tidak di-Update
                            print ('\n* Data Nama Peminjam Berhasil Di-Update *\n')
                            break
                        elif updateCustomerQuestion == 'n':
                            break
                        else:
                            print ('Jawab dengan "Y" atau "N"')
                
                elif updateColumn == '2':
                    updateBookName = input('\nMasukkan Update Judul Buku:')
                    while True:
                        updateBookQuestion = input('\nApakah Anda yakin ingin mengganti Judul Buku({}) >>>>> ({})? (Y/N):'.format(database[updateNomorID]['bookName'],updateBookName)).lower()
                        if updateBookQuestion == 'y':
                            database[updateNomorID]= {'customer' : database[updateNomorID]['customer'],        #Tidak di-Update
                                                    'bookName'  : updateBookName,                                   #Ter-Update
                                                    'borrowDate'   : database[updateNomorID]['borrowDate'],    #Tidak di-Update
                                                    'returnDate'   : database[updateNomorID]['returnDate']}    #Tidak di-Update
                            print ('\n* Data Judul Buku Berhasil Di-Update *\n')
                            break
                        elif updateBookQuestion == 'n':
                            break
                        else:
                            print ('Jawab dengan "Y" atau "N"')

                elif updateColumn == '3':
                    updateBorrowDate = input('\nMasukkan Update Tanggal Pinjam (DD/MM/YYYY):')
                    while True:
                        updateBorrowQuestion = input('\nApakah Anda yakin ingin mengganti Tanggal Pinjam ({}) >>>>> ({})? (Y/N):'.format(database[updateNomorID]['borrowDate'],updateBorrowDate)).lower()
                        if updateBorrowQuestion == 'y':
                            database[updateNomorID]= {'customer' : database[updateNomorID]['customer'],        #Tidak di-Update
                                                    'bookName'  : database[updateNomorID]['bookName'],         #Tidak di-Update
                                                    'borrowDate'   : updateBorrowDate,                              #Ter-Update
                                                    'returnDate'   : database[updateNomorID]['returnDate']}    #Tidak di-Update
                            print ('\n* Data Tanggal Pinjam Berhasil Di-Update *\n')
                            break
                        elif updateBorrowQuestion == 'n':
                            break
                        else:
                            print ('Jawab dengan "Y" atau "N"')

                elif updateColumn == '4':
                    updateReturnDate = input('\nMasukkan Tanggal Pengembalian Buku (DD/MM/YYYY):')
                    while True:
                        updateReturnQuestion = input('\nApakah Anda yakin buku tersebut dikembalikan tanggal ({})? (Y/N):'.format(updateReturnDate)).lower()
                        if updateReturnQuestion == 'y':
                            database[updateNomorID]= {'customer' : database[updateNomorID]['customer'],        #Tidak di-Update
                                                    'bookName'  : database[updateNomorID]['bookName'],         #Tidak di-Update
                                                    'borrowDate'   : database[updateNomorID]['borrowDate'],    #Tidak di-Update
                                                    'returnDate'   : updateReturnDate   }                           #Ter-Update
                            print ('\n* Data Tanggal Kembali Berhasil Di-Update *\n')
                            break
                        elif updateReturnQuestion == 'n':
                            break
                        else:
                            print ('Jawab dengan "Y" atau "N"')
                elif updateColumn == '5':
                    continue
                else:
                    print('\n!! Menu Tidak Ditemukan. Periksa Kembali Pilihan Anda !!\n') 
                   
        elif inputUpdateData == '9': 
            break
        else:
            print('\n!! Menu Tidak Ditemukan. Periksa Kembali Pilihan Anda !!\n') 

def deleteData():
    while True:
            inputDeleteData = input('''    
MENU 4 - MENGHAPUS DATA
         1. Menghapus data berdasarkan NOMOR ID
         9. Kembali ke Menu Utama
         > Masukkan angka MENU 4 untuk menghapus data:''')
            if inputDeleteData == '1':
                deleteNomorID = input('\nMasukkan Nomor ID yang akan dihapus:')
                if deleteNomorID not in database:
                    print('\n!! DATA TIDAK DITEMUKAN, SILAHKAN PERIKSA KEMBALI !!')
                else:
                    print('\n\nNOMOR ID PEMINJAMAN: {}\n\nNAMA PEMINJAM \t|JUDUL BUKU\t\t|TANGGAL PINJAM\t|TANGGAL KEMBALI'.format(deleteNomorID))
                    print('{}     \t|{}  \t|{}\t|{}\n'.format(database[deleteNomorID]['customer'],database[deleteNomorID]['bookName'],database[deleteNomorID]['borrowDate'],database[deleteNomorID]['returnDate']))
                    while True:
                        deleteDataQuestion = input ('\n! Apakah Anda yakin akan menghapus data tersebut? (Y/N):').lower()
                        if deleteDataQuestion == 'y':
                            del database[deleteNomorID]
                            print('\n* Data dengan Nomor ID {} Berhasil Dihapus *\n'.format(deleteNomorID))
                            break
                        elif deleteDataQuestion == 'n':
                            break
                        else:
                            print ('Jawab dengan "Y" atau "N"')

            elif inputDeleteData == '9': 
                break
            else:
                print('\n!! Menu Tidak Ditemukan. Periksa Kembali Pilihan Anda !!\n') 

    
# MENU UTAMA
while True:
    menu =  input('''    
---PROGRAM PEMINJAMAN BUKU PERPUSTAKAAN---\n
MENU UTAMA
1. Tampilkan Data Peminjaman Buku
2. Tambah Data Baru
3. Update Data Peminjaman
4. Hapus Data 
0. Exit Program\n
> Masukkan angka Menu yang ingin dijalankan : ''')
    
    if menu == '1' :
        readData()
    elif menu == '2' :
        addData() 
    elif menu == '3' :
        updateData()
    elif menu == '4' :
        deleteData()   
    elif menu == '0' :
        print('\nTerima Kasih, Sampai Jumpa!')
        break
    else:
        print('\n\n!! MENU TIDAK DITEMUKAN, SILAHKAN PERIKSA KEMBALI PILIHAN ANDA !!')

