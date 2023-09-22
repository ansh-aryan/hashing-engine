import hashlib
from urllib.request import urlopen
from tkinter import *
import tkinter as tk
from itertools import product


def s1():
    global sha1crack
    global sha512crack
    global sha256crack
    global md5crack
    sha1crack=True
    sha512crack=False
    sha256crack=False
    md5crack=False

def s256():
    global sha1crack
    global sha512crack
    global sha256crack
    global md5crack
    sha1crack=False
    sha512crack=False
    sha256crack=True
    md5crack=False
def s512():
    global sha1crack
    global sha512crack
    global sha256crack
    global md5crack
    sha1crack=False
    sha512crack=True
    sha256crack=False
    md5crack=False
def smd5():
    global sha1crack
    global sha512crack
    global sha256crack
    global md5crack
    sha1crack=False
    sha512crack=False
    sha256crack=False
    md5crack=True

def inp():
    global txt
    global hsh
    global sha1crack
    global sha512crack
    global sha256crack
    global md5crack
    if sha1crack == True:
        hsh=txt.get('1.0','end-1c')
    elif sha256crack == True:
        hsh=txt2.get('1.0','end-1c')
    elif sha512crack == True:
        hsh=txt3.get('1.0','end-1c')
    elif md5crack == True:
        hsh=txt4.get('1.0','end-1c')
    actual_password_hash = hsh
    url = inpu()
    wordlist = readwordlist(url).decode('UTF-8')
    guesspasswordlist = wordlist.split('\n')
    cfile=inpwo()
    try:
        f=open(cfile,'r',encoding='cp437')
        passlist=[]
        for x in f:
            x=x.strip('\n')
            passlist.append(x)
    except Exception as e:
        f=open('rockyou.txt','r',encoding='cp437')
        passlist=[]
        for x in f:
            x=x.strip('\n')
            passlist.append(x)
        pass

    # Running the Brute Force attack
    pa=bruteforce(guesspasswordlist, actual_password_hash)
    ps=bruteforce(passlist, actual_password_hash)
    if str(pa)=="None" and str(ps)=="None":
        m1=tk.Toplevel(m)
        m1.title("Error")
        lm1=Label(m1,text="Password Not Found !!",font="Georgia")
        lm1.pack()
    if str(pa) == "None":
        pa=''
    if str(ps) == "None":
        ps=''
    if ps==pa:
        ps=''
    if str(pa)!='' or str(ps)!='':
        l4=tk.Toplevel(m)
        l4.title("Success")
        ll4=Label(l4,text="Hash Cracked !!\nYour password is: "+str(pa)+str(ps),font="Georgia")
        ll4.pack()

def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        wordlistfile = urlopen("https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt").read()
        return wordlistfile
        pass
    return wordlistfile

def inpu():
    urla=txt6.get('1.0','end-1c')
    return urla

def inpwo():
    word=txt7.get('1.0','end-1c')
    return word

def bruteforce(guesspasswordlist, actual_password_hash):
    global sha1crack
    global sha512crack
    global sha256crack
    global md5crack
    if sha1crack ==True:
        for guess_password in guesspasswordlist:
            if sha1_hash(guess_password) == actual_password_hash:
                return str(guess_password)
                exit()
    elif sha256crack==True:
        for guess_password in guesspasswordlist:
            if sha256_hash(guess_password) == actual_password_hash:
                return str(guess_password)
                exit()
    elif sha512crack==True:
        for guess_password in guesspasswordlist:
            if sha512_hash(guess_password) == actual_password_hash:
                return str(guess_password)
                exit()
    elif md5crack==True:
        for guess_password in guesspasswordlist:
            if md5_hash(guess_password) == actual_password_hash:
                return str(guess_password)
                exit()

def sha1_hash(wordlistpassword):
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()

def sha256_hash(wordlistpassword):
    result = hashlib.sha256(wordlistpassword.encode())
    return result.hexdigest()

def sha512_hash(wordlistpassword):
    result = hashlib.sha512(wordlistpassword.encode())
    return result.hexdigest()

def md5_hash(wordlistpassword):
    result = hashlib.md5(wordlistpassword.encode())
    return result.hexdigest()

def getframe1():
    sha1f.deiconify()

def getframe256():
    sha256f.deiconify()

def getframe512():
    sha512f.deiconify()

def getframemd5():
    md5f.deiconify()

def getframem():
    m.deiconify()

def getframehg():
    hg.deiconify()

def getframeinpw():
    inpw.deiconify()

