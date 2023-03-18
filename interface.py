
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.font import *
import re
from setuptools import Command
#--------------------------------------------------------------------------
root = Tk()
#--------------------------------------------------------------------------
root.title("compilation")
root.minsize(950,530)
root.configure(bg='#78BCC4')
root.iconbitmap(r'code.ico')
root.resizable(0,0)
#--------------------------------------------------------------------------
my_font = Font(family="MV Boli",size=12)
#----------------------------------------------------------------------------- 
label = Label(root, text='Saiser votre code ici :', fg='black',bg="#78BCC4",font=my_font)
label.place(x=60, y=40)
label1 = Label(root, text='Console :', fg='black',bg="#78BCC4",font=my_font)
label1.place(x=500, y=40)
#--------------------------------------------------------------------------
s_b = Scrollbar(root)
s_b.pack(side=RIGHT,fill=Y)
#--------------------------------------------------------------------------
inputtxt = Text(root, height = 18,width = 35 ,bg = "#F7F8F3",fg = "#002C3E",font = my_font)
inputtxt.place(x=60,y=70)
#--------------------------------------------------------------------------
Output = Text(root, height = 18,width = 35,bg = "#002C3E",fg="#FFFF00",font = my_font,yscrollcommand = s_b.set)
Output.place(x=500,y= 70)
#--------------------------------------------------------------------------
s_b.config(command=Output.yview)
#-------------------------------------------------------------------------
def num(x):
    if x >= '0' and x <= '9':
        return True
    return False
#--------------------------------------------------------------------------
def ltr(x):
    if x >= 'a' and x <= 'z':
        return True
    return False
#--------------------------------------------------------------------------
def clé(x):
    if  x >= 'A' and x <= 'Z':
        return True
    return False
#--------------------------------------------------------------------------
def sgn(x):
    if x == '-' or x == '+' :
        return True
    return False
#----------------------------------------------------------------------------- 
def opr(x):
    if sgn(x) or x == '*' or x == '/' or x=='<' or x=='>':
        return True
    return False
#--------------------------------------------------------------------------
def sep(x):
    if x == "(" or x == ")" or  x == "[" or x == "]" or x == "{" or x == "}" or x == ";" or x == ",": 
         return True
    return False  
#--------------------------------------------------------------------------
def test1(w2,i):
    if (num(w2[i]) and num(w2[i+1]))  or (ltr(w2[i]) 
        and ltr(w2[i + 1]) ) or ( ltr(w2[i]) and num(w2[i + 1])) or ( ltr(w2[i + 1]) 
        and num(w2[i]))or (w2[i] == '+' and w2[i+1] == '+') or (num(w2[i])  and w2[i + 1] == '.') or ( w2[i] == '.' and num(w2[i + 1]))or(opr(w2[i-1])
        and w2[i] == "." and num(w2[i+1]))or(ltr(w2[i])and w2[i+1]== "_" and ltr(w2[i+2]) ):
        return True
    return False
#--------------------------------------------------------------------------  
def test2(w2,i):
    if (opr(w2[i-1]) and opr(w2[i]) and num(w2[i + 1])) or (w2[i-1]=="=" and opr(w2[i]) and num(w2[i+1]))or(sep(w2[i-1]) 
    and opr(w2[i]) and num(w2[i+1]))or(opr(w2[i-1]) and opr(w2[i]) and w2[i+1]=='.')or(w2[i]=='.' and num(w2[i-1]) ) or(w2[i]=="&" and w2[i+1]=="&") or(w2[i]=="|" 
        and w2[i+1]=="|")  or (num(w2[i]) and w2[i+1]=='.') or (opr(w2[i]) and num(w2[i + 1])) :
        return True
    return False
#--------------------------------------------------------------------------
def TC(tc):
    if    num(tc):                          return 1
    elif  ltr(tc):                          return 2
    elif  sep(tc):                          return 3
    elif  tc=='+':                          return 4
    elif  tc=='-':                          return 5
    elif  tc=='<':                          return 6
    elif  tc=='>':                          return 7
    elif  tc=='=':                          return 8
    elif  tc=='.' :                         return 9
    elif  tc==':':                          return 10
    elif  tc=='|' :                         return 11
    elif  tc=='&':                          return 12
    elif  tc=='_':                          return 13
    elif  tc=='*'or tc == '/':              return 14
    elif  clé(tc):                          return 15
    else:                                   return -1
