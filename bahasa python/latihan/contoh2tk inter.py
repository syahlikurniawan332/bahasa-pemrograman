from tkinter import * # mengimport gui/tkinter
from tkinter import ttk, messagebox as tkMessageBox # mengimport ttk dan messagebox dari tkinter
import sqlite3 # meng import databases

class DataSiswa(object): # sebagai class data siswa 
    def _init_(self): # ini sebagai function atau fungsi untuk self
        self.window = Tk() # membuat class window  
        self.window.title('Membuat Aplikasi CRUD TKinter') # membuat judul windownya
        self.lebar = self.window.winfo_screenwidth() / 2 # mengatur lebar windownya
        self.tinggi = self.window.winfo_screenheight() / 2 # mengatur tinggi windownya

        self.frame1 = Frame( #membuat class frame
            self.window, #membuat class window dalam class frame
            height = self.tinggi / 2, # mengatur tinggi window
            width = self.lebar # mengatur lebar window
        )
        self.frame1['relief'] = GROOVE # menentukan type dari relief    
        self.frame1.grid_propagate(0) # menentukan letak dari grid
        self.frame1.pack(side=LEFT, fill=X, expand=False) # mengatur posisi dari window   

        self.frame2 = Frame( # membuat class frame yang ke 2
            self.window, #membuat class window pada class frame 2
            height = self.tinggi / 2, # mengatur tinggi window
            width = self.lebar / 3 # mengatur lebar window
        )
        self.frame2['relief'] = RIDGE # menentukan type dari relief
        self.frame2.grid_propagate(0) # menentukan letak dari grid
        self.frame2.pack(side=RIGHT)  # mengatur posisi dari window 

        btn_add = Button(self.frame2) # membuat tombol
        btn_add['text'] = 'Tambah' # mengganti nama tombol
        btn_add['command'] = self.add_data # menambah dan menjalankan fungsi pada tombol
        btn_add.grid(row=12, column=0, sticky=W + E) # mengatur posisi tombolnya

        btn_all = Button(self.frame2) # membuat tombol
        btn_all['text'] = 'All Data' # mengganti nama tombol
        btn_all['command'] = self.get_data # menambah dan menjalankan fungsi pada tombol
        btn_all.grid(row=12, column=1, sticky=W + E) # mengatur posisi tombolnya

        btn_exit = Button(self.frame2) # membuat tombol
        btn_exit['text'] = 'Exit' # mengganti nama tombol
        btn_exit['command'] = self.exit # menambah dan menjalankan fungsi pada tombol
        btn_exit.grid(row=12, column=2, sticky=W + E) # mengatur posisi tombolnya

        self.btn_update = Button( # membuat class update dan memanggil fungsi tombol
            self.frame2, # memanggil class fungsi dari frame 2
            text='Update', # membuat nama tombol menjadi update
            command=self.update_data, # menjalankan fungsi
            state=DISABLED # kondisi dari tombol
        )
        self.btn_update.grid(row=13, column=0, sticky=W + E) # mengatur tata letak tombol

        self.btn_delete = Button( # membuat class delete dan memanggil fungsi tombol
            self.frame2,  # memanggil class fungsi dari frame 2
            text='Hapus', # membuat nama tombol menjadi hapus
            command=self.delete_data, # menjalankan fungsi
            state=DISABLED # kondisi dari tombol
        )
        self.btn_delete.grid(row=13, column=1, sticky=W + E) # mengatur tata letak tombol
    
    def exit(self): # fungsi keluar dari window
        apakah = tkMessageBox.askquestion( # memunculkan message box
            'Mau keluar dari Aplikasi ini?', # teksnya
            'Apakah mau keluar dari program?', # teksnya
            icon='warning' # ikon pesan yang akan di tampilkan
        )
        if apakah == 'yes': # kondisi
            self.window.destroy() # # perintah menutup window
            exit() # menjalankan fungsi exit

    def db_name(self): # fungsi membuat databases untuk class self
        global conn, cursor # menghubungkan cursor
        conn = sqlite3.connect('datasiswa.db') # mengkoneksikan databasesnya
        cursor = conn.cursor() # membuat class cursor
        cursor.execute('''CREATE TABLE IF NOT EXISTS datasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nama CHAR,
            npm INT,
            jurusan CHAR,
            gender CHAR            
        );''')

    def selected_data(self, query, parameters=[]): # fungsi memilih data
        self.db_name() # memanggil fungsi db_name
        cursor.execute(query, parameters) # menjalankan perintah dari cursor
        conn.commit() # menjalankan fungsi commit
    
    def add_data(self): # membuat fungsi add_data
        for widget in self.frame1.winfo_children(): # perulangan menjalankan fungsi
            widget.grid_forget() # menjalankan fungsi grid         
        
        ListLabel = ('Nama Lengkap', 'NPM', 'Jurusan') # list data yang di entry ke databases

        for i, l in enumerate(ListLabel): # perulangan
            globals()['label%s' % i] = Label(self.frame1, text=l).grid(row=i, column=0, sticky=W) # mengatur tata letak label

        text1 = StringVar() # menentukan type data dari text satu
        text2 = IntVar() # menentukan type data dari text dua
        text3 = StringVar() # menentukan type data dari text tiga
        textG = StringVar() # menentukan type data dari text G

        text_1 = Entry( # membuat entry text satu
            self.frame1, # fungsi frame 
            width = 30, # mengatur luasnya dari text 1
            textvariable=text1 # membuat class yang memasukkan text satu
        )
        text_1.grid(row=0, column=1, sticky=S) # mengatur letak teks
        text_1.focus() # untuk fokus ke teks 1

        text_2 = Entry( # membuat entry text 2
            self.frame1, # fungsi frame 
            width = 30, # mengatur luasnya dari text 2
            textvariable=text2 # membuat class yang memasukkan text 2
        ).grid(row=1, column=1, sticky=S) # mengatur letak teks 2

        text_3 = Entry( # membuat entry text 3
            self.frame1,# fungsi frame
            width = 30, # mengatur luasnya dari text 3
            textvariable=text3 # membuat class yang memasukkan text 3
        ).grid(row=2, column=1, sticky=S) # mengatur letak teks 3
        
        choice = {'Pria', 'Wanita'}    # fungsi untuk memilih    
        #textG.set('Pria')
        text_G = OptionMenu(# membuat menu pilihan
            self.frame1, # memanggil fungsi frame 
            textG, # class
            *choice #pilihan
        ).grid(row=3, column=1, sticky=W) # mengatur letak
        
        def btn_save(): # fungsi untu tombol menyimpan
            query = 'INSERT INTO datasiswa VALUES(NULL, ?, ?, ?, ?)'   # urutan penyimpanan data         
            parameters = (text1.get(), text2.get(), text3.get(), textG.get()) # paramter untuk memasukkan data
            tkMessageBox.showinfo( # untuk menampilkan pesan
                'Berhasil',
                'Data siswa berhasil disimpan'
            )            
            self.selected_data(query, parameters) # menjalankan funsi selected_data            
            return self.add_data() # mengembalikan keadaan fungsi add_data

        btn_sv = Button( # membuat tombol menyimpan
            self.frame1, # fungsi frame
            text='Simpan', # nama tombol
            command=btn_save # memasukkan fungsi kedalam tombol save
        ).grid(row=12, column=0, sticky=E) # mengatur tata letak
    
    def get_data(self):# fungsi mengambil data
        for widget in self.frame1.winfo_children(): # perulangan 
            widget.grid_forget() # memasukkan fungsi grid

        query = "SELECT * FROM datasiswa" # urutan mengambil data dari databases
        self.selected_data(query) # menjalankan pemilihan data
        Data = cursor.fetchall() # data yang dipilih oleh cursor

        self.tree = ttk.Treeview(self.frame1)  # membuat fungsi tree atau tampilan menurun
        self.tree['columns'] = ('NPM', 'Jurusan', 'Gender')  # membentuk comumn penyususan data
        self.tree.heading('#0', text='Nama')  # memberikan indeks pada column
        self.tree.heading('#1', text='NPM')  # memberikan indeks pada column
        self.tree.heading('#2', text='Jurusan') # memberikan indeks pada column
        self.tree.heading('#3', text='Gender') # memberikan indeks pada column
        for i, v in enumerate(Data): # perulangan
            self.tree.grid(row=i)  # memfokus kan pada tree row i
            self.tree.insert('', END, iid=v[0], text=v[1], values=(v[2], v[3], v[4])) # memasukkan data sesuai indeks
        self.tree.bind('', self.on_select) # melakukan bind pada data yang diselect
        cursor.close() # melakukan bind pada data yang diselect
        conn.close() # menghentikan conn

    def on_select(self, event): # -> None  (fungsi untuk memilih)
        item = self.tree.selection() # item yang dipilih dari tree
        if item is not None: # kondisi jika item data
            self.btn_update['state'] = NORMAL # kondisi tombol update normal/aktif
            self.btn_delete['state'] = NORMAL # kondisi tombol update normal/aktif
        else: # konndisi jika tidak
            self.btn_update['state'] = DISABLED # kondisi tombol tidak aktif
            self.btn_delete['state'] = DISABLED # kondisi tombol tidak aktif

    def update_data(self): # fungsi update data
        for widget in self.frame1.winfo_children(): # perulangan
            widget.grid_forget() # memasukkan fungsi graid

        item = self.tree.selection() # pilihan data dari tree
        try: # coba
            item # variable 
        except IndexError as e: # indexs error
            tkMessageBox.showwarning( # memunculkan teks peringatan
                'Pilih Data',
                'Silahkan pilih data terlebih dahulu'
            ) # isi pesanya
            return # mengembalikan 
        iddata = int(item[0])  # membuat variable id data
        query = "SELECT * FROM datasiswa WHERE id = ? ;"  # pengambilan data sesuai dari id
        self.selected_data(query, (iddata, ))  # fungsi pemilihan data
        result = cursor.fetchall() # hasil dari pilihan cursor

        ListLabel = ('Nama Lengkap', 'NPM', 'Jurusan') # list data       
        for i, l in enumerate(ListLabel): # perulangan       
            globals()['label%s' % i] = Label(self.frame1, text=l).grid(row=i, column=0, sticky=W) # posisi label

        text1 = StringVar(value=result[0][1])  # memasukkan value sesuai indeks
        text2 = IntVar(value=result[0][2])  # memasukkan value sesuai indeks
        text3 = StringVar(value=result[0][3])  # memasukkan value sesuai indeks
        textG = StringVar(value=result[0][4])  # memasukkan value sesuai indeks

        text_1 = Entry( # membuat entry text 1
            self.frame1,  # fungsi frame
            width = 30, # mengatur luas text 1
            textvariable=text1 # membuat variable yg memuat text 1
        )
        text_1.grid(row=0, column=1, sticky=S) # mengatur posisi dari text 1
        text_1.focus() # memfokuskan fungsi

        text_2 = Entry( # membuat text entry 2
            self.frame1, # fungsi frame
            width = 30, # luas text2
            textvariable=text2 # variable yang loading ke dalam text 2
        ).grid(row=1, column=1, sticky=S) # mengatur letak text 2

        text_3 = Entry( # membuat text entry 3
            self.frame1, # fungsi frame
            width = 30, #luas text3 
            textvariable=text3 # variable yang loading ke dalam text 3
        ).grid(row=2, column=1, sticky=S) # mengatur tata letak ke dalam text3 
        
        choice = {'Pria', 'Wanita'} # membuat pilihan        
        #textG.set('Pria')
        text_G = OptionMenu(  # membuat fungsi piihan ganda
            self.frame1, # fungsi frame
            textG, # variable textG
            *choice # hasil pilihan
        ).grid(row=3, column=1, sticky=W) # mengatur letak
        
        def btn_save(): # membuat fungsi tombol save
            query = '''UPDATE datasiswa SET nama = ?, npm = ?, jurusan = ?, gender = ? WHERE id = ?''' # urutan penyimpanan data 
            parameters = (text1.get(), text2.get(), text3.get(), textG.get(), iddata)  # parameter memasukkan data ke databases
            tkMessageBox.showinfo( # fungsi memunculkan text/pesan setelah fungsi dijalankan
                'Berhasil',
                'Data siswa berhasil diperbarui'
            ) # pesan yang akan keluar      
            self.selected_data(query, parameters) # menjalankan fungsi data yang dipilih         
            return self.get_data() # mengembalikan  fungsi get data

        btn_sv = Button( # membuat tombol save
            self.frame1, # fungsI  frame
            text='Simpan', # nama tombolnya
            command=btn_save # memasukkan fungsi 
        ).grid(row=12, column=0, sticky=E) # mengatur letak
        cursor.close() # menghentikan cursor
        conn.close() # menghentikan conn

    def delete_data(self): # fungsi delete data
        item = self.tree.selection() # item akan menggunakan class class tree
        try: 
            if item is not None: # kondisi jika item ada maka
                apakah = tkMessageBox.askquestion( # fungsi text pertanyaan
                    'Hapus Data',
                    'Apakah kamu akan menghapus data ini?'
                )  # pesan yg ditampilkan
                if apakah == 'yes': # kondisi jika pilihan nya adalah yes maka
                    iddata = int(item[0])  # id data adalah indeks item             
                    query = "DELETE FROM datasiswa WHERE id = ? ;"  # query menghapus data sesuai id
                    self.selected_data(query, (iddata, )) # fungsi data yang dipilih
                    tkMessageBox.showinfo( # fungsi test/pesan yang ditampilkan setelah fungsi sebelumnya dijalankan
                        'Berhasil',
                        'Data berhasil dihapus'
                    )
                    self.get_data()  # menjalankan fungsi penyimpanan data
            else: # jika item tidak ada maka
                tkMessageBox.showinfo(  # menjalankan fungsi text/pesan
                    'Pilih Data',
                    'Silahkan pilih data terlebih dahulu'
                )
                self.get_data() # menjalankan fungsi mengumpulkan data/get data
        except IndexError: # kecuali indeks error
            tkMessageBox.showinfo(
                'Pilih Data',
                'Silahkan pilih data terlebih dahulu'
            )
            self.get_data()# fungsi mengumpulkan data
        cursor.close()# menghentikan cursor
        conn.close() # menghentikan conn
    
def disable_event():# fungsi menghentikan event
    pass# menjalankan fungsi pass

if __name__ == '_main_': # fungsi mempertahankan window tetap aktif
    w = DataSiswa() # memanggil class DataSiswa
    w.window.protocol("WM_DELETE_WINDOW", disable_event) # menghentikan pemutaran/penjalanan event
    w.window.mainloop() # mempertahankan window tetap aktif