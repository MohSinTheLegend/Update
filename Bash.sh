import sys,os,string,random,time
def exit():
    os.system("exit")
a = "\x1b[1;93m"
c = "\x1b[1;97m"
list = [a,c]
for i in range(1,150):
        warna = random.choice(list)
        try:
    
            
                 sys.stdout.write(warna +"\r                  [MOHSIN ALI]")
                 sys.stdout.flush()
                 time.sleep(1./17)
        except KeyboardInterrupt:
                print ("\x1b[1;97m")
                exit()