def getframeinpurl():
    inpurl.pack(fill='both',expand=1)

def getframeinpword():
    inpword.pack(fill='both',expand=1)

def getframewg():
    wgen.deiconify()

def gen():
    hsh=txt5.get('1.0','end-1c')
    algo=clicked.get()
    if algo =='SHA-1':
        result=''
        result = hashlib.sha1(hsh.encode())
        result=result.hexdigest()
    elif algo == 'SHA-256':
        result=''
        result=hashlib.sha256(hsh.encode())
        result=result.hexdigest()
    elif algo == 'SHA-512':
        result=''
        result=hashlib.sha512(hsh.encode())
        result=result.hexdigest()
    elif algo == 'MD5':
        result=''
        result=hashlib.md5(hsh.encode())
        result=result.hexdigest()
    tt.insert(END,"Hash Generated is: "+result)
    tt.config(state=DISABLED)
    tt.pack()

def dele():
    tt.config(state=NORMAL)
    tt.delete("1.0","end")

def getab():
    ab.deiconify()

def getins1():
    ins1.deiconify()

def getins2():
    ins2.deiconify()

def getins3():
    ins3.deiconify()

def selectinp():
    sel=svar.get()
    if sel=='URL':
        getframeinpurl()
    elif sel=='Upload':
        getframeinpword()

def wordgen():
    try:
        x=wgentxt1.get('1.0','end-1c')
    except Exception as e:
        ip=tk.Toplevel(wgen)
        ip.title("Error")
        ipl=tk.Label("Invalid Input!!")
        ipl.pack()
        pass
    lst1=[]
    lst2=[]
    try:
        y=wgentxt3.get('1.0','end-1c')
    except Exception as e:
        y=''
        pass
    try:
        w3=wgentxt4.get('1.0','end-1c')
    except Exception as e:
        w3=''
        pass
    try:
        w4=wgentxt5.get('1.0','end-1c')
    except Exception as e:
        w4=''
        pass
    lst1.append(x)
    lst2.append(y)
    lst2.append(w3)
    lst2.append(w4)
    lst4=['1','2','3','4','5','6','7','8','9','0','@','#','%','*','&','/']
    lst3=set()
    for e1,e2 in product(lst1,lst4):
        lst3.add(e1+str(e2))
    for e1,e2 in product(lst1,lst4):
        lst3.add(e1.lower()+str(e2).lower())
    for e1,e2 in product(lst3,lst2):
        lst3.add(e1+str(e2))
    for e1,e2 in product(lst3,lst2):
        lst3.add(e1.lower()+str(e2).lower())
    for e1,e2 in product(lst1,lst2):
        lst3.add(e1+str(e2))
    for e1,e2 in product(lst1,lst2):
        lst3.add(e1.lower()+str(e2).lower())
    for e1,e2 in product(lst1,lst4):
        lst3.add(e1+str(e2))
    for e1,e2 in product(lst1,lst4):
        lst3.add(e1.lower()+str(e2).lower())

    for e1,e2 in product(lst1,lst4):
        if e1!=e2:
            lst3.add(e1+str(e2))
    for e1,e2 in product(lst1,lst2):
        lst3.add(str(e2)+str(e1))
    for e1,e2 in product(lst2,lst2):
        if e1!=e2:
            lst3.add(str(e2).lower()+str(e1).lower())
    for e1,e2 in product(lst2,lst4):
        if e1!=e2:
            lst3.add(e1+str(e2))
    for e1,e2 in product(lst2,lst4):
        lst3.add(e1+str(e2))
    for e1,e2 in product(lst2,lst4):
        lst3.add(e1.lower()+str(e2).lower())
    for e1,e2 in product(lst2,lst2):
        if e1!=e2:
            lst3.add(str(e2)+str(e1))
    for e1,e2 in product(lst2,lst2):
        if e1!=e2:
            lst3.add(str(e2).lower()+str(e1).lower())
    for i in range(0,1):
        for e1,e2 in product(lst4,lst4):
            if e1!=e2:
                lst4.append(e1+str(e2))
    for e1,e2 in product(lst3,lst4):
        if e1!=e2:
            lst3.add(e1+str(e2))
    for e1,e2 in product(lst3,lst4):
        if e1!=e2:
            lst3.add(e1.lower()+str(e2).lower())

    x=set(lst3)
    f=open('wordlist.txt','w')
    for i in x:
        f.write(i+'\n')
    f.close()
    wordgenlab=tk.Label(wgen,text="Process Finished !!\n Wordlist saved as wordlist.txt")
    wordgenlab.pack()

