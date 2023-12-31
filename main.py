import sys        # Untuk fungsi pada terminal, seperti autoketik() dan exit()
import subprocess # Installing python module within code / script (Tanpa requirements.txt)

try: # Imort Module
    import requests # Post, Get, dan Put URL API
    import time     # Untuk informasi waktu
    import random   # Untuk random user
    import os       # Untuk clear terminal
    import urllib3  # HTTP client untuk Python
    import json     # Agar body requests dapat dilihat dengan cara di print
    import bs4      # Untuk versi output
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "urllib3"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])
finally:
    import requests # Post, Get, dan Put URL API
    import urllib3  # HTTP client untuk Python
    from bs4 import BeautifulSoup as bs

from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post,get # Bisa langsung from requests import post dan get

# Inisialisasi Variasi Warna Output Terminal.
hijau   = "\033[1;92m"
putih   = "\033[1;97m"
abu     = "\033[1;90m"
kuning  = "\033[1;93m"
ungu    = "\033[1;95m"
merah   = "\033[1;91m"
biru    = "\033[1;96m"

# Function ini berfumgsi sebagai pengganti print(), agar lebih menarik saat terlihat di terminal.
def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

# Function ini berfungsi sebagai inforamasi waktu saat pengiriman spam berlangsung.
def countdown(time_sec):
    mins, secs = divmod(time_sec,60)
    timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{:02d}:{:02d}'.format(mins,secs)
    waktu      = time.localtime()
    keterangan_jam = time.strftime("%H:%M:%S",waktu)
    keterangan_tanggal = time.strftime("%d",waktu)
    keterangan_bulan = time.strftime("%B",waktu)
    bulan_bulan = {
        "January"    : 'Januari',
        "February"   : "Februari",
        "March"      : "Maret",
        "April"      : "April",
        "May"        : "Mei",
        "June"       : "Juni",
        "July"       : "Juli",
        "August"     : "Agustus",
        "September"  : "September",
        "October"    : "Oktober",
        "November"   : "November",
        "December"   : "Desember"
    } # Mengubah keterangan bulan menjadi bahasa Indonesia.
    bulan = bulan_bulan.get(keterangan_bulan)

    keterangan_tahun = time.strftime("%Y",waktu)

    keterangan_hari = time.strftime("%A",waktu)
    hari_hari = {
        "Sunday"    : 'Minggu',
        "Monday"    : "Senin",
        "Tuesday"   : "Selasa",
        "Wednesday" : "Rabu",
        "Thursday"  : "Kamis",
        "Friday"    : "Jum'at",
        "Saturday"  : "Sabtu"
    } # Mengubah keterangan hari menjadi bahasa Indonesia
    hari = hari_hari.get(keterangan_hari)

    print(f"{timeformat} | {putih}{hari}, {keterangan_tanggal} {bulan} {keterangan_tahun} | {putih}Waktu {keterangan_jam}",end='\r')
    time.sleep(1)
    time_sec -= 1

def tanya(nomor):
    check_input = 0
    while check_input == 0:
        a = input(f"""{putih}Apakah Kamu ingin mengulangi Spam Tools? y/t {putih}Input Kamu: {putih}""")
        if a == "y" or a == "Y":
            check_input = 1
            start(nomor,1)
            break
        elif a == "t" or a == "T":
            check_input = 1
            autoketik(f"{putih}Berhasil Keluar Dari Tools!")
            sys.exit()
            break
        else:
            print("Masukan Pilihan Dengan Benar!")
            sys.exit

def jam(nomor): # Jangan hapus!
    autoketik("Program Berjalan!")
    b   = nomor[1:12] # Contoh nomor = 081319196666
    c   = "62" + b    # Contoh nomor = 6281319196666
    rto = 0           # Flag ketika memasuki RTO maka akan program otomatis menunda proses selama 80 detik
    RTO_flag = 0
    for _ in range(10): # Looping
        try: # Sudah aman
            autoketik(f"{putih}Sukses Mengirim Spam!")
            countdown(120) # Jangan Diubah !!!!

        except requests.exceptions.ConnectionError: # Error Handling ketika Request Time Out di salah satu URL API
            if RTO_flag == 0:
                print("")
                autoketik("--Request Time Out--") # Flag ketika memasuki RTO di salah satu URL API
                print(f"{putih}Proses Automatis dialihkan ke Requests Alternatif{putih}")
            # Sudah aman
            autoketik(f"{putih}Sukses Mengirim Spam!")
            countdown(120) # Jangan diubah ngentod!
            RTO_flag = 1
            rto = 1 # Flag tunda

        except requests.exceptions.ConnectionError:
            print("")
            autoketik("--Gagal membuat koneksi baru!--")
            time.sleep(1000) # Tunda 1000 detik
            rto = 1

        # https://urllib3.readthedocs.io/en/stable/reference/urllib3.exceptions.html
        except urllib3.exceptions.NewConnectionError: # Error Handling 2 ketika masih terjadi error berlebihan
            print("")
            autoketik("--Gagal membuat koneksi baru!--")
            time.sleep(1000) # Tunda 1000 detik
            rto = 1
        
        except TimeoutError: # HTTPSConnectionPool() A Connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
            print("")
            autoketik("--A Connection attempt failed because the connected party did not properly respond after a period of time--")
            time.sleep(1000) # Tunda 1000 detik
            rto = 1
        
        except urllib3.exceptions.ProtocolError: # HTTPSConnectionPool() A Connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
            print("")
            autoketik("--A Connection attempt failed because the connected party did not properly respond after a period of time--")
            time.sleep(1000) # Tunda 1000 detik
            rto = 1
        
        except KeyboardInterrupt: # # Error Handling Ketika user menekan tombol CTRL + C atau Interrupt Terminal
            print("")
            tanya(nomor)
    if rto==1:
        time.sleep(80) # Jika sudah error RTO maka tunda dulu proses selama 80 detik
        start(nomor,1)
    else:
        start(nomor,1) # Fungsi start() dengan membawa parameter (nomor target, flag 1 yang berarti bukan perama kali masuk kedalam fungsi start())

def start(nomor,x): # Def fungsi untuk start tools
    if x == 0: # Flag ketika pertama kali masuk ke dalam fungsi start()
        os.system("cls") # Clear terminal
        autoketik(f"{putih}Infinite Loop Spam to {putih}{nomor} {putih}is {putih}Ready!{putih}") # Flag dimana program berjalan
        jam(nomor)
    else:
        print("")
        autoketik("--reboot tunggu 20 detik--")
        time.sleep(15) # Tunda 20 detik
        os.system("cls") # Clear terminal
        autoketik(f"{putih}Mengulang Spam ke Nomor : {nomor}.....{putih}") # Flag di mana program berjalan
        jam(nomor)

def main():
    os.system("cls") # Clear terminal agar cmd berwarna
    autoketik(f"Selamat datang di {putih}Bundaran HI")
    print(f"""{putih}Author : {putih} Kuli Jawa""")
    # Contoh : 081319196666
    print(nomor := input(f"{putih}Masukan Nomor: {putih}")) # Operator input nomor target
    start(nomor,0) # Mulai Tools!

try:
    main()
except KeyboardInterrupt:
    autoketik(f"""{putih}Batal Kumis {putih}--Keluar dari Tools--""")
    sys.exit()