#----------------------------------------------------------------------------- 
def EC(ec,z):
    k=''
    if    ec==2 :   k=k+" "+z+" :est un Identificateur \n"
    elif  ec==6 :   k=k+" "+z+" :est un number entier\n"
    elif  ec==8 :   k=k+" "+z+" :est un number reel \n"
    elif  ec==10 :  k=k+" "+z+" :est un OR \n"
    elif  ec==11 :  k=k+" "+z+" :est un operateur\n"
    elif  ec==13 :  k=k+" "+z+" :est un pas positif \n"
    elif  ec==12 :  k=k+" "+z+" :est un number entier signe positif \n"
    elif  ec==15 :  k=k+" "+z+" :est un number reel signe positif \n"
    elif  ec==16 :  k=k+" "+z+" :est un operateur \n"
    elif  ec==17 :  k=k+" "+z+" :est un number entier signe négatif \n"
    elif  ec==19 :  k=k+" "+z+" :est un number reel signe négatif  \n"
    elif  ec==20 :  k=k+" "+z+" :est un pas négatif \n"
    elif  ec==21 :  k=k+" "+z+" :est un operateur \n"
    elif  ec==22 :  k=k+" "+z+" :est un operateur \n"
    elif  ec==23 :  k=k+" "+z+" :est un operateur \n"
    elif  ec==24 :  k=k+" "+z+" :est un operateur \n"
    elif  ec==26 :  k=k+" "+z+" :est un AND \n"
    elif  ec==27 :  k=k+" "+z+" :est un séparateur \n"
    elif  ec==28 :  k=k+" "+z+" :est un operateur \n"
    elif  ec==29 :  k=k+" "+z+" :est un séparateur\n"
    elif  ec==30 :  k=k+" "+z+" :est un operateur\n"
    elif  ec==31 :  k=k+" "+z+" :est un operateur\n"
    elif  ec==32 :  k=k+" "+z+" :est un mot clé\n"
    else:           k=k+" "+z+" :est un error \n"
    Output.config(state='normal')
    Output.insert(END, k)
    Output.config(state='disabled')
#----------------------------------------------------------------------------- 
def text1(event=""):
    Output.config(state='normal')
    Output.delete(1.0,END)
    String = inputtxt.get("1.0",END)
    r=String.replace("\n"," ")     
    i=0
    while i <= len(r):
        r=r.replace("  "," ")
        i+=1
    j=0
    w2=r
    long = len(w2)
    y=""
    if len(w2)>= 1:
        w2 = w2 +  "#"
    for i in range(0, long):
            if test1(w2,i):    
                y +=  w2[i]  
            elif test2(w2,i):         
                y +="#" + w2[i]
              
            else :
                y += w2[i] + "#"
    y = re.sub("\# #|\##","#",y)
    w2=y
    w=""
    while j <= len(w2)-1:
        if(w2[j] != "$"):
            w+=w2[j]
        elif(w2[j] == "$"):
            j +=1
            w+=""
            while w2[j] != "$":
                if j<len (w2)-1:
                    w=w.replace("  "," ")
                    j +=1 
                else: 
                     w=w.replace("##","#")
                     w=w.replace(":#=",":=")
                     Output.insert(END,w)
                     return w             
        j+=1
#--------------------------------------------------------------------------
    w=w.replace("##","#")
    w=w.replace(":#=",":=")
    w=w.replace("=#=","==")
    w=w.replace("<#=","<=")
    w=w.replace(">#=",">=")
    w=w.replace("-#.","-.")
    w=w.replace("+#.","+.")
    w=w.replace("+++","++#+")
    w=w.replace("---","--#-")
    w=w.replace("# #","#")
    w=w.replace("_#_","_")
    w=w.replace("#_#","_")
    w=w.replace("__","_")
    w=w.replace("_#","_")
#-----------------------------------------------------------------------------    
    w=w.replace("F#O#R","FOR")
    w=w.replace("E#L#S#E","ELSE")
    w=w.replace("E#L#I#F","ELIF")
    w=w.replace("I#F","IF")
    w=w.replace("W#H#I#L#E","WHILE")
    w=w.replace("D#O","DO")
    w=w.replace("T#R#Y","TRY")
    w=w.replace("E#X#C#E#P#T","EXCEPT")
    w=w.replace("R#E#T#U#R#N","RETURN")
    w=w.replace("B#R#E#A#K","BREAK")
#-----------------------------------------------------------------------------
    w=w.replace(" ","")
    Output.insert(END, w)
    return w
root.bind('<Control-l>',text1)
#-----------------------------------------------------------------------------
def lexical():
    Output.config(state='normal')
    Output.delete("1.0", "end")
    y=text1()
    return y
#----------------------------------------------------------------------------- 
def lexi4():
    Output.config(state='normal')
    mm=lexical()
    Output.insert(END, mm)
    Output.config(state='disabled')
