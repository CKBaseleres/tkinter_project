import tkinter as tk
from tkinter import ttk,messagebox,Menu
import sqlite3 as seq

con = seq.connect("project.db")
cur = con.cursor()

def addFaci():
    def newFaci():
        if (namee.get() == "" and quantityy.get() == "" and statuss.get()):
            messagebox.showinfo("Error","Please insert an input on all fields.")
        elif(quantityy.get().isdigit() == False):
            messagebox.showinfo("Error","Please insert a digit value in quantity.")
        else:
            cur.execute('SELECT * from facilities where name=(?)',(namee.get(),))
            result = cur.fetchone()
            if(result != None):
                messagebox.showinfo("Error","{} already exists in records.".format(namee.get()))
                namee.delete(0,'end')
                quantityy.delete(0,'end')
                statuss.delete(0,'end')
            else:
                cur.execute('INSERT INTO facilities(name,quantity,status) VALUES (?,?,?)',(namee.get(),quantityy.get(),statuss.get()))
                con.commit()
                tk.messagebox.showinfo("Success", "Successfully added {}.".format(namee.get()))
                namee.delete(0,'end')
                quantityy.delete(0,'end')
                statuss.delete(0,'end')
    clearWidgets()
    window.minsize(width=300,height=125)
    window.geometry("300x125")
    window.title("Add Facility")
    # Labels
    name = ttk.Label(window,text="Facility Name:",padding=3,background="#e8b614",font=("",12))
    name.grid(column=0,row=0)
    quantity = ttk.Label(window,text="Quantity:",padding=3,background="#e8b614",font=("",12))
    quantity.grid(column=0,row=1)   
    status = ttk.Label(window, text="Status: ",padding=3,background="#e8b614",font=("",12))
    status.grid(column=0,row=2)  
    # Entries
    namee = ttk.Entry(window)
    namee.grid(column=1,row=0)
    quantityy = ttk.Entry(window)
    quantityy.grid(column=1,row=1) 
    c =['Active','Inactive']
    statuss= ttk.Combobox(window,values=c)
    statuss.grid(column=1,row=2) 
    # Button
    b = ttk.Style()
    b.configure('theme.TButton',background="#e8b614")
    add = ttk.Button(window, text="Add",padding=3,command=newFaci,style="theme.TButton")
    add.grid(column=1,row=3)


def manFaci():
    clearWidgets()
    window.minsize(width=325,height=125)
    window.geometry("325x125")
    window.title("Manage Facilities")
    def getData():
        c=[]
        cur.execute("SELECT * FROM facilities")
        result = cur.fetchall()
        for row in result:
            c.append(row[1])
            c.sort()
        global facilities
        facilities = ttk.Combobox(window,values=c)
        facilities.grid(column=1,row=0)
    
    def searchFac():
        cur.execute('SELECT * FROM facilities WHERE name=(?)',(facilities.get(),))
        result=cur.fetchone()
        namee.delete(0, 'end')
        namee.insert(0,result[1])
        quantityy.delete(0, 'end')
        quantityy.insert(0,result[2])
        statuss.delete(0,'end')
        statuss.insert(0,result[3])

    def updateFac():
        if (namee.get() == "" and quantityy.get() == "" and statuss.get()):
            messagebox.showinfo("Error","Please insert an input on all fields.")
        elif(quantityy.get().isdigit() == False):
            messagebox.showinfo("Error","Please insert a digit value in quantity.")
        else:
            cur.execute('UPDATE facilities SET name=(?),quantity=(?),status=(?) WHERE name=(?)',(namee.get(),quantityy.get(),statuss.get(),facilities.get()))
            con.commit()
            messagebox.showinfo("Message","{} has been updated!!".format(facilities.get()))
            namee.delete(0, 'end')
            quantityy.delete(0, 'end')
            statuss.delete(0,'end')
            getData()
       

    # LABELS
    getData()
    name = ttk.Label(window,text="Name:",padding=3,background="#e8b614",font=("",12))
    name.grid(column=0,row=1)
    quantity = ttk.Label(window,text="Quantity:",padding=3,background="#e8b614",font=("",12))
    quantity.grid(column=0,row=2)  
    status = ttk.Label(window, text="Status: ",padding=3,background="#e8b614",font=("",12))
    status.grid(column=0,row=3) 
    # ENTRIES
    namee = ttk.Entry(window)
    namee.grid(column=1,row=1)
    quantityy = ttk.Entry(window)
    quantityy.grid(column=1,row=2)
    statuss= ttk.Combobox(window,values=["Available","Not Available"])
    statuss.grid(column=1,row=3) 
    # BUTTONs
    b = ttk.Style()
    b.configure('theme.TButton',background="#e8b614")
    update = ttk.Button(window,text="Update",padding=3,command=updateFac,style="theme.TButton")
    update.grid(column=2,row=1)
    search = ttk.Button(window,text="Search", padding=3,command=searchFac,style="theme.TButton")
    search.grid(column=2,row=0)

