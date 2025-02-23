from tkinter import *
def fl(a,b):
 s1=list(a)
 s2=list(b)
 l3=list(a)
 l4=list(b)
 while ' ' in s1:
    s1.remove(' ')
 while ' ' in s2:
    s2.remove(' ')
 while ' ' in l3:
    l3.remove(' ')
 while ' ' in l4:
    l4.remove(' ')
 for i in s1:
    if i in s2:
        s2.remove(i)
 for i in l4:
    if i in l3:
        l3.remove(i)
 size1=len(l3)
 size2=len(s2) 
 sum=size1+size2
 lis=['Friends',' In Love','Affection','Get Marriage','Enemies','Sibblings']
 n=6
 m=lis*100
 if sum!=0:
  while n != 1:
     del m[0:sum-1]
     lis.remove(m[0])
     print()
     g=m[0]
     while ( g in m) :
         m.remove(g)
     n=len(lis)
 rr=" {} and {} has a relation of ---------  {}   ".format(a,b,lis[0])
 x.config(text=rr)
 x.pack()
def flame():
 a=en1.get()
 b=en2.get()
 fl(a,b)
t=Tk()
na=StringVar()
pa=StringVar()
t.geometry("300x300")
t.title("my flames code")
en1=Entry(t,textvariable =na)
en1.pack()
en2=Entry(t,textvariable =pa)
en2.pack()
#na.set("enter the name 1:")
#pa.set("enter the name 2:")
x=Label(t,text='',bg="#FFB6C1")
Button(t,text="get result",command=flame,bg="#ADD8E6").pack()
t.mainloop(60)
