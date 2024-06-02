import tkinter as tk
from tkinter import messagebox


import mysql.connector
import sign_up

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hershey",
    database="finalproject"
)

mycursor = db.cursor()
def login_page(mainpage):

  def validate_login():
      username = username_entry.get()
      password = password_entry.get()

      mycursor.execute("SELECT * FROM user WHERE Username = %s AND Password = PASSWORD(%s)", (username, password))

      result = mycursor.fetchone()
      if result:
          messagebox.showinfo("Login Successful", "Welcome, %s!" % username)
          parent.destroy()
          mainpage()
      else:
          messagebox.showerror("Login Failed", "Invalid username or password")
    
 
  parent = tk.Tk()
  parent.title("Login Form")
  parent.geometry("700x300")
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

  signup_button = tk.Button(parent, text="Signup", command= lambda: sign_up.signup_page(login_page))
  signup_button.pack()

  parent.mainloop()