x= tk.Tk()
x.geometry("750x250")
x.title('Hash Cracker')
l1=tk.Label(x,text="Hashing Engine",height=1,font=('Courier',30,'bold'), relief=SUNKEN, anchor=CENTER,fg='red',bg='black')
l1.pack(fill='both',pady=8)
bx1=tk.Button(x,width=30,height=1,text="Hash Cracker",font=('Arial',15,'bold'),command=lambda: [getframem(),hg.withdraw()],bg='green')
bx1.pack(padx='8.0',pady='5.0')
bx2=tk.Button(x,width=30,height=1,text="Hash Generator",font=('Arial',15,'bold'),command=lambda: [getframehg(),m.withdraw()],bg='gray')
bx2.pack(padx='8.0',pady='5.0')
bx3=tk.Button(x,width=30,height=1,text="Wordlist Generator",font=('Arial',15,'bold'),command=getframewg,bg='green')
bx3.pack(padx='8.0',pady='5.0')


m=Toplevel(x)
m.geometry("750x350")
m.withdraw()
m.protocol("WM_DELETE_WINDOW",m.withdraw)

wgen=Toplevel(x)
wgen.withdraw()
wgen.protocol("WM_DELETE_WINDOW",wgen.withdraw)

sha1f=Toplevel(m)
sha512f=Toplevel(m)
sha256f=Toplevel(m)
md5f=Toplevel(m)
hg=Toplevel(x)
ab=Toplevel(x)
ins1=Toplevel(m)
ins2=Toplevel(hg)
ins3=Toplevel(wgen)

menub= tk.Menu(x)
help1=tk.Menu(menub,tearoff=0)
menub.add_cascade(label="Help",menu=help1)
help1.add_command(label="About",command=getab)

menuins1=tk.Menu(m)
helpins1=tk.Menu(menuins1,tearoff=0)
menuins1.add_cascade(label="Help",menu=helpins1)
helpins1.add_command(label="Instructions",command=getins1)

menuins2=tk.Menu(hg)
helpins2=tk.Menu(menuins2,tearoff=0)
menuins2.add_cascade(label="Help",menu=helpins2)
helpins2.add_command(label="Instructions",command=getins2)

menuins3=tk.Menu(wgen)
helpins3=tk.Menu(menuins3,tearoff=0)
menuins3.add_cascade(label="Help",menu=helpins3)
helpins3.add_command(label="Instructions",command=getins3)

inpw=Toplevel(x)
inpw.withdraw()
inpw.protocol("WM_DELETE_WINDOW",inpw.withdraw)

inpurl=Frame(inpw)
inpword=Frame(inpw)


ab.withdraw()
ab.protocol("WM_DELETE_WINDOW",ab.withdraw)
ins1.withdraw()
ins1.protocol("WM_DELETE_WINDOW",ins1.withdraw)
ins2.withdraw()
ins2.protocol("WM_DELETE_WINDOW",ins2.withdraw)
ins3.withdraw()
ins3.protocol("WM_DELETE_WINDOW",ins3.withdraw)
ins1.withdraw()
sha1f.withdraw()
sha1f.protocol("WM_DELETE_WINDOW",sha1f.withdraw)
sha256f.withdraw()
sha256f.protocol("WM_DELETE_WINDOW",sha256f.withdraw)
sha512f.withdraw()
sha512f.protocol("WM_DELETE_WINDOW",sha512f.withdraw)
md5f.withdraw()
md5f.protocol("WM_DELETE_WINDOW",md5f.withdraw)

ab.geometry("1000x500")
abl=tk.Label(ab,text="About Us",height=1,font=('Courier', 30,'bold'), relief=SUNKEN, anchor=CENTER,bg='black',fg='white')
abl.pack(padx=10,pady=10)
abl2=tk.Label(ab,text="\n\nThe Hashing Engine is a project developed by\n a team of students from MIT Manipal, India.\n\n\n The team consists of 3 members namely:",font=('Georgia',20,'italic'),bg='black',fg='white')
abl2.pack(fill='both')
abl3=tk.Label(ab,text="\n\nAdarsh Mehta (200953090)\n\nAnsh Aryan (200953070)\n\nRohan Arya (200953064)\n",font=('Georgia',20,'italic'),fg='red',bg='black')
abl3.pack(fill='both')
ab.config(bg='black')

