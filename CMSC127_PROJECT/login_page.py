import tkinter as tk
from tkinter import messagebox


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="angel",
    database="finalproject"
)

mycursor = db.cursor()
def login_page(mainpage):

  def validate_login():
      name = username_entry.get()
      password = password_entry.get()

      mycursor.execute("SELECT * FROM user WHERE Name = %s AND Password = %s", (name, password))

      result = mycursor.fetchone()
      if result:
          messagebox.showinfo("Login Successful", f"Welcome, {name}!")
      else:
          messagebox.showerror("Login Failed", "Invalid username or password")
      parent.destroy()
      mainpage()
    
 
  parent = tk.Tk()
  parent.title("Login Form")
  parent.geometry("300x200")
  username_label = tk.Label(parent, text="Username:")
  username_label.pack()

  username_entry = tk.Entry(parent)
  username_entry.pack()


  password_label = tk.Label(parent, text="Password:")
  password_label.pack()

  password_entry = tk.Entry(parent, show="*") 
  password_entry.pack()


  login_button = tk.Button(parent, text="Login", command=validate_login)
  login_button.pack()

  parent.mainloop()