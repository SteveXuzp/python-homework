#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from utilshw1 import *
class Comment:
    name=name
    time=time
    course=course
    contents=contents #all the data
    
    def showall(self,txt):
        txt.delete(0.0,END)
        for i in range(0,len(name)):
            s=self.name[i]+"  "+self.time[i]+"  "+self.course[i]+"\n"+self.contents[i]+"\n"+"\n"
            txt.insert(END,s)
            
    def latest(self,txt):
        txt.delete(0.0,END)
        s=self.name[0]+"  "+self.time[0]+"  "+self.course[0]+"\n"+self.contents[0]
        txt.insert(END,s)
        
    def allcourses(self,txt):
        txt.delete(0.0,END)
        new_courses=list(set(self.course))
        for i in range(0,len(new_courses)):
            s=new_courses[i]+"\n"
            txt.insert(END,s)
            
    def visual_interface(self):
        root = Tk()
        root.geometry('960x480')
        root.title('USTC course comments')
        
        txt = Text(root)
        txt.place(rely=0.5, relwidth=1.0 ,relheight=0.5)

        lb1 = Label(root, text='This can show comments on USTC icourse club, click the bottom to show the result.',
                    font=("Times New Roman",16,"bold"))
        lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        btn1 = Button(root, text='show all the comments', command=lambda:self.showall(txt))
        btn1.place(relx=0.05, rely=0.3, relwidth=0.25, relheight=0.1)
        
        btn2 = Button(root, text='show the latest comment', command=lambda:self.latest(txt))
        btn2.place(relx=0.375, rely=0.3, relwidth=0.25, relheight=0.1)
        
        btn1 = Button(root, text='show all the courses that are evaluated ', command=lambda:self.allcourses(txt))
        btn1.place(relx=0.7, rely=0.3, relwidth=0.25, relheight=0.1)

        root.mainloop()
        


            
            