ins1.geometry("1400x500")
ins1l=tk.Label(ins1,text="Instructions",height=1,font=('Courier', 30,'bold'), relief=SUNKEN, anchor=CENTER,bg='black',fg='white')
ins1l.pack(padx=10,pady=10)
ins1l2=tk.Label(ins1,text="\n\nThe Hash cracker has 4 options available with more on the way.\n\n You can crack hashes by simply clicking on the button for the hashing algo of your choice.\n\n Then paste the hash you want to crack in the text field and simply press the button named Crack\n\n Congratulations!! You have now cracked the password.\n\nIt also has a button called input wordlist where you can input a list of your choice for cracking.\n\n Simply choose the input method and paste the URL or location of the file and click the input button.",font=('Georgia',20,'italic'),bg='black',fg='white')
ins1l2.pack(fill='both')
ins1.config(bg='black')



ins3.geometry("1500x500")
ins3l=tk.Label(ins3,text="Instructions",height=1,font=('Courier', 30,'bold'), relief=SUNKEN, anchor=CENTER,bg='black',fg='white')
ins3l.pack(padx=10,pady=10)
ins3l2=tk.Label(ins3,text="\n\nThe Wordlist Generator has 4 fields available.\n\n You can input words of your choice to generate potential passwords including those words.\n\n Fill in words of your choice and press the button!! The wordlist will be stored in the same location as this program !!\n\n Congratulations!! You have created your own wordlist to crack passwords with specific information about the victim.\n\n",font=('Georgia',20,'italic'),bg='black',fg='white')
ins3l2.pack(fill='both')
ins3.config(bg='black')

ins2.geometry("1400x500")
ins2l=tk.Label(ins2,text="Instructions",height=1,font=('Courier', 30,'bold'), relief=SUNKEN, anchor=CENTER,bg='black',fg='white')
ins2l.pack(padx=10,pady=10)
ins2l2=tk.Label(ins2,text="\n\n\n\nThe Hash generator has 4 options available with more on the way.\n\n You can generate hashes by simply clicking on the button for the hashing algo of your choice.\n\n Then paste the password you want to hash in the text field and simply press the button named Generate\n\n Congratulations!! You have now cracked the password.\n",font=('Georgia',20,'italic'),bg='black',fg='white')
ins2l2.pack(fill='both')
ins2.config(bg='black')

hg.withdraw()
hg.protocol("WM_DELETE_WINDOW",hg.withdraw)
tt=tk.Text(hg,width=70,height=5)

wgenl=tk.Label(wgen,text="Wordlist Generator",height=1,font=('Courier', 20,'bold'), relief=SUNKEN, anchor=CENTER,fg='red',bg='black')
wgenl.pack(padx=8,pady=8)
wgenl2=tk.Label(wgen,text="Main Word:",font=('Courier', 12,'bold'),relief=SUNKEN)
wgenl2.pack(padx=8,pady=8)
wgentxt1=tk.Text(wgen,width=30,height=1)
wgentxt1.pack(padx=8,pady=8)
wgenl3=tk.Label(wgen,text="Word 2:",font=('Courier', 12,'bold'),relief=SUNKEN)
wgenl3.pack(padx=8,pady=8)
wgentxt3=tk.Text(wgen,width=30,height=1)
wgentxt3.pack(padx=8,pady=8)
wgenl4=tk.Label(wgen,text="Word 3:",font=('Courier', 12,'bold'),relief=SUNKEN)
wgenl4.pack(padx=8,pady=8)
wgentxt4=tk.Text(wgen,width=30,height=1)
wgentxt4.pack(padx=8,pady=8)
wgenl5=tk.Label(wgen,text="Word 4:",font=('Courier', 12,'bold'),relief=SUNKEN)
wgenl5.pack(padx=8,pady=8)
wgentxt5=tk.Text(wgen,width=30,height=1)
wgentxt5.pack(padx=8,pady=8)
wbut1=tk.Button(wgen,text="Generate",width=20,command=wordgen)
wbut1.pack(padx=8,pady=8)

inpwlab=tk.Label(inpw,text="Mode of Input?",font=("Courier",15,'bold'),relief=SUNKEN,anchor=CENTER,fg='white')
inpwlab.pack()
svar=StringVar()
options2=['URL','Upload']
svar.set('URL')

b7=tk.OptionMenu(inpw,svar,*options2)
b7.pack(padx=10,pady=10)
b8=tk.Button(inpw,text="Select",width=15,height=1,command=selectinp)
b8.pack(padx=5,pady=5)

txt6=tk.Text(inpurl,width=30,height=1)
txt6.pack()
b6=tk.Button(inpurl,text="Input",command=lambda: [inpu(),inpw.withdraw()])
b6.pack()

