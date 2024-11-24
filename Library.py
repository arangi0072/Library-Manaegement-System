from tkinter import *
from tkcalendar import *
import tkinter.messagebox as tmg
import random
import time
from cryptography.fernet import Fernet


# with open("ke.bin.key", "rb") as k:
key = b'Zibp3y81EZ7fWmO6xfcCGVFi8SK5h-PG1j5LvZDCtzs='
fernet = Fernet(key)
with open("pas.bin", "rb") as p:
    passwor = p.read()
password = fernet.decrypt(passwor).decode()
with open("books.bin", "a") as boo:
    boo.write("")
# with open("books.bin", "wb") as cv:
    # df = fernet.encrypt('''{'Computer':['computer','Arpit',3],'Physics':['Physics','HC Verma',5]}/{5678904657:['computer','Arpit',3],8734938193:['Physics','HC Verma',5]}/{24724783920:['Arpit'],47820483948:['Rangi']}'''.encode())
    # cv.write(df)


def scroll(x, y):
    l.yview(x, y)
    l1.yview(x, y)
    l2.yview(x, y)


def login1():
    global new2
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[1]
    books_name_dic = data[0]
    member_dic = data[2]

    new2 = Tk()
    new2.attributes('-fullscreen', True)
    new2.config(bg='ghostwhite')
    Label(new2, text="Library Management System",
          font="comicsans 40", bg="ghostwhite").pack(side=TOP)
    f = Frame(new2, bg="ghostwhite")
    f1 = Frame(new2, bg="ghostwhite")
    f2 = Frame(new2, bg="ghostwhite")
    f.pack(side=BOTTOM, pady=10)
    f2.pack(side="left")
    f1.pack(pady=170)
    Scroll_bar = Scrollbar(f2)
    # Scroll_bar1 = Scrollbar(f2)
    # Scroll_bar2 = Scrollbar(f2)
    global l
    global l1
    global l2
    Label(f2, text="Book Name \t Author \t\t Quantity",
          bg="ghostwhite", font="comicsans 20").pack()
    l = Listbox(f2, height="25", font="comicssans 15",
                yscrollcommand=Scroll_bar.set)
    l1 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l2 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l.pack(side="left")
    l1.pack(side="left")
    # Scroll_bar1.pack(side=LEFT, fill=Y)
    # Scroll_bar1.config(command=l.yview)
    l2.pack(side="left")
    # Scroll_bar2.pack(side=LEFT, fill=Y)
    # Scroll_bar2.config(command=l.yview)
    Scroll_bar.pack(side=LEFT, fill=Y)
    Scroll_bar.config(command=scroll)
    l3 = dic.values()
    bo = dic.keys()
    t_boo = len(bo)
    value = 1
    for i in l3:
        l.insert(END, f"{value}. {i[0]}")
        l1.insert(END, f"{value}. {i[1]}")
        l2.insert(END, f"{value}. {i[3]}")
        value += 1
        if value == 10:
            break
    # Frame(f1, height=50, width=400).pack()
    Label(f1, text=f"Total No. of Unique Books : {t_boo}",
          bg="ghostwhite", font="comicsans 20").pack(side="top")
    Label(f1, text=f"Total No. of All Books : {data[5]}",
          bg="ghostwhite", font="comicsans 20").pack(side="top")
    Label(f1, text=f"Total No. of Members : {len(member_dic.keys())}",
          bg="ghostwhite", font="comicsans 20").pack(side="top")
    Label(f1, text=f"Total No. of Avaliable Books in Library Now : {data[6]}", bg="ghostwhite", font="comicsans 20").pack(
        side="top")
    f7 = Frame(f1, bg="ghostwhite")
    f7.pack(side=BOTTOM, padx=10, pady=10)
    f5 = Frame(f1, bg="ghostwhite")
    f5.pack(side=LEFT, padx=10, pady=10)
    f6 = Frame(f1, bg="ghostwhite")
    f6.pack(side=RIGHT, pady=10, padx=10)
    Button(f, text="Manage Books", bg="white",
           font="comicsans 20", command=manage_books).pack(side=LEFT, padx=4)
    Button(f, text="Manage Members", bg="white",
           font="comicsans 20", command=Manage_members).pack(side=LEFT, padx=4)
    Button(f, text="List of Books/Members", bg="white",
           font="comicsans 20", command=lsi_bo_mem).pack(side=LEFT, padx=4)
    Button(f, text="Entry/Exit", bg="white",
           font="comicsans 20", command=entry_exit).pack(side=LEFT, padx=4)
    Button(f, text="Record", bg="white",
           font="comicsans 20", command=entry_record1).pack(side=LEFT, padx=4)
    Button(f, text="Find A Book", bg="white",
           font="comicsans 20", command=find_book).pack(side=LEFT, padx=4)
    Button(f, text="Exit", bg="white",
           font="comicsans 20", command=back3).pack(side=LEFT, padx=4)
    Button(f5, text="Find Member", bg="white",
           font="comicsans 20", command=find_mem).pack(padx=4, pady=3)
    Button(f5, text="Issue A Book", bg="white",
           font="comicsans 20", command=issue_book).pack(padx=4, pady=3)
    Button(f6, text="Update info", bg="white",
           font="comicsans 20", command=update_info).pack(padx=4, pady=3)
    Button(f6, text="Update Expiry Date", bg="white",
           font="comicsans 20", command=update_expire1).pack(padx=4, pady=3)
    Button(f7, text="Retrive Book", bg="white",
           font="comicsans 20", command=retrive_book1).pack(padx=4, pady=3)
    new2.bind('<Escape>',lambda x:new2.destroy())
    new2.mainloop()


def retrive_book1():
    new2.destroy()
    retrive_book()


def retrive_book():
    global new18
    new18 = Tk()
    new18.attributes('-fullscreen', True)
    new18.config(bg="ghostwhite")
    f = Frame(new18, bg="ghostwhite")
    f.place(in_=new18, anchor="c", rely=.5, relx=.5)
    f1 = Frame(f, bg="ghostwhite")
    f2 = Frame(f, bg="ghostwhite")
    f3 = Frame(f, bg="ghostwhite")
    f3.pack(side=BOTTOM)
    f2.pack(side=LEFT)
    f1.pack(side=RIGHT)
    Label(f2, text="Member's ID/Phone No. : ",
          font="comicsans 20", bg="ghostwhite").pack()
    Label(f2, text="Book's ID/Name : ",
          font="comicsans 20", bg="ghostwhite").pack()
    Label(f2, text="Quantity : ", font="comicsans 20", bg="ghostwhite").pack()
    global mem_id
    mem_id = StringVar()
    global book_id3
    book_id3 = StringVar()
    global quantity
    quantity = IntVar()
    Entry(f1, textvariable=mem_id, font="comicsasn 20").pack()
    Entry(f1, textvariable=book_id3, font="comicsasn 20").pack()
    Entry(f1, textvariable=quantity, font="comicsasn 20").pack()
    Button(f3, text="Retrive Book", font="comicsans 20",
           bg="ghostwhite", command=retrive).pack()
    Button(f3, text="Back", font="comicsans 20",
           bg="ghostwhite", command=back18).pack()
    new18.bind('<Escape>',lambda event:back18())
    
    new18.mainloop()


