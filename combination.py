toplam=0
def yazdir(bir,iki,uc,dort,bes):
    print(bir+iki+uc+dort+bes)
    print(bir+iki+dort+uc+bes)
    print(bir+uc+iki+dort+bes)
    print(bir+uc+dort+iki+bes)
    print(bir+dort+iki+uc+bes)
    print(bir+dort+uc+iki+bes)
    print(bir+iki+uc+bes+dort)
    print(bir+iki+dort+bes+uc)
    print(bir+uc+iki+bes+dort)
    print(bir+uc+dort+bes+iki)
    print(bir+dort+iki+bes+uc)
    print(bir+dort+uc+bes+iki)
    print(bir+iki+bes+uc+dort)
    print(bir+iki+bes+dort+uc)
    print(bir+uc+bes+iki+dort)
    print(bir+uc+bes+dort+iki)
    print(bir+dort+bes+iki+uc)
    print(bir+dort+bes+uc+iki)
    print(bir+bes+iki+uc+dort)
    print(bir+bes+iki+dort+uc)
    print(bir+bes+uc+iki+dort)
    print(bir+bes+uc+dort+iki)
    print(bir+bes+dort+iki+uc)
    print(bir+bes+dort+uc+iki)

print("\n\nMerhaba\nCoded by acap1t \n\n\n")
print("5 Char giriniz!")
bir = str(input("#>"))
iki = str(input("#>"))
uc = str(input("#>"))
dort = str(input("#>"))
bes = str(input("#>"))
print("[+]Basliyoruz!\n----\n\n")


yazdir(bir,iki,uc,dort,bes)
yazdir(iki,bir,uc,dort,bes)
yazdir(uc,bir,iki,dort,bes)
yazdir(dort,bir,iki,uc,bes)
yazdir(bes,bir,iki,uc,dort)
print("Islem tamamlandi.\n120 Kombinasyon Yazildi")