txt7=tk.Text(inpword,width=30,height=1)
txt7.pack()
b9=tk.Button(inpword,text="Input",command=lambda: [inpwo(),inpw.withdraw()])
b9.pack()

l= tk.Label(m, text='Hash Cracker 101',height=1,font=('Courier', 30,'bold'), relief=SUNKEN, anchor=CENTER,fg='green',bg='black')
l.pack(pady='8.0',fill='both')
lasha1=tk.Label(sha1f,text="Crack SHA-1 Hash",height=1,font=('Courier', 20,'bold'), relief=SUNKEN, anchor=CENTER,fg='red',bg='black')
lasha1.pack(padx=8,pady=8)
txt= tk.Text(sha1f,width=30,height=1)
txt.pack(padx=8,pady=8)
crackb1=tk.Button(sha1f,text="Crack",width=10,bg='green',command=inp,font=('Arial',12,'bold'))
crackb1.pack(padx=8,pady=8)

lasha256=tk.Label(sha256f,text="Crack SHA-256 Hash",font=('Courier', 20,'bold'), relief=SUNKEN, anchor=CENTER,fg='red',bg='black')
lasha256.pack(padx=8,pady=8)
txt2= tk.Text(sha256f,width=30,height=1)
txt2.pack(padx=8,pady=8)
crackb2=tk.Button(sha256f,text="Crack",width=10,command=inp,bg='green',font=('Arial',12,'bold'))
crackb2.pack(padx=8,pady=8)

lasha512=tk.Label(sha512f,text="Crack SHA-512 Hash",font=('Courier', 20,'bold'), relief=SUNKEN, anchor=CENTER,fg='red',bg='black')
lasha512.pack(padx=8.0,pady=8)
txt3= tk.Text(sha512f,width=30,height=1)
txt3.pack(padx=8,pady=8)
crackb3=tk.Button(sha512f,text="Crack",width=10,command=inp,bg='green',font=('Arial',12,'bold'))
crackb3.pack(padx=8,pady=8)


lamd5=tk.Label(md5f,text="Crack MD5 Hash",font=('Courier', 20,'bold'), relief=SUNKEN, anchor=CENTER,fg='red',bg='black')
lamd5.pack(padx=8,pady=8)
txt4=tk.Text(md5f,width=30,height=1)
txt4.pack(padx=8,pady=8)
crackb4=tk.Button(md5f,text="Crack",command=inp,bg='green',font=('Arial',12,'bold'))
crackb4.pack(padx=8,pady=8)


lagensha1=tk.Label(hg,text="Generate Hash",bg='black',fg='green',font=('Arial',15,'bold'))
lagensha1.pack(padx=8,pady=8,fill='both')
txt5=tk.Text(hg,width=30,height=1)
txt5.pack(padx=8,pady=8)
clicked=StringVar()
options=['SHA-1','SHA-256','SHA-512','MD5']
clicked.set('Select Hashing Algorithm')
men=tk.OptionMenu(hg,clicked,*options)
men.config(font=('Arial',10,'bold'))
men.pack()
bgens1=tk.Button(hg,text="Generate",command=lambda:[dele(),gen()],font=("Arial",12,'bold'),bg='green')
bgens1.pack(padx=8,pady=8)

button1= tk.Button(m,text='SHA-1',height=1,width=25,font=('Arial',12,'bold'),command=lambda: [getframe1(),s1()],bg='gray')
button1.pack(padx='8.0',pady='8.0')

button2= tk.Button(m,text='SHA-256',height=1,width=25,font=('Arial',12,'bold'),command=lambda: [getframe256(),s256()],bg='green')
button2.pack(padx='8.0',pady='8.0')

button3= tk.Button(m,text='SHA-512',height=1,width=25,font=('Arial',12,'bold'),command=lambda: [getframe512(),s512()],bg='gray')
button3.pack(padx='8.0',pady='8.0')

button4=tk.Button(m,text='MD5',height=1,width=25,font=('Arial',12,'bold'),command=lambda: [getframemd5(),smd5()],bg='green')
button4.pack(padx='8.0',pady='8.0')

buinp=tk.Button(m,text="Input Wordlist",command=getframeinpw,bg='black',fg='green',font=('Arial',12,'bold'))
buinp.pack(padx='8.0',pady='8.0')
disp=tk.Text
hg.config(menu=menuins2)
wgen.config(menu=menuins3)
m.config(menu=menuins1)
x.config(menu=menub)
m.mainloop()
x.mainloop()