def retrive():
    with open("books.bin", "rb") as fg:
        dat = fg.read()
    dat1 = fernet.decrypt(dat).decode()
    data = eval(dat1)
    mem = data[2]
    book = data[0]
    book_id1 = data[1]
    mem_ph = data[4]
    mem_issue = data[8]
    stock = data[6]
    book_iss = data[7]
    # try:
    if int(mem_id.get()) in mem.keys():
        if book_id3.get().capitalize() in book.keys():
            if int(mem_id.get()) in mem_issue.keys():
                bookt = book[book_id3.get().capitalize()]
                if bookt in mem_issue[int(mem_id.get())].keys():
                    val = mem_issue[int(mem_id.get())][bookt]
                    if quantity.get() > val[2]:
                        tmg.showerror(
                            "Book", f"Only {val[2]} Books are issued to Member.")
                    elif quantity.get() == val[2]:
                        del mem_issue[int(mem_id.get())][bookt]
                        del book_iss[bookt][int(mem_id.get())]
                        val23 = book_id1[bookt]
                        # tmg.showinfo("", val23)
                        # print(val23)
                        data[6] = stock + quantity.get()
                        book_id1[bookt] = [val23[0], val23[1],
                                           val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        # with open("books.bin", "rb") as fg:
                        #     dat = fg.read()
                        #     dat1 = fernet.decrypt(dat).decode()
                        # data = eval(dat1)
                        # tmg.showinfo("", data)
                        tmg.showinfo("Retrive", "Book is retrived.")
                    elif quantity.get() < val[2]:
                        val12 = mem_issue[int(mem_id.get())][bookt]
                        val21 = book_iss[bookt][int(mem_id.get())]
                        book_iss[bookt][int(mem_id.get())] = [
                            val21[0], val21[1], val21[2] - quantity.get()]
                        mem_issue[int(mem_id.get())][bookt] = [
                            val12[0], val12[1], val12[2] - quantity.get()]
                        val23 = book_id1[bookt]
                        data[6] = stock + quantity.get()
                        book_id1[bookt] = [val23[0], val23[1],
                                           val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        tmg.showinfo("Retrive", "Book is retrived.")
                else:
                    tmg.showerror(
                        "Book", "No such book is issed to this Member.")
            else:
                tmg.showerror("Member", "No book is issued to this Member.")
        elif int(book_id3.get()) in book_id1.keys():
            if int(mem_id.get()) in mem_issue.keys():
                if int(book_id3.get()) in mem_issue[int(mem_id.get())].keys():
                    val = mem_issue[int(mem_id.get())][int(book_id3.get())]
                    if quantity.get() > val[2]:
                        tmg.showerror(
                            "Book", f"Only {val[2]} Books are issued to Member.")
                    elif quantity.get() == val[2]:
                        del mem_issue[int(mem_id.get())][int(book_id3.get())]
                        del book_iss[int(book_id3.get())][int(mem_id.get())]
                        val23 = book_id1[int(book_id3.get())]
                        data[6] = stock + quantity.get()
                        book_id1[int(book_id3.get())] = [
                            val23[0], val23[1], val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        tmg.showinfo("Retrive", "Book is retrived.")
                    elif quantity.get() < val[2]:
                        val12 = mem_issue[int(
                            mem_id.get())][int(book_id3.get())]
                        val21 = book_iss[int(book_id3.get())
                                         ][int(mem_id.get())]
                        book_iss[int(book_id3.get())][int(mem_id.get())] = [
                            val21[0], val21[1], val21[2] - quantity.get()]
                        mem_issue[int(mem_id.get())][int(book_id3.get())] = [
                            val12[0], val12[1], val12[2] - quantity.get()]
                        val23 = book_id1[int(book_id3.get())]
                        data[6] = stock + quantity.get()
                        book_id1[int(book_id3.get())] = [
                            val23[0], val23[1], val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        tmg.showinfo("Retrive", "Book is retrived.")
                else:
                    tmg.showerror(
                        "Book", "No such book is issed to this Member.")
            else:
                tmg.showerror("Member", "No book is issued to this Member.")
        else:
            tmg.showerror(
                "Book", "No such book present in Library's Database.")
    elif int(mem_id.get()) in mem_ph.keys():
        if book_id3.get().capitalize() in book.keys():
            memt = mem_ph[int(mem_id.get())]
            if memt in mem_issue.keys():
                bookt = book[book_id3.get().capitalize()]
                if bookt in mem_issue[memt].keys():
                    val = mem_issue[memt][bookt]
                    if quantity.get() > val[2]:
                        tmg.showerror(
                            "Book", f"Only {val[2]} Books are issued to Member.")
                    elif quantity.get() == val[2]:
                        del mem_issue[memt][bookt]
                        del book_iss[bookt][memt]
                        val23 = book_id1[bookt]
                        data[6] = stock + quantity.get()
                        book_id1[bookt] = [val23[0], val23[1],
                                           val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        tmg.showinfo("Retrive", "Book is retrived.")
                    elif quantity.get() < val[2]:
                        val12 = mem_issue[memt][bookt]
                        val21 = book_iss[bookt][memt]
                        book_iss[bookt][memt] = [
                            val21[0], val21[1], val21[2] - quantity.get()]
                        mem_issue[memt][bookt] = [
                            val12[0], val12[1], val12[2] - quantity.get()]
                        val23 = book_id1[bookt]
                        data[6] = stock + quantity.get()
                        book_id1[bookt] = [val23[0], val23[1],
                                           val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        tmg.showinfo("Retrive", "Book is retrived.")
                else:
                    tmg.showerror(
                        "Book", "No such book is issed to this Member.")
            else:
                tmg.showerror("Member", "No book is issued to this Member.")
        elif int(book_id3.get()) in book_id1.keys():
            memt = mem_ph[int(mem_id.get())]
            if memt in mem_issue.keys():
                bookt = int(book_id3.get())
                if bookt in mem_issue[memt].keys():
                    val = mem_issue[memt][bookt]
                    if quantity.get() > val[2]:
                        tmg.showerror(
                            "Book", f"Only {val[2]} Books are issued to Member.")
                    elif quantity.get() == val[2]:
                        del mem_issue[memt][bookt]
                        del book_iss[bookt][memt]
                        val23 = book_id1[bookt]
                        data[6] = stock + quantity.get()
                        book_id1[bookt] = [val23[0], val23[1],
                                           val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        tmg.showinfo("Retrive", "Book is retrived.")
                    elif quantity.get() < val[2]:
                        val12 = mem_issue[memt][bookt]
                        val21 = book_iss[bookt][memt]
                        book_iss[bookt][memt] = [
                            val21[0], val21[1], val21[2] - quantity.get()]
                        mem_issue[memt][bookt] = [
                            val12[0], val12[1], val12[2] - quantity.get()]
                        val23 = book_id1[bookt]
                        data[6] = stock + quantity.get()
                        book_id1[bookt] = [val23[0], val23[1],
                                           val23[2], val23[3]+quantity.get()]
                        with open("books.bin", "wb") as cvb:
                            ndata = fernet.encrypt(f"{data}".encode())
                            cvb.write(ndata)
                        tmg.showinfo("Retrive", "Book is retrived.")
                else:
                    tmg.showerror(
                        "Book", "No such book is issed to this Member.")
            else:
                tmg.showerror("Member", "No book is issued to this Member.")
        else:
            tmg.showerror(
                "Book", "No such book present in Library's Database.")
    else:
        tmg.showerror(
            "Member", "No such member present in Library's Database.")
    # except:
        # tmg.showerror("Retrive", "Please enter correct information.")


def back18():
    new18.destroy()
    login1()


def update_expire1():
    new2.destroy()
    update_expire()


def update_expire():
    global new16
    new16 = Tk()
    new16.attributes('-fullscreen', True)
    new16.config(bg="ghostwhite")
    f = Frame(new16, bg="ghostwhite")
    f.place(in_=new16, anchor="c", relx=.5, rely=.5)
    f1 = Frame(f, bg="ghostwhite")
    f2 = Frame(f, bg="ghostwhite")
    f3 = Frame(f, bg="ghostwhite")
    f3.pack(side=BOTTOM)
    f1.pack(side=LEFT)
    f2.pack(side=RIGHT)
    Label(f1, text="Member's ID/Phone No. : ",
          font="comicsans 20", bg="ghostwhite").pack()
    global mem_id
    mem_id = StringVar()
    Entry(f2, textvariable=mem_id, font="comicsans 20").pack()
    Button(f3, text='Find', font='comicsans 20',
           bg="ghostwhite", command=find_me).pack()
    new16.bind('<Return>',lambda event:find_me())
    
    Button(f3, text='Back', font='comicsans 20',
           bg="ghostwhite", command=back16).pack()
    new16.bind('<Escape>',lambda event:back16())
    
    new16.mainloop()


def find_me():
    try:
        with open('books.bin', 'rb') as df:
            dat2 = df.read()
            dat1 = fernet.decrypt(dat2).decode()
        data = eval(dat1)
        mem = data[2]
        mem_ph = data[4]
        if int(mem_id.get()) in mem.keys():
            new16.destroy()
            global new17
            new17 = Tk()
            val = mem[int(mem_id.get())]
            new17.attributes('-fullscreen', True)
            new17.config(bg="ghostwhite")
            f = Frame(new17, bg="ghostwhite")
            f.place(in_=new17, anchor="c", relx=.5, rely=.5)
            f4 = Frame(f, bg="ghostwhite")
            f1 = Frame(f, bg="ghostwhite")
            f2 = Frame(f, bg="ghostwhite")
            f3 = Frame(f, bg="ghostwhite")
            f4.pack(side=TOP)
            f1.pack(side=BOTTOM)
            f2.pack(side=LEFT)
            f3.pack(side=RIGHT)
            Label(f4, text=f"Member's id : {mem_id.get()}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Name : {val[1]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Expiry Date : {val[4]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f2, text=f"New Member's Expiry Date : ",
                  font="comicsans 20", bg="ghostwhite").pack()
            global mem_ex
            mem_ex = DateEntry(f3, dateformat=3, width=12, background='ghostwhite', font="comicsans 18",
                               foreground='black', borderwidth=4)
            mem_ex.pack()
            Button(f1, text="Update", font="comicsans 20",
                   bg="ghostwhite", command=update2).pack()
            Button(f1, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back173).pack()
            new17.bind('<Escape>',lambda event:back173())
            
            new17.mainloop()
        elif int(mem_id.get()) in mem_ph.keys():
            new16.destroy()
            global new171
            new171 = Tk()
            t = mem_ph[int(mem_id.get())]
            val = mem[t]
            new171.attributes('-fullscreen', True)
            new171.config(bg="ghostwhite")
            f = Frame(new171, bg="ghostwhite")
            f.place(in_=new171, anchor="c", relx=.5, rely=.5)
            f4 = Frame(f, bg="ghostwhite")
            f1 = Frame(f, bg="ghostwhite")
            f2 = Frame(f, bg="ghostwhite")
            f3 = Frame(f, bg="ghostwhite")
            f4.pack(side=TOP)
            f1.pack(side=BOTTOM)
            f2.pack(side=LEFT)
            f3.pack(side=RIGHT)
            Label(f4, text=f"Member's id : {t}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Name : {val[1]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Expiry Date : {val[4]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f2, text=f"New Member's Expiry Date : ",
                  font="comicsans 20", bg="ghostwhite").pack()
            global mem_ex1
            mem_ex1 = DateEntry(f3, dateformat=3, width=12, background='ghostwhite', font="comicsans 18",
                                foreground='black', borderwidth=4)
            mem_ex1.pack()
            Button(f1, text="Update", font="comicsans 20",
                   bg="ghostwhite", command=update21).pack()
            Button(f1, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back172).pack()
            new171.bind('<Escape>',lambda event:back172())
            
            new171.mainloop()
        else:
            tmg.showerror(
                "Member", f"NO such Member present in Library's Database with Id = {mem_id.get()}")
    except:
        tmg.showerror("Member", "Please enter the correct information.")


def back173():
    new17.destroy()
    update_expire()


def back172():
    new171.destroy()
    update_expire()


def update21():
    with open("books.bin", "rb") as dvb:
        dat = dvb.read()
    dat1 = fernet.decrypt(dat).decode()
    data = eval(dat1)
    mem = data[2]
    mem_ph = data[4]
    t = mem_ph[int(mem.get())]
    val = mem[t]
    mem[t] = [val[0], val[1], val[2], val[3], mem_ex.get()]
    with open("books.bin", "wb") as cvb:
        ndata = fernet.encrypt(f"{data}".encode())
        cvb.write(ndata)
    tmg.showinfo("Member", "Expiry Date is Updated.")


def update2():
    with open("books.bin", "rb") as dvb:
        dat = dvb.read()
    dat1 = fernet.decrypt(dat).decode()
    data = eval(dat1)
    mem = data[2]
    val = mem[int(mem_id.get())]
    mem[int(mem_id.get())] = [val[0], val[1], val[2], val[3], mem_ex.get()]
    with open("books.bin", "wb") as cvb:
        ndata = fernet.encrypt(f"{data}".encode())
        cvb.write(ndata)
    tmg.showinfo("Member", "Expiry Date is Updated.")


def update_info():
    new2.destroy()
    update_info1()


def update_info1():
    global new16
    new16 = Tk()
    new16.attributes('-fullscreen', True)
    new16.config(bg="ghostwhite")
    f = Frame(new16, bg="ghostwhite")
    f.place(in_=new16, anchor="c", relx=.5, rely=.5)
    f1 = Frame(f, bg="ghostwhite")
    f2 = Frame(f, bg="ghostwhite")
    f3 = Frame(f, bg="ghostwhite")
    f3.pack(side=BOTTOM)
    f1.pack(side=LEFT)
    f2.pack(side=RIGHT)
    Label(f1, text="Member's ID/Phone No. : ",
          font="comicsans 20", bg="ghostwhite").pack()
    global mem_id
    mem_id = StringVar()
    Entry(f2, textvariable=mem_id, font="comicsans 20").pack()
    Button(f3, text='Find', font='comicsans 20',
           bg="ghostwhite", command=find_info).pack()
    new16.bind('<Return>',lambda event:find_info())
    
    Button(f3, text='Back', font='comicsans 20',
           bg="ghostwhite", command=back16).pack()
    new16.bind('<Escape>',lambda event:back16())
    
    new16.mainloop()


def find_info():
    try:
        with open('books.bin', 'rb') as df:
            dat2 = df.read()
            dat1 = fernet.decrypt(dat2).decode()
        data = eval(dat1)
        mem = data[2]
        mem_ph = data[4]
        if int(mem_id.get()) in mem.keys():
            new16.destroy()
            global new17
            new17 = Tk()
            val = mem[int(mem_id.get())]
            new17.attributes('-fullscreen', True)
            new17.config(bg="ghostwhite")
            f = Frame(new17, bg="ghostwhite")
            f.place(in_=new17, anchor="c", relx=.5, rely=.5)
            f4 = Frame(f, bg="ghostwhite")
            f1 = Frame(f, bg="ghostwhite")
            f2 = Frame(f, bg="ghostwhite")
            f3 = Frame(f, bg="ghostwhite")
            f4.pack(side=TOP)
            f1.pack(side=BOTTOM)
            f2.pack(side=LEFT)
            f3.pack(side=RIGHT)
            Label(f4, text=f"Member's id : {mem_id.get()}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Name : {val[1]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Address : {val[2]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Phone : {val[3]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f2, text=f"New Member's Address : ",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f2, text=f"New Member's Phone : ",
                  font="comicsans 20", bg="ghostwhite").pack()
            global mem_adder
            mem_adder = StringVar()
            global mem_phon
            mem_phon = StringVar()
            Entry(f3, textvariable=mem_adder, font="comicsans 20").pack()
            Entry(f3, textvariable=mem_phon, font="comicsans 20").pack()
            Button(f1, text="Update", font="comicsans 20",
                   bg="ghostwhite", command=update).pack()
            Button(f1, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back17).pack()
            new17.bind('<Escape>',lambda event:back17())
            
            new17.mainloop()
        elif int(mem_id.get()) in mem_ph.keys():
            new16.destroy()
            global new171
            new171 = Tk()
            t = mem_ph[int(mem_id.get())]
            val = mem[t]
            new171.attributes('-fullscreen', True)
            new171.config(bg="ghostwhite")
            f = Frame(new171, bg="ghostwhite")
            f.place(in_=new171, anchor="c", relx=.5, rely=.5)
            f4 = Frame(f, bg="ghostwhite")
            f1 = Frame(f, bg="ghostwhite")
            f2 = Frame(f, bg="ghostwhite")
            f3 = Frame(f, bg="ghostwhite")
            f4.pack(side=TOP)
            f1.pack(side=BOTTOM)
            f2.pack(side=LEFT)
            f3.pack(side=RIGHT)
            Label(f4, text=f"Member's id : {t}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Name : {val[1]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Address : {val[2]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f4, text=f"Member's Phone : {val[3]}",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f2, text=f"New Member's Address : ",
                  font="comicsans 20", bg="ghostwhite").pack()
            Label(f2, text=f"New Member's Phone : ",
                  font="comicsans 20", bg="ghostwhite").pack()
            global mem_adder1
            mem_adder1 = StringVar()
            global mem_phon1
            mem_phon1 = StringVar()
            Entry(f3, textvariable=mem_adder1, font="comicsans 20").pack()
            Entry(f3, textvariable=mem_phon1, font="comicsans 20").pack()
            Button(f1, text="Update", font="comicsans 20",
                   bg="ghostwhite", command=update1).pack()
            Button(f1, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back171).pack()
            new171.bind('<Escape>',lambda event:back171())
            
            new171.mainloop()
        else:
            tmg.showerror(
                "Member", f"NO such Member present in Library's Database with Id = {mem_id.get()}")
    except:
        tmg.showerror("Member", "Please enter the correct information.")


def back171():
    new171.destroy()
    update_info1()


def update():
    with open('books.bin', 'rb') as df:
        dat2 = df.read()
        dat1 = fernet.decrypt(dat2).decode()
    data = eval(dat1)
    mem = data[2]
    mem_ph = data[4]
    val = mem[int(mem_id.get())]
    mem[int(mem_id.get())] = [val[0], val[1],
                              mem_adder.get(), int(mem_phon.get()), val[4]]
    mem_ph[int(mem_phon.get())] = mem_ph[val[3]]
    del mem_ph[val[3]]
    with open('books.bin', 'wb') as gh:
        data1 = fernet.encrypt(f"{data}".encode())
        gh.write(data1)
    tmg.showinfo("Member", "Member Info is updated.")


def update1():
    with open('books.bin', 'rb') as df:
        dat2 = df.read()
        dat1 = fernet.decrypt(dat2).decode()
    data = eval(dat1)
    mem = data[2]
    mem_ph = data[4]
    t = mem_ph[int(mem_id.get())]
    val = mem[t]
    mem[t] = [val[0], val[1],
              mem_adder1.get(), int(mem_phon1.get()), val[4]]
    mem_ph[int(mem_phon1.get())] = mem_ph[val[3]]
    del mem_ph[val[3]]
    with open('books.bin', 'wb') as gh:
        data1 = fernet.encrypt(f"{data}".encode())
        gh.write(data1)
    tmg.showinfo("Member", "Member Info is updated.")


def back17():
    new17.destroy()
    update_info1()


def back16():
    new16.destroy()
    login1()


def issue_book():
    new2.destroy()
    global new15
    new15 = Tk()
    new15.attributes('-fullscreen', True)
    new15.config(bg="ghostwhite")
    Frame(new15, bg="ghostwhite", height=230).pack()
    f = Frame(new15, bg="ghostwhite")
    f.pack()
    f3 = Frame(f, bg="ghostwhite")
    f3.pack(side=BOTTOM)
    f1 = Frame(f, bg="ghostwhite")
    f1.pack(side=LEFT, padx=10)
    f2 = Frame(f, bg="ghostwhite")
    f2.pack(side=RIGHT)
    global member_id
    member_id = StringVar()
    global books_id
    books_id = StringVar()
    global books_quan
    books_quan = IntVar()
    global dat11
    dat11 = DateEntry(f3, dateformat=3, width=12, background='ghostwhite', font="comicsans 18",
                      foreground='black', borderwidth=4)
    Label(f1, text="Member's ID/Phone NO. : ",
          bg="ghostwhite", font="comicsans 20").pack()
    Label(f1, text="Book's Id/Name : ",
          bg="ghostwhite", font="comicsans 20").pack()
    Label(f1, text="Quantity of Book : ",
          bg="ghostwhite", font="comicsans 20").pack()
    Entry(f2, textvariable=member_id, font="comicsans 20").pack()
    Entry(f2, textvariable=books_id, font="comicsans 20").pack()
    Entry(f2, textvariable=books_quan, font="comicsans 20").pack()
    Button(f3, text="Issue Book", font="comicsans 20",
           bg="ghostwhite", command=issue_books).pack()
    Button(f3, text="Back", font="comicsans 20",
           bg="ghostwhite", command=back15).pack()
    new15.bind('<Escape>',lambda event:back15())
    
    new15.mainloop()


def issue_books():
    with open("books.bin", "rb") as zx:
        dat = zx.read()
        dat1 = fernet.decrypt(dat).decode()
    data = eval(dat1)
    mem = data[2]
    boo = data[0]
    book = data[1]
    mem_phone = data[4]
    try:
        if int(member_id.get()) in mem.keys():
            if books_id.get().capitalize() in boo.keys():
                t = boo[books_id.get().capitalize()]
                member_name12 = mem[int(member_id.get())]
                val = book[t]
                if val[3] - books_quan.get() == 0 or val[3] - books_quan.get() > 0:
                    book[t] = [val[0], val[1], val[2],
                               val[3] - books_quan.get()]
                    book_trace = data[7]
                    stock_iss = data[6]
                    data[6] = stock_iss - books_quan.get()
                    member_trace = data[8]
                    if t not in book_trace.keys():
                        book_trace[t] = {}
                        book_trace[t][int(member_id.get())] = [
                            member_name12[1], dat11.get(), int(books_quan.get())]
                        if int(member_id.get()) not in member_trace.keys():
                            member_trace[int(member_id.get())] = {}
                            member_trace[int(member_id.get())][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                        else:
                            member_trace[int(member_id.get())][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                    else:
                        book_trace[t][int(member_id.get())] = [
                            member_name12[1], dat11.get(), int(books_quan.get())]
                        if int(member_id.get()) not in member_trace.keys():
                            member_trace[int(member_id.get())] = {}
                            member_trace[int(member_id.get())][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")

                        else:
                            member_trace[int(member_id.get())][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                else:
                    tmg.showerror(
                        "Books", f"Only {val[3]} books are avaliable.")
            elif int(books_id.get()) in book.keys():
                t = int(books_id.get())
                val = book[t]
                book_name12 = val[0]
                if val[3] - books_quan.get() == 0 or val[3] - books_quan.get() > 0:
                    book[t] = [val[0], val[1], val[2],
                               val[3] - books_quan.get()]
                    book_trace = data[7]
                    member_trace = data[8]
                    member_name12 = mem[int(member_id.get())]
                    stock_iss = data[6]  # book_name12, dat11.get()
                    data[6] = stock_iss - books_quan.get()
                    if t not in book_trace.keys():
                        book_trace[t] = {}
                        book_trace[t][int(member_id.get())] = [
                            member_name12[1], int(books_quan.get())]
                        if int(member_id.get()) not in member_trace.keys():
                            member_trace[int(member_id.get())] = {}
                            member_trace[int(member_id.get())][t] = [
                                book_name12, dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                        else:
                            member_trace[int(member_id.get())][t] = [
                                book_name12, dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                    else:
                        book_trace[t][int(member_id.get())] = [
                            member_name12[1], dat11.get(), int(books_quan.get())]
                        if int(member_id.get()) not in member_trace.keys():
                            member_trace[int(member_id.get())] = {}
                            member_trace[int(member_id.get())][t] = [
                                book_name12, dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                        else:
                            member_trace[int(member_id.get())][t] = [
                                book_name12, dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                else:
                    tmg.showerror(
                        "Books", f"Only {val[3]} books are avaliable.")
            else:
                tmg.showerror("Book", f"No such book is avaliable.")
        elif int(member_id.get()) in mem_phone.keys():
            memz = mem_phone[int(member_id.get())]
            if books_id.get().capitalize() in boo.keys():
                t = boo[books_id.get().capitalize()]
                val = book[t]
                if val[3] - books_quan.get() == 0 or val[3] - books_quan.get() > 0:
                    book[t] = [val[0], val[1], val[2],
                               val[3] - books_quan.get()]
                    book_trace = data[7]
                    member_trace = data[8]
                    member_name12 = mem[memz]
                    stock_iss = data[6]
                    data[6] = stock_iss - books_quan.get()
                    if t not in book_trace.keys():
                        book_trace[t] = {}
                        book_trace[t][memz] = [member_name12[1],
                                               dat11.get(), int(books_quan.get())]
                        if memz not in member_trace.keys():
                            member_trace[memz] = {}
                            member_trace[memz][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                        else:
                            member_trace[memz][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                    else:
                        book_trace[t][memz] = [member_name12[1],
                                               dat11.get(), int(books_quan.get())]
                        if memz not in member_trace.keys():
                            member_trace[memz] = {}
                            member_trace[memz][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                        else:
                            member_trace[memz][t] = [
                                books_id.get().capitalize(), dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                else:
                    tmg.showerror(
                        "Books", f"Only {val[3]} books are avaliable.")
            elif int(books_id.get()) in book.keys():
                t = int(books_id.get())
                val = book[t]
                book_name12 = val[0]
                if val[3] - books_quan.get() == 0 or val[3] - books_quan.get() > 0:
                    book[t] = [val[0], val[1], val[2],
                               val[3] - books_quan.get()]
                    book_trace = data[7]
                    member_trace = data[8]
                    member_name12 = mem[memz]
                    stock_iss = data[6]
                    data[6] = stock_iss - books_quan.get()
                    if t not in book_trace.keys():
                        book_trace[t] = {}
                        book_trace[t][memz] = [member_name12[1],
                                               dat11.get(), int(books_quan.get())]
                        if memz not in member_trace.keys():
                            member_trace[memz] = {}
                            member_trace[memz][t] = [book_name12,
                                                     dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                        else:
                            member_trace[memz][t] = [book_name12,
                                                     dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                    else:
                        book_trace[t][memz] = [member_name12[1],
                                               dat11.get(), int(books_quan.get())]
                        if memz not in member_trace.keys():
                            member_trace[memz] = {}
                            member_trace[memz][t] = [book_name12,
                                                     dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                        else:
                            member_trace[memz][t] = [book_name12,
                                                     dat11.get(), int(books_quan.get())]
                            with open("books.bin", "wb") as cvb:
                                data23 = fernet.encrypt(f'{data}'.encode())
                                cvb.write(data23)
                                tmg.showinfo(
                                    "Book", "Book is issued successfully.")
                else:
                    tmg.showerror(
                        "Books", f"Only {val[3]} books are avaliable.")
            else:
                tmg.showerror("Book", f"No such book is avaliable.")
        else:
            tmg.showerror(
                "Book", f"No such member is present in library database.")
    except Exception as e:
        tmg.showerror("Member", e)


def back15():
    new15.destroy()
    login1()


def find_mem():
    new2.destroy()
    find_mem1()


def find_mem1():
    global new5
    new5 = Tk()
    new5.attributes('-fullscreen', True)
    new5.config(bg="ghostwhite")
    Frame(new5, bg="ghostwhite", height=250).pack()
    f3 = Frame(new5, bg="ghostwhite")
    f3.pack()
    f = Frame(f3, bg="ghostwhite")
    f1 = Frame(f3, bg="ghostwhite")
    f2 = Frame(f3, bg="ghostwhite")

    f.pack(side=BOTTOM)
    f1.pack(side=LEFT)
    f2.pack(side=RIGHT)
    Label(f1, text="Member's ID/Phone No. : ",
          font="comicsans 20", bg="ghostwhite").pack()
    global id1
    id1 = StringVar()
    Entry(f2, textvariable=id1, font="comicsans 20").pack()
    Button(f, text="Find Member", bg="ghostwhite",
           font="comicsans 20", command=find_memb).pack()
    new5.bind('<Return>',lambda event:find_memb())
    
    Button(f, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back20).pack()
    new5.bind('<Escape>',lambda event:back20())
    
    new5.mainloop()


def find_memb():
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[0]
    books_name_dic = data[1]
    member_name = data[2]
    record = data[3]
    fb = data[4]
    try:
        if int(id1.get()) in member_name.keys():
            d = member_name[int(id1.get())]
            new5.destroy()
            global new13
            new13 = Tk()
            new13.attributes('-fullscreen', True)
            new13.config(bg="ghostwhite")
            # Frame(new13, bg="ghostwhite", height=250).pack()
            f = Frame(new13, bg="ghostwhite")
            f.place(in_=new13, anchor="c", rely=.5, relx=.5)
            Label(f, text=f"Member's ID :  {d[0]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Member's Name :  {d[1]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Member's Address :  {d[2]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Member's Phone No. :  {d[3]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Expiry Date :  {d[4]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            f3 = Frame(f, bg="ghostwhite")
            f3.pack(side=BOTTOM)
            f2 = Frame(f, bg="ghostwhite")
            f2.pack()
            Button(f3, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back141).pack()
            new13.bind('<Escape>',lambda event:back141())
            
            if int(id1.get()) in data[8].keys():
                scrollbar1 = Scrollbar(f2)
                scrollbar1.pack(side=RIGHT, fill=Y)
                Label(f2, text="Book's Id \t\t Book's Name \t Issued Date \t Quantity \t",
                      font="comicsans 20", bg="ghostwhite").pack()
                global l
                l = Listbox(f2, font="comicsans 15",
                            yscrollcommand=scrollbar1.set)
                l.pack(side=LEFT)
                global l1
                l1 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l1.pack(side=LEFT)
                global l2
                l2 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l2.pack(side=LEFT)
                global l3
                l3 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l3.pack(side=LEFT)
                scrollbar1.config(command=scroll4)
                for i in data[8][int(id1.get())].keys():
                    vc = data[8][int(id1.get())][i]
                    l.insert(END, i)
                    l1.insert(END, vc[0])
                    l2.insert(END, vc[1])
                    l3.insert(END, vc[2])
            new13.mainloop()
        elif int(id1.get()) in fb.keys():
            d1 = fb.get(int(id1.get()))
            d = member_name[d1]
            new5.destroy()
            global new14
            new14 = Tk()
            new14.attributes('-fullscreen', True)
            new14.config(bg="ghostwhite")
            Frame(new14, bg="ghostwhite", height=250).pack()
            f = Frame(new14, bg="ghostwhite")
            f.pack()
            Label(f, text=f"Member's ID :  {d[0]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Member's Name :  {d[1]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Member's Address :  {d[2]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Member's Phone No. :  {d[3]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Expiry Date :  {d[4]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            f2 = Frame(f, bg="ghostwhite")
            f2.pack()
            f3 = Frame(f, bg="ghostwhite")
            f3.pack()
            Button(f3, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back104).pack()
            new14.bind('<Escape>',lambda event:back104())
            
            if d1 in data[8].keys():
                scrollbar1 = Scrollbar(f2)
                scrollbar1.pack(side=RIGHT, fill=Y)
                Label(f2, text="Book's Id \t Book's Name \t Issued Date \t Quantity \t",
                      font="comicsans 20", bg="ghostwhite").pack()
                global l4
                l4 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l4.pack(side=LEFT)
                global l5
                l5 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l5.pack(side=LEFT)
                global l6
                l6 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l6.pack(side=LEFT)
                global l7
                l7 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l7.pack(side=LEFT)
                scrollbar1.config(command=scroll44)
                for i in data[8][d1].keys():
                    vc = data[8][d1][i]
                    l4.insert(END, i)
                    l5.insert(END, vc[0])
                    l6.insert(END, vc[1])
                    l7.insert(END, vc[2])
            new14.mainloop()
        else:
            tmg.showerror("Member", "No such member present in record.")
    except Exception as e:
        tmg.showerror("Book", e)


def back104():
    new14.destroy()
    find_mem1()


def back141():
    new13.destroy()
    find_mem1()


def back20():
    new5.destroy()
    login1()


def find_book():
    new2.destroy()
    find_book1()


def find_book1():
    global new5
    new5 = Tk()
    new5.attributes('-fullscreen', True)
    new5.config(bg="ghostwhite")
    # Frame(new5, bg="ghostwhite", height=250).pack()
    f3 = Frame(new5, bg="ghostwhite")
    f3.place(in_=new5, anchor="c", rely=.5, relx=.5)
    f = Frame(f3, bg="ghostwhite")
    f1 = Frame(f3, bg="ghostwhite")
    f2 = Frame(f3, bg="ghostwhite")

    f.pack(side=BOTTOM)
    f1.pack(side=LEFT)
    f2.pack(side=RIGHT)
    Label(f1, text="Book Name/ID : ", font="comicsans 20", bg="ghostwhite").pack()
    # Label(f1, text="Quantity", font="comicsans 20", bg="ghostwhite").pack()
    global id1
    id1 = StringVar()
    # global quanti
    # quanti = IntVar()
    Entry(f2, textvariable=id1, font="comicsans 20").pack()
    # Entry(f2, textvariable=quanti, font="comicsans 20").pack()
    Button(f, text="Find Book", bg="ghostwhite",
           font="comicsans 20", command=find_boo).pack()
    new5.bind('<Return>',lambda event:find_boo())
    
    Button(f, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back21).pack()
    new5.bind('<Escape>',lambda event:back21())
    
    new5.mainloop()


def find_boo():
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[0]
    books_name_dic = data[1]
    member_name = data[2]
    record = data[3]
    fb = dic.keys()
    df = books_name_dic.keys()
    try:
        if id1.get().capitalize() in fb:
            d1 = dic.get(id1.get().capitalize())
            d = books_name_dic.get(d1)
            new5.destroy()
            global new13
            new13 = Tk()
            new13.attributes('-fullscreen', True)
            new13.config(bg="ghostwhite")
            f78 = Frame(new13, bg="ghostwhite")
            f78.place(in_=new13, anchor="c", relx=.5, rely=.5)
            f = Frame(f78, bg="ghostwhite")
            f.pack()

            Label(f, text=f"Book's ID :  {d1}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Book's Name :  {d[0]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Book's Author :  {d[1]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Book's Total Quantity :  {d[2]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Book's Quantity Available :  {d[3]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            f1 = Frame(f, bg="ghostwhite")
            f1.pack(side=BOTTOM)
            f2 = Frame(f, bg="ghostwhite")
            f2.pack(side=BOTTOM)
            Button(f1, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back14).pack()
            new13.bind('<Escape>',lambda event:back14())
            
            if d1 in data[7].keys():
                scrollbar1 = Scrollbar(f2)
                scrollbar1.pack(side=RIGHT, fill=Y)
                Label(f2, text="Member's Id \t Member's Name \t Issued Date \t Quantity \t",
                      font="comicsans 20", bg="ghostwhite").pack()
                global l
                l = Listbox(f2, font="comicsans 15",
                            yscrollcommand=scrollbar1.set)
                l.pack(side=LEFT)
                global l1
                l1 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l1.pack(side=LEFT)
                global l2
                l2 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l2.pack(side=LEFT)
                global l3
                l3 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l3.pack(side=LEFT)
                scrollbar1.config(command=scroll4)
                for i in data[7][d1].keys():
                    vc = data[7][d1][i]
                    l.insert(END, i)
                    l1.insert(END, vc[0])
                    l2.insert(END, vc[1])
                    l3.insert(END, vc[2])
            new13.mainloop()
        elif id1.get().capitalize() not in fb:
            d = books_name_dic.get(int(id1.get()))
            d1 = int(id1.get())
            new5.destroy()
            global new14
            new14 = Tk()
            new14.attributes('-fullscreen', True)
            new14.config(bg="ghostwhite")
            Frame(new14, bg="ghostwhite", height=250).pack()
            f78 = Frame(new14, bg="ghostwhite")
            f78.place(in_=new14, anchor="c", relx=.5, rely=.5)
            f = Frame(f78, bg="ghostwhite")
            f.pack()
            Label(f, text=f"Book's ID :  {id1.get()}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Book's Name :  {d[0]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Book's Author :  {d[1]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            Label(f, text=f"Book's Quantity :  {d[2]}",
                  bg="ghostwhite", font="comicsans 20").pack()
            # Button(f, text="Back", font="comicsans 20",
            #    bg="ghostwhite", command=back114).pack()
            f1 = Frame(f, bg="ghostwhite")
            f1.pack(side=BOTTOM)
            f2 = Frame(f, bg="ghostwhite")
            f2.pack(side=BOTTOM)
            Button(f1, text="Back", font="comicsans 20",
                   bg="ghostwhite", command=back114).pack()
            new14.bind('<Escape>',lambda event:back114())
            
            if d1 in data[7].keys():
                scrollbar1 = Scrollbar(f2)
                scrollbar1.pack(side=RIGHT, fill=Y)
                Label(f2, text="Member's Id \t Member's Name \t Issued Date \t Quantity \t",
                      font="comicsans 20", bg="ghostwhite").pack()
                global l4
                l4 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l4.pack(side=LEFT)
                global l5
                l5 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l5.pack(side=LEFT)
                global l6
                l6 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l6.pack(side=LEFT)
                global l7
                l7 = Listbox(f2, font="comicsans 15",
                             yscrollcommand=scrollbar1.set)
                l7.pack(side=LEFT)
                scrollbar1.config(command=scroll44)
                for i in data[7][d1].keys():
                    vc = data[7][d1][i]
                    l4.insert(END, i)
                    l5.insert(END, vc[0])
                    l6.insert(END, vc[1])
                    l7.insert(END, vc[2])
            new14.mainloop()
        else:
            tmg.showerror("Book", "No such book present in library.")
    except Exception as e:
        tmg.showerror("Book", e)


def scroll4(x, y):
    l.yview(x, y)
    l1.yview(x, y)
    l2.yview(x, y)
    l3.yview(x, y)


def scroll44(x, y):
    l4.yview(x, y)
    l5.yview(x, y)
    l6.yview(x, y)
    l7.yview(x, y)


def back14():
    new13.destroy()
    find_book1()


def back114():
    new14.destroy()
    find_book1()


def back21():
    new5.destroy()
    login1()


def entry_record1():
    new2.destroy()
    entry_record()


def entry_record():
    global new10
    new10 = Tk()
    new10.attributes('-fullscreen', True)
    new10.config(bg="ghostwhite")
    # Frame(new10, bg="ghostwhite", height=250).pack()
    f = Frame(new10, bg="ghostwhite")
    f.place(in_=new10, anchor="c", relx=.5, rely=.5)
    f1 = Frame(f, bg="ghostwhite")
    f1.pack(side=BOTTOM)
    f2 = Frame(f, bg="ghostwhite")
    f2.pack(side=LEFT)
    f3 = Frame(f, bg="ghostwhite")
    f3.pack(side=RIGHT)
    Label(f2, text="Date", bg="ghostwhite", font="comicsans 20").pack(padx=20)
    global dat
    dat = DateEntry(f3, dateformat=3, width=12, background='ghostwhite', font="comicsans 18",
                    foreground='black', borderwidth=4)
    dat.pack()
    Button(f1, text="Load Record", font="comicsans 20",
           bg="ghostwhite", command=load_record).pack()
    new10.bind('<Return>',lambda event:load_record())
    
    Button(f1, text="Back", font="comicsans 20",
           bg="ghostwhite", command=back9).pack()
    new10.bind('<Escape>',lambda event:back9())
    
    new10.mainloop()


def load_record():
    with open("books.bin", "rb") as xc:
        data1 = xc.read()
    dat1 = fernet.decrypt(data1).decode()
    data = eval(dat1)
    recor = data[3]
    g = str(dat.get())
    if str(dat.get()) in recor.keys():
        new10.destroy()
        global new11
        new11 = Tk()
        new11.attributes('-fullscreen', True)
        new11.config(bg="ghostwhite")
        f = Frame(new11, bg="ghostwhite")
        f.pack(side=BOTTOM)
        f1 = Frame(new11, bg="ghostwhite")
        f1.pack(pady=40)
        Scroll_bar = Scrollbar(f1)
        global l
        global l1
        global l2
        global l3
        Label(f1, text="ID \t\t Name \t\t Entry\t\tExit\t",
              bg="ghostwhite", font="comicsans 20").pack()
        l = Listbox(f1, height="25", font="comicssans 15",
                    yscrollcommand=Scroll_bar.set)
        l1 = Listbox(f1, height="25", font="comicssans 15",
                     yscrollcommand=Scroll_bar.set)
        l2 = Listbox(f1, height="25", font="comicssans 15",
                     yscrollcommand=Scroll_bar.set)
        l3 = Listbox(f1, height="25", font="comicssans 15",
                     yscrollcommand=Scroll_bar.set)
        l.pack(side="left")
        l1.pack(side="left")
        l2.pack(side="left")
        l3.pack(side="left")
        reco = recor[g]
        for i in reco.keys():
            val = reco[i]
            l.insert(END, i)
            l1.insert(END, val[0])
            l2.insert(END, val[1])
            if len(val) == 3:
                l3.insert(END, val[2])

        Scroll_bar.pack(side=LEFT, fill=Y)
        Scroll_bar.config(command=scroll3)
        Button(f, text="Back", bg="ghostwhite",
               font="comicsans 20", command=back13).pack()
        new11.bind('<Escape>',lambda event:back13())
        
        new11.mainloop()
    else:
        tmg.showerror("Record", f"No record is avaliable for {dat.get()}")


def back13():
    new11.destroy()
    entry_record()


def scroll3(x, y):
    l.yview(x, y)
    l1.yview(x, y)
    l2.yview(x, y)
    l3.yview(x, y)


def back9():
    new10.destroy()
    login1()


def entry_exit():
    new2.destroy()
    global new9
    new9 = Tk()
    new9.attributes('-fullscreen', True)
    new9.config(bg="ghostwhite")
    Frame(new9, bg="ghostwhite", height=200).pack()
    f1 = Frame(new9, bg="ghostwhite")
    f1.pack()
    f3 = Frame(new9, bg="ghostwhite")
    f3.pack(side=BOTTOM)
    f = LabelFrame(f1, text="Entry", bg="ghostwhite", font="comicsans 30")
    f.pack(side=LEFT)
    f2 = LabelFrame(f1, text="Exit", bg="ghostwhite", font="comicsans 30")
    f2.pack(side=RIGHT, padx=10)
    fa5 = Frame(f, bg="ghostwhite")
    fa5.pack(side=BOTTOM)
    fa = Frame(f, bg="ghostwhite")
    fa.pack(side=LEFT)
    fa1 = Frame(f, bg="ghostwhite")
    fa1.pack(side=RIGHT)
    fa6 = Frame(f2, bg="ghostwhite")
    fa6.pack(side=BOTTOM)
    fa3 = Frame(f2, bg="ghostwhite")
    fa3.pack(side=LEFT)
    fa4 = Frame(f2, bg="ghostwhite")
    fa4.pack(side=RIGHT)
    Label(fa, text="Memder's ID ", font='comicsans 20', bg="ghostwhite").pack()
    global mem_id
    mem_id = StringVar()
    Entry(fa1, textvariable=mem_id, font="comocsans 20").pack(padx=10)
    Button(fa5, text="Add Entry", bg="ghostwhite",
           font="comicsans 20", command=add_entry).pack(pady=10)
    Label(fa3, text="Memder's ID ", font='comicsans 20', bg="ghostwhite").pack()
    global mem_id1
    mem_id1 = StringVar()
    global date1
    date1 = DateEntry(f1, dateformat=3, width=12, background='ghostwhite', font="comicsans 18",
                      foreground='black', borderwidth=4)
    Entry(fa4, textvariable=mem_id1, font="comocsans 20").pack(padx=10)
    Button(fa6, text="Add Exit", bg="ghostwhite",
           font="comicsans 20", command=add_exit).pack(pady=10)
    Button(f3, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back8).pack(pady=10)
    new9.bind('<Escape>',lambda event:back8())

    new9.mainloop()


def add_exit():
    with open("books.bin", "rb") as cv:
        dat = cv.read()
    data1 = fernet.decrypt(dat).decode()
    data = eval(data1)
    dic = data[0]
    Time = time.asctime(time.localtime(time.time()))
    # tmg.showerror("", Time)
    book_n = data[1]
    mem_n = data[2]
    record = data[3]
    valu = mem_n.keys()
    try:
        if int(mem_id1.get()) in valu:
            value = mem_n.get(int(mem_id1.get()))
            da = value[4]
            date3 = da.split("/")
            date2 = str(date1.get())
            date4 = date2.split("/")
            if int(date4[2]) < int(date3[2]):
                if mem_id1.get() in record[str(date1.get())].keys():
                    time1 = Time.split(' ')
                    m = record[str(date1.get())][mem_id1.get()]
                    record[str(date1.get())][mem_id1.get()] = [
                        m[0], m[1], f"{time1[3]}"]
                    with open("books.bin", "wb") as xc:
                        data2 = fernet.encrypt(f"{data}".encode())
                        xc.write(data2)
                else:
                    tmg.showerror(
                        "Entry", f"Entry of member {mem_id1.get()} is not entered till now.")
            elif int(date4[2]) == int(date3[2]):
                if int(date4[1]) < int(date3[1]):
                    if mem_id1.get() in record[str(date1.get())].keys():
                        time1 = Time.split(' ')
                        m = record[str(date1.get())][mem_id1.get()]
                        record[str(date1.get())][mem_id1.get()] = [
                            m[0], m[1], f"{time1[3]}"]
                        with open("books.bin", "wb") as xc:
                            data2 = fernet.encrypt(f"{data}".encode())
                            xc.write(data2)
                    else:
                        tmg.showerror(
                            "Entry", f"Entry of member {mem_id1.get()} is not entered till now.")
                elif int(date4[1]) == int(date3[1]):
                    if int(date4[0]) < int(date3[0]):
                        if mem_id1.get() in record[str(date1.get())].keys():
                            time1 = Time.split(' ')
                            m = record[str(date1.get())][mem_id1.get()]
                            record[str(date1.get())][mem_id1.get()] = [
                                m[0], m[1], f"{time1[3]}"]
                            with open("books.bin", "wb") as xc:
                                data2 = fernet.encrypt(f"{data}".encode())
                                xc.write(data2)
                        else:
                            tmg.showerror(
                                "Entry", f"Entry of member {mem_id1.get()} is not entered till now.")
                    else:
                        tmg.showerror(
                            "Member", f"ID = {mem_id.get()} has been expired.")
                else:
                    tmg.showerror(
                        "Member", f"ID = {mem_id.get()} has been expired.")
            else:
                tmg.showerror(
                    "Member", f"ID = {mem_id.get()} has been expired.")
        else:
            tmg.showerror("Member", f"No member have ID = {mem_id.get()}")
    except:
        tmg.showerror("Member", f"No member have ID = {mem_id.get()}")


def add_entry():
    with open("books.bin", "rb") as cv:
        dat = cv.read()
    data1 = fernet.decrypt(dat).decode()
    data = eval(data1)
    dic = data[0]
    book_n = data[1]
    mem_n = data[2]
    Time = time.asctime(time.localtime(time.time()))
    record = data[3]
    valu = mem_n.keys()
    # print(mem_n)
    # print(valu)
    try:
        if int(mem_id.get()) in valu:
            value = mem_n.get(int(mem_id.get()))
            da = value[4]
            date3 = da.split("/")
            date2 = str(date1.get())
            date4 = date2.split("/")
            if int(date4[2]) < int(date3[2]):
                if str(date1.get()) not in record.keys():
                    record[str(date1.get())] = {}
                    time1 = Time.split(' ')
                    na = mem_n[int(mem_id.get())]
                    record[str(date1.get())][mem_id.get()] = [
                        na[1], f"{time1[3]}"]
                    with open("books.bin", "wb") as xc:
                        data2 = fernet.encrypt(f"{data}".encode())
                        xc.write(data2)
                else:
                    na = mem_n[int(mem_id.get())]
                    time1 = Time.split(' ')
                    record[str(date1.get())][mem_id.get()] = [
                        na[1], f"{time1[3]}"]
                    with open("books.bin", "wb") as xc:
                        data2 = fernet.encrypt(f"{data}".encode())
                        xc.write(data2)
            elif int(date4[2]) == int(date3[2]):
                if int(date4[1]) < int(date3[1]):
                    if str(date1.get()) not in record.keys():
                        record[str(date1.get())] = {}
                        time1 = Time.split(' ')
                        na = mem_n[int(mem_id.get())]
                        record[str(date1.get())][mem_id.get()] = [
                            na[1], f"{time1[3]}"]
                        with open("books.bin", "wb") as xc:
                            data2 = fernet.encrypt(f"{data}".encode())
                            xc.write(data2)
                    else:
                        time1 = Time.split(' ')
                        na = mem_n[int(mem_id.get())]
                        record[str(date1.get())][mem_id.get()] = [
                            na[1], f"{time1[3]}"]
                        with open("books.bin", "wb") as xc:
                            data2 = fernet.encrypt(f"{data}".encode())
                            xc.write(data2)
                elif int(date4[1]) == int(date3[1]):
                    if int(date4[0]) < int(date3[0]):
                        if str(date1.get()) not in record.keys():
                            record[str(date1.get())] = {}
                            time1 = Time.split(' ')
                            na = mem_n[int(mem_id.get())]
                            record[str(date1.get())][mem_id.get()] = [
                                na[1], f"{time1[3]}"]
                            with open("books.bin", "wb") as xc:
                                data2 = fernet.encrypt(f"{data}".encode())
                                xc.write(data2)
                        else:
                            time1 = Time.split(' ')
                            na = mem_n[int(mem_id.get())]
                            record[str(date1.get())][mem_id.get()] = [
                                na[1], f"{time1[3]}"]
                            with open("books.bin", "wb") as xc:
                                data2 = fernet.encrypt(f"{data}".encode())
                                xc.write(data2)
                    else:
                        tmg.showerror(
                            "Member", f"ID = {mem_id.get()} has been expired.")
                else:
                    tmg.showerror(
                        "Member", f"ID = {mem_id.get()} has been expired.")
            else:
                tmg.showerror(
                    "Member", f"ID = {mem_id.get()} has been expired.")
        else:
            tmg.showerror("Member", f"No member have ID = {mem_id.get()}")
    except:
        tmg.showerror("Member", f"No member have ID = {mem_id.get()}")


def back8():
    new9.destroy()
    login1()


def lsi_bo_mem():
    new2.destroy()
    lis_bo_mem1()


def lis_bo_mem1():
    global new7
    new7 = Tk()
    new7.attributes('-fullscreen', True)
    new7.config(bg="ghostwhite")
    Frame(new7, bg="ghostwhite", height=250).pack()
    f = Frame(new7, bg="ghostwhite")
    f.pack()
    Button(f, bg="ghostwhite", text="Books",
           font="comicsans 20", command=books_lis).pack()
    Button(f, bg="ghostwhite", text="Members",
           font="comicsans 20", command=mem_lis).pack()
    Button(f, bg="ghostwhite", text="Back",
           font="comicsans 20", command=back6).pack()
    new7.bind('<Escape>',lambda event:back6())
    

    new7.mainloop()


def mem_lis():
    new7.destroy()
    global new8
    new8 = Tk()
    new8.attributes('-fullscreen', True)
    new8.config(bg="ghostwhite")
    f2 = Frame(new8, bg="ghostwhite")
    f2.pack(pady=100)
    Scroll_bar = Scrollbar(f2)
    global l
    global l1
    global l2
    global l3
    global l4
    Button(f2, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back7).pack(side=BOTTOM)
    new8.bind('<Escape>',lambda event:back7())
    Label(f2, text="ID\tMember Name \t Address \t\t Phone No.\tExpiry Date\t",
          bg="ghostwhite", font="comicsans 20").pack()
    l = Listbox(f2, height="25", font="comicssans 15",
                yscrollcommand=Scroll_bar.set)
    l1 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l2 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l3 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l4 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l.pack(side="left")
    l1.pack(side="left")
    l2.pack(side="left")
    l3.pack(side="left")
    l4.pack(side="left")
    Scroll_bar.pack(side=LEFT, fill=Y)
    Scroll_bar.config(command=scroll2)
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[1]
    books_name_dic = data[0]
    member_dic = data[2]
    value = member_dic.values()
    for i in value:
        l.insert(END, i[0])
        l1.insert(END, i[1])
        l2.insert(END, i[2])
        l3.insert(END, i[3])
        l4.insert(END, i[4])

    new8.mainloop()


def scroll2(x, y):
    l.yview(x, y)
    l1.yview(x, y)
    l2.yview(x, y)
    l3.yview(x, y)
    l4.yview(x, y)


def back7():
    new8.destroy()
    lis_bo_mem1()


def books_lis():
    new7.destroy()
    global new8
    new8 = Tk()
    new8.attributes('-fullscreen', True)
    new8.config(bg="ghostwhite")
    f2 = Frame(new8, bg="ghostwhite")
    f2.pack(pady=100)
    Scroll_bar = Scrollbar(f2)
    global l
    Button(f2, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back7).pack(side=BOTTOM)
    new8.bind('<Escape>',lambda event:back7())
    
    global l1
    global l4
    global l2
    global l3
    Label(f2, text="Id\t\tBook Name \t Author \t\t Quantity\t\tAvailable Quantity\t",
          bg="ghostwhite", font="comicsans 20").pack()
    l4 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l = Listbox(f2, height="25", font="comicssans 15",
                yscrollcommand=Scroll_bar.set)
    l1 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l2 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l3 = Listbox(f2, height="25", font="comicssans 15",
                 yscrollcommand=Scroll_bar.set)
    l4.pack(side="left")
    l.pack(side="left")
    l1.pack(side="left")
    l2.pack(side="left")
    l3.pack(side="left")
    Scroll_bar.pack(side=LEFT, fill=Y)
    Scroll_bar.config(command=scroll1)
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[0]
    books_name_dic = data[1]
    member_dic = data[2]
    value = books_name_dic.keys()
    for i1 in value:
        i = books_name_dic.get(i1)
        l4.insert(END, i1)
        l.insert(END, i[0])
        l1.insert(END, i[1])
        l2.insert(END, i[2])
        l3.insert(END, i[3])

    new8.mainloop()


def scroll1(x, y):
    l4.yview(x, y)
    l.yview(x, y)
    l1.yview(x, y)
    l2.yview(x, y)
    l3.yview(x, y)


def back6():
    new7.destroy()
    login1()


def Manage_members():
    new2.destroy()
    Manage_members1()


def Manage_members1():
    global new6
    new6 = Tk()
    new6.attributes('-fullscreen', True)
    new6.config(bg="ghostwhite")
    Frame(new6, height=250, bg="ghostwhite").pack()
    Button(new6, text="Add A New Member", bg="ghostwhite",
           font="comicsans 20", command=add_member).pack()
    Button(new6, text="Remove A Member", bg="ghostwhite",
           font="comicsans 20", command=remove_mem).pack()
    Button(new6, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back4).pack()
    new6.bind('<Escape>',lambda event:back4())
    
    new6.mainloop()


def remove_mem():
    new6.destroy()
    global new4
    new4 = Tk()
    new4.attributes('-fullscreen', True)
    new4.config(bg="ghostwhite")

    Frame(new4, height=200, bg="ghostwhite").pack()
    f3 = Frame(new4, bg="ghostwhite")
    f3.pack()
    f = Frame(f3, bg="ghostwhite")
    f1 = Frame(f3, bg="ghostwhite")
    f4 = Frame(f3, bg="ghostwhite")
    f4.pack(side=BOTTOM)
    f.pack(side=LEFT)
    f1.pack(side=RIGHT)
    global membe_id
    # global me/mb_adder
    # global mem_no
    membe_id = StringVar()
    # memb_adder = StringVar()
    # mem_no = StringVar()
    Label(f, text="Member ID", bg="ghostwhite", font="comicsans 20").pack()
    # Label(f, text="Adderss", bg="ghostwhite", font="comicsans 20").pack()
    # Label(f, text="PHONE No.", bg="ghostwhite", font="comicsans 20").pack()
    Entry(f1, textvariable=membe_id, font="comicsans 19").pack()
    # Entry(f1, textvariable=memb_adder, font="comicsans 19").pack()
    # Entry(f1, textvariable=mem_no, font="comicsans 19").pack()
    Button(f4, text="Remove Member", bg="ghostwhite",
           font="comicsans 20", command=remove_memb).pack()
    Button(f4, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back5).pack()
    new4.bind('<Escape>',lambda event:back5())
    new4.mainloop()


def back5():
    new4.destroy()
    Manage_members1()


def remove_memb():
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[0]
    books_name_dic = data[1]
    member_name = data[2]
    record = data[3]
    phone = data[4]
    nj = member_name.keys()
    try:
        if int(membe_id.get()) in nj:
            z = member_name[int(membe_id.get())]
            del phone[z[3]]
            del member_name[int(membe_id.get())]
            with open("books.bin", "wb") as bomem:
                dat = fernet.encrypt(
                    f"{data}".encode())
                bomem.write(dat)
            tmg.showinfo(
                "Member", f"{membe_id.get()} member is successfully removed.")
        else:
            tmg.showerror("Member", f"No member have this ID {membe_id.get()}")
    except:
        tmg.showerror("Member", f"No member have this ID {membe_id.get()}")


def add_member():
    new6.destroy()
    global new4
    new4 = Tk()
    new4.attributes('-fullscreen', True)
    new4.config(bg="ghostwhite")

    Frame(new4, height=200, bg="ghostwhite").pack()
    f3 = Frame(new4, bg="ghostwhite")
    f3.pack()
    f = Frame(f3, bg="ghostwhite")
    f1 = Frame(f3, bg="ghostwhite")
    f4 = Frame(f3, bg="ghostwhite")
    f4.pack(side=BOTTOM)
    f.pack(side=LEFT)
    f1.pack(side=RIGHT)
    global memb_name
    global memb_adder
    global mem_no
    memb_name = StringVar()
    memb_adder = StringVar()
    mem_no = StringVar()
    mon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    Label(f, text="Member Name", bg="ghostwhite", font="comicsans 20").pack()
    Label(f, text="Address", bg="ghostwhite", font="comicsans 20").pack()
    Label(f, text="PHONE No.", bg="ghostwhite", font="comicsans 20").pack()
    Label(f, text="Expiry Date", bg="ghostwhite", font="comicsans 20").pack()
    Entry(f1, textvariable=memb_name, font="comicsans 19").pack()
    Entry(f1, textvariable=memb_adder, font="comicsans 19").pack()
    Entry(f1, textvariable=mem_no, font="comicsans 19").pack()
    global date
    date = DateEntry(f1, dateformat=3, width=12, background='ghostwhite', font="comicsans 18",
                     foreground='black', borderwidth=4)
    date.pack()
    # tmg.showinfo("", date.get())
    Button(f4, text="Add Member", bg="ghostwhite",
           font="comicsans 20", command=add_memb).pack()
    Button(f4, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back5).pack()
    new4.bind('<Escape>',lambda event:back5())
    
    new4.mainloop()


def back5():
    new4.destroy()
    Manage_members1()


def memb_id():
    a = random.randint(0, 9)
    a1 = random.randint(0, 9)
    a2 = random.randint(0, 9)
    a3 = random.randint(0, 9)
    a4 = random.randint(0, 9)
    # a5 = random.randint(0, 9)
    # a6 = random.randint(0, 9)
    # a7 = random.randint(0, 9)
    # a8 = random.randint(0, 9)
    # a9 = random.randint(0, 9)
    global id
    id = f"{a}{a1}{a2}{a3}{a4}"


def add_memb():
    if memb_name.get() != "" and memb_adder.get() != "" and len(mem_no.get()) == 10:
        with open("books.bin", "rb") as boo:
            book = boo.read()
        books = fernet.decrypt(book).decode()
        # print(books)
        data = eval(books)
        s = data[4]
        if int(mem_no.get()) not in s.keys():
            # print(data)
            dic = data[0]
            books_name_dic = data[1]
            member_name = data[2]
            record = data[3]
            phone = data[4]
            memb_id()
            keya = member_name.keys()
            if int(id) not in keya:
                phone[int(mem_no.get())] = int(id)
                member_name[int(id)] = [int(id), memb_name.get(),
                                        memb_adder.get(), int(mem_no.get()), str(date.get())]
                with open("books.bin", "wb") as xc:
                    dat = fernet.encrypt(
                        f"{data}".encode())
                    xc.write(dat)
                tmg.showinfo("Member", f"Member's ID = {id}")
            else:
                add_memb()
        else:
            tmg.showerror(
                "Member", f"{mem_no.get()} is already registered by other member.")
    else:
        tmg.showerror("Member", "Please enter correct and valid information. ")


def back4():
    new6.destroy()
    login1()


def back3():
    new2.destroy()


def manage_books():
    new2.destroy()
    manage_books1()


def manage_books1():
    global new6
    new6 = Tk()
    new6.attributes('-fullscreen', True)
    new6.config(bg="ghostwhite")
    Frame(new6, height=250, bg="ghostwhite").pack()
    Button(new6, text="Add Stock", bg="ghostwhite",
           font="comicsans 20", command=add_book_stock).pack()
    Button(new6, text="Add New Book", bg="ghostwhite",
           font="comicsans 20", command=add_new_book).pack()
    Button(new6, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back11).pack()
    new6.bind('<Escape>',lambda event:back11())
    new6.mainloop()


def add_book_stock():
    new6.destroy()
    global new5
    new5 = Tk()
    new5.attributes('-fullscreen', True)
    new5.config(bg="ghostwhite")
    Frame(new5, bg="ghostwhite", height=250).pack()
    f3 = Frame(new5, bg="ghostwhite")
    f3.pack()
    f = Frame(f3, bg="ghostwhite")
    f1 = Frame(f3, bg="ghostwhite")
    f2 = Frame(f3, bg="ghostwhite")

    f.pack(side=BOTTOM)
    f1.pack(side=LEFT)
    f2.pack(side=RIGHT)
    Label(f1, text="Book Name/ID", font="comicsans 20", bg="ghostwhite").pack()
    Label(f1, text="Quantity", font="comicsans 20", bg="ghostwhite").pack()
    global id1
    id1 = StringVar()
    global quanti
    quanti = IntVar()
    Entry(f2, textvariable=id1, font="comicsans 20").pack()
    Entry(f2, textvariable=quanti, font="comicsans 20").pack()
    Button(f, text="Add Stock", bg="ghostwhite",
           font="comicsans 20", command=add_stock).pack()
    Button(f, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back2).pack()
    new5.bind('<Escape>',lambda event:back2())

    new5.mainloop()


def add_stock():
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[0]
    books_name_dic = data[1]
    member_name = data[2]
    record = data[3]
    fb = dic.keys()
    df = books_name_dic.keys()
    # try:
    if id1.get().capitalize() in fb:
        d2 = dic.get(id1.get().capitalize())
        d1 = books_name_dic.get(d2)
        print(d1)
        books_name_dic[d2] = [d1[0], d1[1],
                              d1[2]+quanti.get(), d1[3]+quanti.get()]
        tot_boo = data[5]
        tot_boo3 = data[6]
        tot_boo1 = tot_boo + quanti.get()
        tot_boo4 = tot_boo3 + quanti.get()
        data[5] = tot_boo1
        data[6] = tot_boo4

        with open("books.bin", "wb") as xc:
            dat = fernet.encrypt(
                f'''{data}'''.encode())
            xc.write(dat)
        tmg.showinfo(
            "Book", f"Stock is successfully added.\nBook ID = {d2}")
    elif id1.get().capitalize() not in fb:
        d = books_name_dic.get(int(id1.get()))
        books_name_dic[int(id1.get())] = [d[0], d[1], d[2] +
                                          quanti.get(), d[3]+quanti.get()]
        tot_boo = data[5]
        tot_boo3 = data[6]
        tot_boo1 = tot_boo + quanti.get()
        tot_boo4 = tot_boo3 + quanti.get()
        data[5] = tot_boo1
        data[6] = tot_boo4
        with open("books.bin", "wb") as xc:
            dat = fernet.encrypt(
                f'''{data}'''.encode())
            xc.write(dat)
        tmg.showinfo("Book", "Stock is successfully added.")
    # except:
        # None
    else:
        tmg.showerror("Book", "No such book present in library.")
    # except Exception as e:
        # tmg.showerror("Book", e)


def back2():
    new5.destroy()
    manage_books1()


def add_new_book():
    new6.destroy()
    global new4
    new4 = Tk()
    new4.attributes('-fullscreen', True)
    new4.config(bg="ghostwhite")

    Frame(new4, height=200, bg="ghostwhite").pack()
    f3 = Frame(new4, bg="ghostwhite")
    f3.pack()
    f = Frame(f3, bg="ghostwhite")
    f1 = Frame(f3, bg="ghostwhite")
    f4 = Frame(f3, bg="ghostwhite")
    f4.pack(side=BOTTOM)
    f.pack(side=LEFT)
    f1.pack(side=RIGHT)
    global book_name
    global book_author
    global book_no
    book_name = StringVar()
    book_author = StringVar()
    book_no = IntVar()
    Label(f, text="Book Name", bg="ghostwhite", font="comicsans 20").pack()
    Label(f, text="Name of Author", bg="ghostwhite", font="comicsans 20").pack()
    Label(f, text="No. of Books", bg="ghostwhite", font="comicsans 20").pack()
    Entry(f1, textvariable=book_name, font="comicsans 19").pack()
    Entry(f1, textvariable=book_author, font="comicsans 19").pack()
    Entry(f1, textvariable=book_no, font="comicsans 19").pack()
    Button(f4, text="Add Books", bg="ghostwhite",
           font="comicsans 20", command=add_book).pack()
    Button(f4, text="Back", bg="ghostwhite",
           font="comicsans 20", command=back10).pack()
    new4.bind('<Escape>',lambda event:back10())

    new4.mainloop()


def book_id():
    a = random.randint(0, 9)
    a1 = random.randint(0, 9)
    a2 = random.randint(0, 9)
    a3 = random.randint(0, 9)
    a4 = random.randint(0, 9)
    a5 = random.randint(0, 9)
    # a6 = random.randint(0, 9)
    # a7 = random.randint(0, 9)
    # a8 = random.randint(0, 9)
    # a9 = random.randint(0, 9)
    global id
    id = f"{a}{a1}{a2}{a3}{a4}{a5}"


def add_book():
    with open("books.bin", "rb") as boo:
        book = boo.read()
    books = fernet.decrypt(book).decode()
    # print(books)
    data = eval(books)
    # print(data)
    dic = data[1]
    books_name_dic = data[0]
    member_dic = data[2]
    record = data[3]
    aaas = dic.keys()
    as1 = books_name_dic.keys()
    book_id()
    if book_name.get().capitalize() not in as1:
        if int(id) not in aaas:
            dic[int(id)] = [book_name.get().capitalize(),
                            book_author.get(), book_no.get(), book_no.get()]
            books_name_dic[book_name.get().capitalize()] = int(id)
            # tmg.showinfo("", dic)
            # dic1 = bytes(str(dic), 'utf-8')
            ta = data[5]
            ta1 = data[6]
            data[5] = ta + book_no.get()
            data[6] = ta1 + book_no.get()
            new_dic = fernet.encrypt(
                f'''{data}'''.encode())
            with open("books.bin", "wb") as df:
                df.write(new_dic)
            # with open("books.bin", "rb") as df:
            #     sd = df.read()
            # ass = fernet.decrypt(sd).decode()
            tmg.showinfo(
                "Books", f"Book is added successfully added.\nBook ID = {id}")
        else:
            add_book()
    else:
        tmg.showerror(
            "Book", f"{book_name.get()} is already avaliable in Library.")


def back10():
    new4.destroy()
    manage_books1()


def back11():
    new6.destroy()
    login1()


def login():
    if use.get() == "arpit" and pas.get() == password and ro.get() == 1:
        tmg.showinfo("Login", "Successfully login.")
        root.destroy()
        login1()
    else:
        tmg.showerror("Login", "Invalid Username and Password.")


def change():
    with open("pas.bin", "wb") as f:
        g = fernet.encrypt(newpas1.get().encode())
        f.write(g)
    tmg.showinfo("Password", "Password changed successfully.")
    new1.destroy()
    main()


def back1():
    new1.destroy()
    main()


def submit():
    if forp.get().capitalize() == "Coding":
        new.destroy()
        global new1
        new1 = Tk()
        new1.attributes('-fullscreen', True)
        new1.config(bg="ghoastwhite")
        Frame(new1, bg="ghoastwhite", height=250).pack()
        f = Frame(new1, bg="ghoastwhite")
        f.pack()
        Label(f, text="New Password", font="comicsans 20", bg="ghoastwhite").grid()
        Label(f, text="Confirm Password",
              font="comicsans 20", bg="ghoastwhite").grid(row=1)
        global newpas
        newpas = StringVar()
        global newpas1
        newpas1 = StringVar()
        Entry(f, textvariable=newpas, font="comicsans 20").grid(row=0, column=1)
        Entry(f, textvariable=newpas1, font="comicsans 20").grid(row=1, column=1)
        Button(f, text="Change", font="comicsans 20",
               command=change).grid(row=2, column=1)
        Button(f, text="Back", font="comicsans 20",
               command=back1, padx=19).grid(row=3, column=1)
        new6.bind('<Escape>',lambda event:back1())
        new1.mainloop()


def back():
    new.destroy()
    main()


def forgot():
    root.destroy()
    global new
    new = Tk()
    new.attributes("-fullscreen", True)
    new.title("GTA")
    new.config(bg="ghostwhite")
    Frame(new, bg="ghoastwhite", height=250).pack()
    f = Frame(new, bg="white")
    f.pack()
    Label(f, text="What is your hobby?",
          font="comicsans 20", bg="ghoastwhite").pack()
    global forp
    forp = StringVar()
    Entry(f, textvariable=forp, font="comicsans 20").pack()
    Button(f, text="Submit", font="comicsans 20", command=submit).pack()
    Button(f, text="Back", font="comicsans 20", command=back, padx=13).pack()
    new.bind('<Escape>',lambda event:back())

    new.mainloop()


def back12():
    root.destroy()


def main():
    global root
    root = Tk()
    root.attributes('-fullscreen', True)
    root.config(bg="ghostwhite")
    root.title("GTA")
    Frame(root, height=250, bg="ghostwhite").pack()
    f3 = Frame(root, padx=54, pady=8, bg="ghostwhite")
    f3.pack()
    Label(f3, text="Username", font="comicsans 20", bg="ghostwhite").grid()
    Label(f3, text="Password", font="comicsans 20", bg="ghostwhite").grid(row=1)
    global use
    global pas
    global ro
    use = StringVar()
    pas = StringVar()
    ro = IntVar()
    Entry(f3, textvariable=use, font="comicsans 20").grid(row=0, column=1)
    Entry(f3, textvariable=pas, font="comicsans 20").grid(row=1, column=1)
    Checkbutton(f3, text="I'm not a robot.", bg="ghostwhite",
                variable=ro, font="comicsans 20").grid(row=2, column=1)
    Button(f3, text="Forgot Password", bg="ghostwhite", command=forgot,
           font="comicsans 20").grid(row=3, column=1)
    Button(f3, text="Login", bg="ghostwhite", command=login,
           font="comicsans 20", padx=70).grid(row=4, column=1)
    Button(f3, text="Exit", bg="ghostwhite", command=back12,
           font="comicsans 20", padx=80).grid(row=5, column=1)
    root.bind('<Escape>',lambda x:root.destroy())
    root.mainloop()
main()
# Made By Arpit Rangi
