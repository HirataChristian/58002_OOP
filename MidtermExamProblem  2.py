from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl0 = Label(win, text="My Full Name", fg="red", font=("arial",20))
        self.lbl0.place(x=200, y=10)
        self.lbl1 = Label(win, text="Enter Given Name:", fg="red")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text="Enter Middle Name:", fg="red")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text="Enter Last Name:", fg="red")
        self.lbl3.place(x=100, y=150)
        self.lbl4 = Label(win, text="My Full Name is:", fg="red")
        self.lbl4.place(x=100, y=225)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=325, y=50)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=325, y=100)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=325, y=150)
        self.txt4 = Entry(win, bd=3, fg="red", bg="white")
        self.txt4.place(x=325, y=225)
        self.btn_show = Button(win, text="Show Full Name", command=self.show)
        self.btn_show.place(x=230, y=260)
        self.btn_clear = Button(win, text="Clear All", command=self.clear)
        self.btn_clear.place(x=230, y=300)

    def show(self):
        self.txt4.delete(0, 'end')
        first = str(self.txt1.get())
        middle = str(self.txt2.get())
        last = str(self.txt3.get())
        full_name = first + ' ' + middle + ' ' + last
        self.txt4.insert(END, str(full_name))
        self.txt4.config(fg="red")

    def clear(self):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("My Full Name")
window.mainloop()
