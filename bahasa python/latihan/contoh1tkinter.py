import tkinter as tk # mengimport library tkinter sebagai tk

window = tk.Tk() # membentuk/membuat window
window.title('Form Data Mahasiswa') # memberi nama atau judul dari window
window.geometry('500x200') # mengatur letak dari window

frame1 = tk.Frame(master=window) # membuat frame pada window
frame1['relief'] = tk.GROOVE # menentukan type relief 
frame1['borderwidth'] = 4 # membuat garis pembatas
frame1.pack(side=tk.LEFT, fill=tk.Y) # mengatur letak dari frame pada window

frame2 = tk.Frame(master=window) # membuat frame pada window
frame2['relief'] = tk.RIDGE # menentukan type relief
frame2.pack(side=tk.LEFT, fill=tk.Y) # mengatur posisis dari frame pada window

list = { # membuat data list 
    0: 'Nama Lengkap', # isi record list yg pertama
    1: 'NPM', # isi record list yg kudua
    3: 'Tanggal Lahir', # isi record list yg ketiga
    4: 'Program Studi', # isi record list yg keempat
    5: 'Jurusan' # isi record list yg kelima
} # penutup dari list
i = 4 # membuat variable i
for i in list: # perulangan untuk memanggil data pada list
    label = tk.Label(master=frame1) # membuat label
    label['text'] = list[i], ':' # memasukan nilai daripada list
    label.grid(row=i, column=0, sticky=tk.W) # mengatur letak label

    entry = tk.Entry(master=frame2) # membuat tempat mengisi jawaban/entry
    entry['width'] = 50 # mengatur luas dari entry
    entry.grid(row=i, column=0, sticky=tk.W) # mengatur letak dari entry
    i = i+1 # penambahan variable i agar terjadinya pengulangan

    la = tk.Label(master=frame1) # membuat label
    la['text'] = 'Sex :' # memberi nama pada label
    la.grid(row=11, column=0, sticky=tk.W) # mengatur posisi dari label
    va = tk.IntVar() # memasukkan fungsi pemilihan
    ra1 = tk.Radiobutton(master=frame2, text='Pria', variable=va, value=1) # membuat pilihan pertama
    ra1.grid(row=10, column=0, sticky=tk.W) # mengatur letak pilihan pertama

    ra2 = tk.Radiobutton(master=frame2, text='Wanita', variable=va, value=2) # membuat pilihan kedua 
    ra2.grid(row=10, column=1, sticky=tk.W) # mengatur letak pilihan kedua

button1 = tk.Button(master=frame2) # membuat tombol 
button1['text'] = 'Submit' # memberi nama pada tombol
button1.grid(row=11, column=0, sticky=tk.W) # mengatur letak dari tombol

button2 = tk.Button(master=frame2) # membuat tombol
button2['text'] = 'Batal' # memberi nama pada tombol
button2.grid(row=11, column=1, sticky=tk.W) # mengatur letak dari tombol

window.mainloop() # fungsi agar window tetap aktif