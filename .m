import os, re platform



def Mohsin():
    #os.system('clear')
    #os.system('termux-setup-storage')
    global user
    try:
        r = open('Mohsin.txt','r').read()
    except IOError:
        name = "None"
        user = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:40.0) Gecko/20100101 Firefox/40.0'
        m=open('mohsin.txt','w')
        m.write(user)
        m.close()
        os.system ("rm -rf matrix.txt ")
        os.system ("pip2 install ipaddress")
        os.system ('pip2 install lolcat')
        os.system ('pip2 install requests')
        bit=platform.architecture()[0]
        if bit=="64bit":
            import apcb
            apcb.gf()
        elif bit=="32bit":
            import apcs
            apcs.gf()
    os.system ("rm -rf matrix.txt")
    os.system ("pip2 install ipaddress")
    os.system ('pip2 install lolcat')
    os.system ('pip2 install requests')
    bit=platform.architecture()[0]
    if bit=="64bit":
        import apcb
        apcb.gf()
    elif bit=="32bit":
        import apcs
        apcs.gf()
    
if __name__ == '__main__':
    Mohsin()
