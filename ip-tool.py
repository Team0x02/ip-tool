# IPtool

# Author - ghostDEFACER




print("IP TOOL HOŞGELDİNİZ")


import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        print (CY+"""
 """+Y+"""İLK TOOLUM (:"""+G+"""

     İP TOOL
"""+R+""">>"""+Y+"""----"""+CY+""" ghost0x02 - ghostDEFACER """+Y+"""----"""+R+"""<<""")

    def m3():
        try:
            print(R+"""\n
               """+R+"""██╗██████╗░░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
               """+R+"""██║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
               """+R+"""██║██████╔╝█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
               """+R+"""██║██╔═══╝░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
               """+R+"""██║██║░░░░░░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
               """+R+"""╚═╝╚═╝░░░░░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
                       """+W+"""╭Yazar: @ghost0x02 , @ghostDEFACER & @readlydex0x02
                       """+W+"""│Geliştirci:@ghost0x02 @Rattashi
                       """+W+"""│Versiyon: 1.2
                       """+W+"""│Dil: Python
        """+W+"""╭──────────────┴Tarih: 01.12.2022
        """+Y+"""│ Seçenekler"""+G+""" >>"""+Y+"""
        """+W+"""│ 1-) Kendinizi Tarayın"""+Y+"""
        """+W+"""│ 2-) Website Tarayın Örnek: google.com"""+Y+"""
        """+W+"""│ 3-) Ip Tarayın"""+Y+"""
        """+W+"""│ 4-) Çıkış
""")
            ch=int(input(CY+"Seçeneği Girdiniz: "+W))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                main()
                m3()
            elif ch==4:
                print(Y+"Çıkış yaptınız geri girmek için python3 ip-tool.py demeniz yeterli."+W)
            else:
                print(R+"\nGeçersiz!\n")
                m3()
        except ValueError:
            print(R+"\nGeçersiz!\n")
            m3()

    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(R+"\n≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠")
                print(Y+'\n>>>'+CY+' IP bilgileri\n ')
                print(G+"Durum : "+Y,data['status'],'\n')
                print(G+"1) IP ADRESİ : "+Y,data['query'],'\n')
                print(G+"2) Hat : "+Y,data['org'],'\n')
                print(G+"3) Şehir : "+Y,data['regionName'],'\n')
                print(G+"4) Şehir Kodu : "+Y,data['region'],'\n')
                print(G+"5) İlçe : "+Y,data['city'],'\n')
                print(G+"6) Mahalle Kodu : "+Y,data['zip'],'\n')
                print(G+"7) Ülke : "+Y,data['country'],'\n')
                print(G+"8) Yer\n")
                print(G+"\tEnlem : "+Y,data['lat'],'\n')
                print(G+"\tBoylam : "+Y,data['lon'],'\n')
                l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                print(R+"\n#"+Y+" Google Map Açılış : "+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" Bağlantıya Gitmek İstermisiniz?"+G+" (y|n): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\nBaşka Bir IP Bulun Yada Çıkın Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\nTekrar Deneyiniz!\n")
                        m3()
                else:
                    pr=input(R+"\n>>"+Y+" Bağlantıya Gitmek İstermisiniz?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print(R+"\n≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠")
                        print(Y+"\nBaşka Bir IP Bulun Yada Çıkın "+R+"Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print(R+"\nGeçersiz!\n")
                        m3()
                return
            except KeyError:
                print(R+"\nHata! Web Sitesi Geçersiz\n"+W)
                m3()
        except urllib.error.URLError:
            print(R+"\nHata!"+Y+" İnternet Bağlantınızı Kontrol Edin!\n"+W)
            exit()


    def main():
        u=input(G+"\n>>> "+Y+"WEB SİTESİNİN ADRESİNİ GİRİN:"+W+" ")
        if u=="":
            print(R+"\nWEB SİTESİNİN ADRESİNİ GİRİN!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)

    def main():
        u=input(G+"\n>>> "+Y+"Ip adresi girin.:"+W+" ")
        if u=="":
            print(R+"\nIp Adresi girin.")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)


    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\nİYİ GÜNLER"+W)
