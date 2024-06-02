import tkinter as tk
from tkinter import Label, messagebox, ttk


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="finalproject",
    password="angel",
    database="finalproject"
)

mycursor = db.cursor()
def signup_page(loginpage):

  def validate_login():
      username = username_entry.get()
      password = password_entry.get()

    #   mycursor.execute("SELECT * FROM user WHERE Username = %s AND Password = PASSWORD(%s)", (username, password))

    #   result = mycursor.fetchone()
    #   if result:
    #       messagebox.showinfo("Login Successful", "Welcome, %s!" % username)
    #       parent.destroy()
    #       mainpage()
    #   else:
    #       messagebox.showerror("Login Failed", "Invalid username or password")
  
  parent = tk.Tk()
  parent.title("Signup Form")
  parent.geometry("700x300")

  var = tk.StringVar()
  typeofcustomer = ttk.Combobox(parent, state="readonly", values=["Customer", "Owner"], textvariable=var)
  
  name_label = tk.Label(parent, text="Name:")
  name_label.pack()

  name_entry = tk.Entry(parent)
  name_entry.pack()

  age_label = tk.Label(parent, text="Age:")
  age_label.pack()

#   typeofcustomer.grid(row=0, column=3, columnspan=2)

  username_entry = tk.Entry(parent)
  username_entry.pack()

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

  # parent.mainloop()