def manEquip():
    clearWidgets()
    window.minsize(width=325,height=100)
    window.geometry("325x100")
    window.title("Manage Equipments")
    def searchEquip():
        cur.execute('SELECT * FROM equipment WHERE name=(?)',(equipments.get(),))
        result=cur.fetchone()
        namee.delete(0, 'end')
        namee.insert(0,result[1])
        quantityy.delete(0, 'end')
        quantityy.insert(0,result[2])

    def updateEquip():
        if (namee.get() == "" and quantityy.get() == ""):
            messagebox.showinfo("Error","Please insert an input on all fields.")
        elif(quantityy.get().isdigit() == False):
            messagebox.showinfo("Error","Please insert a digit value in quantity.")
        else:
            cur.execute('UPDATE equipment SET name=(?),quantity=(?) WHERE name=(?)',(namee.get(),quantityy.get(),equipments.get()))
            con.commit()
            messagebox.showinfo("Message","{} has been updated!".format(equipments.get()))
            namee.delete(0, 'end')
            quantityy.delete(0, 'end')
            getData()

    def delEquip():
        cur.execute('DELETE FROM equipment WHERE name=(?)',(equipments.get(),))
        con.commit()
        messagebox.showinfo("Message","{} has been deleted".format(equipments.get()))
        namee.delete(0, 'end')
        quantityy.delete(0, 'end')
        getData()
     
    def getData():
        c=[]
        cur.execute("SELECT * FROM equipment")
        result = cur.fetchall()
        for row in result:
            c.append(row[1])
            c.sort()
        global equipments
        equipments = ttk.Combobox(window,values=c)
        equipments.grid(column=1,row=0)

    getData()
     # LABELS 
    name = ttk.Label(window,text="Name:",padding=3,background="#e8b614",font=("",12))
    name.grid(column=0,row=1)
    quantity = ttk.Label(window,text="Quantity:",padding=3,background="#e8b614",font=("",12))
    quantity.grid(column=0,row=2)   
    # ENTRIES
    namee = ttk.Entry(window)
    namee.grid(column=1,row=1)
    quantityy = ttk.Entry(window)
    quantityy.grid(column=1,row=2) 
    # BUTTONs
    b = ttk.Style()
    b.configure('theme.TButton',background="#e8b614")
    update = ttk.Button(window,text="Update",padding=3,command=updateEquip,style="theme.TButton")
    update.grid(column=2,row=1)
    delete = ttk.Button(window,text="Delete", padding=3,command=delEquip,style="theme.TButton")
    delete.grid(column=2,row=2)
    search = ttk.Button(window,text="Search",padding=3,command=searchEquip,style="theme.TButton")
    search.grid(column=2,row=0)


def addEquip():
    def newEquip():
        if (namee.get() == "" and quantityy.get() == ""):
            messagebox.showinfo("Error","Please insert an input on all fields.")
        elif(quantityy.get().isdigit() == False):
            messagebox.showinfo("Error","Please insert a digit value in quantity.")
        else:
            cur.execute("select * from equipment where name=(?)",(namee.get(),))
            result = cur.fetchone()
            if(result != None):
                messagebox.showinfo("Error","{} already exists in records.".format(namee.get()))
                namee.delete(0,'end')
                quantityy.delete(0,'end')
            else:
                cur.execute('INSERT INTO equipment(name,quantity) VALUES (?,?)',(namee.get(),quantityy.get()))
                con.commit()
                tk.messagebox.showinfo("Success", "Successfully added {}.".format(namee.get()))
                namee.delete(0,'end')
                quantityy.delete(0,'end')
    clearWidgets()
    window.title("Add Equipment")
    window.minsize(width=300,height=100)
    window.geometry("300x100")
    # Labels
    name = ttk.Label(window,text="Equipment Name:",padding=3,background="#e8b614",font=("",12))
    name.grid(column=0,row=0)
    quantity = ttk.Label(window,text="Quantity:",padding=3,background="#e8b614",font=("",12))
    quantity.grid(column=0,row=1)    
    # Entries
    namee = ttk.Entry(window)
    namee.grid(column=1,row=0)
    quantityy = ttk.Entry(window)
    quantityy.grid(column=1,row=1) 
    # Button
    b = ttk.Style()
    b.configure('theme.TButton',background="#e8b614")
    add = ttk.Button(window, text="Add",padding=3,command=newEquip, style='theme.TButton')
    add.grid(column=1,row=2)

