import tkinter as tk
from tkinter import Label, messagebox, ttk

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hershey",
    database="finalproject"
)

mycursor = db.cursor()
def signup_page(loginpage):

  def validate_signup():
      username = username_entry.get()
      password = password_entry.get()
      name = name_entry.get()
      age = age_entry.get()
      role = role_label_entry.get()

      if len(username) == 0 or len(password) == 0 or len(name) == 0 or len(age) == 0 or len(role) == 0:
        messagebox.showerror("Sign Up Invalid", "Please fill up all the fields")
      else:
        sql = "INSERT INTO USER(Name, Age, Password, Username, Role) values(%s, %s, password(%s), %s, %s)"
        val = (name, age, password, username, role)
        mycursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Success!", "Sign Up Successful!")
        print("successfully added")
        signup.destroy()
        loginpage()
  
  signup = tk.Tk()
  signup.title("Signup Form")
  signup.geometry("700x300")
  
  name_label = tk.Label(signup, text="Name:")
  name_label.pack()

  name_entry = tk.Entry(signup)
  name_entry.pack()

  age_label = tk.Label(signup, text="Age:")
  age_label.pack()

  age_entry = tk.Entry(signup)
  age_entry.pack()

  role_label = tk.Label(signup, text="Role:")
  role_label.pack()

  role_label_entry = ttk.Combobox(signup, state="readonly", values=["Customer", "Owner"])
  role_label_entry.pack()

  username_label = tk.Label(signup, text="Username:")
  username_label.pack()

  username_entry = tk.Entry(signup)
  username_entry.pack()

  password_label = tk.Label(signup, text="Password:")
  password_label.pack()

  password_entry = tk.Entry(signup, show="*") 
  password_entry.pack()

  login_button = tk.Button(signup, text="Sign Up", command= validate_signup)
  login_button.pack()

  # parent.mainloop()