#-----------------------------------------------------------------------------    
def Syntaxique(event=""): 
    t=[
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,6, 2, 29,11,16,21,23,30,29,27,9,25,-1,28,32],
        [-1,2, 2, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1],
        [-1,2,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,-1,-1],
        [-1,2,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,5,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,-1,-1],
        [-1,6,-1,-1,-1,-1,-1,-1,-1,7,-1,-1,-1,5,-1,-1],
        [-1,8,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,8,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,5,-1,-1],
        [-1,12,-1,-1,13,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,12,-1,-1,-1,-1,-1,-1,-1,14,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,17,-1,-1,-1,20,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,17,-1,-1,-1,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1],
        [-1,19,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,19,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,22,22,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,24,-1,24,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,26,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,28,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,32]
    ]
    mm=lexical()
    Output.delete("1.0", "end")
    i=0
    k =''
    ec=1
    while i < len(mm):
        tc=mm[i]
        if tc!='#' :
            k=k+mm[i]
            if ec!=-1 and TC(tc)!=-1:
                 ec=t[ec][TC(tc)]
            else: ec=-1
        else :
            EC(ec,k)
            k = ''
            ec=1
        i=i+1
root.bind('<Control-m>',Syntaxique)
#--------------------------------------------------------------------------
def open_file(event=""):
    text_file = filedialog.askopenfile(filetypes = (("Text files", ".txt"), ("All files", "*.*"))).name
    text_file = open(text_file,'r')              
    content = text_file.read()
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, content)
    print (text_file)
root.bind('<Control-o>',open_file)    
#---------------------------------------------------------------------------------------------------------------------------------------   
def saveFile(event=""):
    file = filedialog.asksaveasfile(initialdir="/",defaultextension='.txt',filetypes=[("Text file",".txt"),("All files", "*.*")])
    if file is None:
        return
    filetext = str(inputtxt.get(1.0,END))
    file.write(filetext)
    file.close()
root.bind('<Control-s>',saveFile)     
#-----------------------------------------------------------------------------------------------------------------------------------
def New_file(event=""):
     inputtxt.delete('1.0', END)
     Output.config(state='normal')
     Output.delete('1.0', END)
root.bind('<Control-n>',New_file)     
#--------------------------------------------------------------------------------------------------------------------------------------------    
def Exit(event=""):
     result = messagebox.askquestion("Exit", "Are You Sure You Want to Exit?")
     if result == "yes":
        root.destroy()
     else:
        return None
root.bind('<Control-e>',Exit)    
#-------------------------------------------------------------------------------------------------------------------------------------------- 
def Test(event=""):
    r = "a:=-b+-x;\na99=.33=+5;\na1:=-.33*-66;\na1;-3.3;+66:=+6++.3;\n3.;IF.;i++++3.3;\nmmmmm3\nm.\n9."
    inputtxt.delete("1.0", "end")
    inputtxt.insert(END, r)
root.bind('<Control-t>',Test)     
#--------------------------------------------------------------------------------------------------------------------------------------------
newImage=PhotoImage(file="new.png")
openImage = PhotoImage(file="open.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")
configImage = PhotoImage(file="config.png")
#-------------------------------------------------------------------------------------------------------------------------------------------- 
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0,font=("MV Boli",11),background = "#F7F8F3")
filemenu.add_command(label="New",image=newImage, command=New_file,compound="left")
filemenu.add_command(label="Open",image=openImage, command=open_file,compound="left")
filemenu.add_command(label="Save As ..",image=saveImage, command=saveFile,compound="left")
#--------------------------------------------------------------------------
filemenu.add_separator() 
#--------------------------------------------------------------------------
filemenu.add_command(label="Exit",image=exitImage, command=Exit,compound="left")
#--------------------------------------------------------------------------
analysemenu = Menu(menubar, tearoff=0,font=("MV Boli",11),background = "#F7F8F3")
analysemenu.add_command(label="Lexical",image=configImage,command= lexical,compound="left")
analysemenu.add_command(label="Syntaxique",image=configImage,command= Syntaxique,compound="left")
analysemenu.add_command(label="Semontique",image=configImage,compound="left")
#--------------------------------------------------------------------------
test = Menu(menubar,tearoff=0, font=("MV Boli",11),background = "#F7F8F3")
test.add_command(label="Test",image=configImage, command=Test,compound="left")
#-------------------------------------------------------------------------------
menubar.add_cascade(label="File", menu= filemenu)
menubar.add_cascade(label="Analyse", menu= analysemenu)
menubar.add_cascade(label="Test", menu= test)
#--------------------------------------------------------------------------
root.config(menu=menubar)
#--------------------------------------------------------------------------
root.mainloop()