# function to clear widgets in the window
def clearWidgets():
    list = window.grid_slaves()
    for l in list:
        l.destroy()
    list = window.pack_slaves()
    for i in list:
        i.destroy()

def login():
    cur.execute("SELECT * FROM users where username=(?) and pass=(?)",(entUser.get(),entPass.get()))
    result = cur.fetchone()
    if result != None:
        name= result[3]
        lblUser.destroy()
        lblPass.destroy()
        entUser.destroy()
        entPass.destroy()
        btnLogin.destroy()
        fileMenu.add_command(label="Log Out",command=main)
        equipMenu=Menu(menubar,tearoff=0)
        equipMenu.add_command(label="Add Equipment", command=addEquip)
        equipMenu.add_command(label="Manage Equipments", command=manEquip)
        menubar.add_cascade(label="Equipment", menu=equipMenu)
        facMenu=Menu(menubar,tearoff=0)
        facMenu.add_command(label="Add Facility", command=addFaci)
        facMenu.add_command(label="Manage Facilities", command=manFaci)
        menubar.add_cascade(label="Facility", menu=facMenu)
        lblres = ttk.Label(window, text="Welcome Sir {}!".format(name),font=("Helvetica",15),background="#e8b614")
        lblres.pack()
    else:
        tk.messagebox.showinfo("Error", "Invalid username or password.")

def signup():
    def newUser():
        if(nname.get() == "" and passwordd.get()== "" and unamee.get()==""):
            tk.messagebox.showinfo("Error", "Please input on all fields.")
            nname.delete(0,'end')
            passwordd.delete(0,'end')
            unamee.delete(0,'end')
        else:
            cur.execute("INSERT INTO users(username,pass,name) VALUES (?,?,?)",(unamee.get(),passwordd.get(),nname.get()))
            con.commit()
            tk.messagebox.showinfo("Success", "Welcome {}.".format(nname.get()))
            nname.delete(0,'end')
            passwordd.delete(0,'end')
            unamee.delete(0,'end')
            main()

    clearWidgets()
    window.minsize(width=325,height=125)
    window.geometry("325x125")
    window.title("Sign Up")
     # LABELS 
    uname = ttk.Label(window,text="Username:",padding=3,background="#e8b614",font=("",12))
    uname.grid(column=0,row=0)
    password = ttk.Label(window,text="Password:",padding=3,background="#e8b614",font=("",12))
    password.grid(column=0,row=1)
    name = ttk.Label(window,text="Name:",padding=3,background="#e8b614",font=("",12))
    name.grid(column=0,row=2)
    # ENTRIES
    unamee = ttk.Entry(window)
    unamee.grid(column=1,row=0)
    passwordd = ttk.Entry(window,show="*")
    passwordd.grid(column=1,row=1)
    nname = ttk.Entry(window)
    nname.grid(column=1,row=2)
    # BUTTONs
    b = ttk.Style()
    b.configure('theme.TButton',background="#e8b614")
    signupp = ttk.Button(window,text="Sign Up",padding=3,style="theme.TButton",command=newUser)
    signupp.grid(column=1,row=3)

def main():
    clearWidgets()
    window.minsize(width=450,height=210)
    window.title("Equipment and Facility Management System")
    global btnLogin,fileMenu,menubar,entPass,lblPass,entUser,lblUser
    title = ttk.Label(window,text="Welcome to Equipment and Facility",font=("helvetica",20),background="#e8b614")
    title.pack()
    title3 = ttk.Label(window,text="Management System",font=("helvetica",20),background="#e8b614")
    title3.pack()
    lblUser = ttk.Label(window,text="Username:",font=("Helvetica",10),background="#e8b614")
    lblUser.pack()
    entUser= ttk.Entry(window)
    entUser.pack()
    lblPass = ttk.Label(window,text="Password:",font=("helvetica",10),background="#e8b614")
    lblPass.pack()
    entPass = ttk.Entry(window,show='*')
    entPass.pack()
    b = ttk.Style()
    b.configure('theme.TButton',background="#e8b614")
    btnLogin = ttk.Button(window, text="Login",padding=3, style='theme.TButton',command=login)
    btnLogin.pack()
    emptymenu=Menu(window)
    window.config(menu=emptymenu)
    menubar=tk.Menu(window)
    fileMenu = tk.Menu(window)
    fileMenu = Menu(menubar,tearoff=0)
    fileMenu.add_command(label="New Admin",command=signup)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=fileMenu,state="active")
    window.config(menu=menubar)
window=tk.Tk()
window.title("Equipment and Facility Management")
window.configure(background="#e8b614")
main()
window.mainloop()