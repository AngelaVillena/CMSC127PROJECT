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


root = tk.Tk()

root.geometry("700x500")
root.title("CMSC 127 PROJECT - FOOD AND FOOD ESTABLISHMENT REVIEWS")

label = tk.Label(root, text="Welcome")
label.pack()


# diapslya the buttons
def mainpage():
    root.destroy()
    main_window = tk.Tk()
    
    main_window.geometry("700x500")
    main_window.title("Main Window")
    def add_foodestablishment():
    
      def submit_data():
          business_id = businessid.get()
          business_name = businessname.get()
          business_address = address.get()
          
          # INSERT QUERY FOR FOOD ESTABLISHMENT TABLE
          sql = "INSERT INTO FOOD_ESTABLISHMENT (Business_id, Name, Address) VALUES (%s, %s, %s)"
          val = (business_id, business_name, business_address)
          mycursor.execute(sql, val)
          db.commit()
          print("Record inserted successfully!")
          messagebox.showinfo("Success", "Food establishment has been recorded successfully!")
          new_window.destroy()
        
      new_window = tk.Toplevel(main_window)
      new_window.geometry("400x300")
      new_window.title("Add food establishment")
      
      labels = ['Business id:', 'Business name:', 'Address:']
      for i in range(3):
          tk.Label(new_window, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
      
      businessid = tk.Entry(new_window, width=40, font=('Arial', 14))
      businessid.grid(row=0, column=1, columnspan=2)

      businessname = tk.Entry(new_window, width=40, font=('Arial', 14))
      businessname.grid(row=1, column=1, columnspan=2)

      address = tk.Entry(new_window, width=40, font=('Arial', 14))
      address.grid(row=2, column=1, columnspan=2)

      submit = tk.Button(new_window, text='Submit Now', command=submit_data)
      submit.grid(row=3, column=2)  

    AddFoodEstablishment = tk.Button(main_window, text='Add a new food establishment', command=add_foodestablishment)
    AddFoodEstablishment.pack(pady=20)

    def add_fooditem():
    
      def submit_data():
          food_id = foodid.get()
          food_name = foodname.get()
          food_price = price.get()
          type_of_food = typeoffood.get()
          food_description = description.get()
          food_businessid =businessid.get()
          
          # INSERT QUERY FOR FOOD ESTABLISHMENT TABLE
          sql = "INSERT INTO FOOD_ITEM (Food_id, Name, Price, Type_of_food, Description, Business_id) VALUES (%s, %s, %s, %s,%s,%s)"
          val = (food_id, food_name, food_price,type_of_food,food_description,food_businessid)
          mycursor.execute(sql, val)
          db.commit()
          print("Record inserted successfully!")
          messagebox.showinfo("Success", "Food item has been recorded successfully!")
          fooditem.destroy()
      fooditem = tk.Toplevel(main_window)
      fooditem.geometry("400x300")
      fooditem.title("Add new food item")
      
      labels = ['Food id:', 'Food name:', 'Price:','Type of food:', 'Description','Business id:']
      for i in range(6):
          tk.Label(fooditem, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
      
      foodid = tk.Entry(fooditem, width=40, font=('Arial', 14))
      foodid.grid(row=0, column=1, columnspan=2)

      foodname = tk.Entry(fooditem, width=40, font=('Arial', 14))
      foodname.grid(row=1, column=1, columnspan=2)

      price = tk.Entry(fooditem, width=40, font=('Arial', 14))
      price.grid(row=2, column=1, columnspan=2)

      typeoffood = tk.Entry(fooditem, width=40, font=('Arial', 14))
      typeoffood.grid(row=3, column=1, columnspan=2)

      description = tk.Entry(fooditem, width=40, font=('Arial', 14))
      description.grid(row=4, column=1, columnspan=2)

      businessid = tk.Entry(fooditem, width=40, font=('Arial', 14))
      businessid.grid(row=5, column=1, columnspan=2)

      submit = tk.Button(fooditem, text='Submit Now', command=submit_data)
      submit.grid(row=7, column=2)  



    AddFoodItem = tk.Button(main_window, text='Add a new food item', command=add_fooditem)
    AddFoodItem.pack(pady=20)


    def add_foodreview():
      def submit_data():
          review_no = reviewno.get()
          review_description = description.get()
          review_rating = food_rating.get()
          review_businessid = businessid.get()
          review_foodid = foodid.get()
          review_userid = userid.get() 
      
          
          # INSERT QUERY FOR FOOD ESTABLISHMENT TABLE
          sql = "INSERT INTO REVIEW (Review_no, Description, Rating, Time, Date, Business_id,Food_id,User_id) VALUES (%s, %s, %s, curtime(), curdate(), %s,%s,%s)"
          val = (review_no, review_description, review_rating,review_businessid,review_foodid, review_userid)
          mycursor.execute(sql, val)
          db.commit()
          print("Record inserted successfully!")
          messagebox.showinfo("Success", "Review has been recorded successfully!")
          foodreview.destroy()
      foodreview = tk.Toplevel(main_window)
      foodreview.geometry("400x300")
      foodreview.title("Add new food item")
      
      labels = ['Review no:', 'Description:', 'Rating:','Business id:','Food id:','User id:']
      for i in range(6):
          tk.Label(foodreview, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
      
      reviewno = tk.Entry(foodreview, width=40, font=('Arial', 14))
      reviewno.grid(row=0, column=1, columnspan=2)

      description = tk.Entry(foodreview, width=40, font=('Arial', 14))
      description.grid(row=1, column=1, columnspan=2)

      food_rating = tk.Scale(foodreview, from_=0, to=10, orient="horizontal", length=200)
      food_rating.grid(row=2, column=1, columnspan=2)

      businessid = tk.Entry(foodreview, width=40, font=('Arial', 14))
      businessid.grid(row=3, column=1, columnspan=2)

      foodid = tk.Entry(foodreview, width=40, font=('Arial', 14))
      foodid.grid(row=4, column=1, columnspan=2)

      # if nakologged in then user id input is not necessary
      userid = tk.Entry(foodreview, width=40, font=('Arial', 14))
      userid.grid(row=5, column=1, columnspan=2)
      submit = tk.Button(foodreview, text='Submit Now', command=submit_data)
      submit.grid(row=6, column=2)  



    AddReview = tk.Button(main_window, text='Add a new food review', command=add_foodreview)
    AddReview.pack(pady=20)



def login_validation():
    print('here')
   
    userid = username_entry.get()
    password = password_entry.get()

    sql = "SELECT password FROM user WHERE User_id = %s and Password = %s"
    val = (userid,password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    
    # If the user exists and the password matches, show a success message
    if result and result[0] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + userid + "!")
        mainpage()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# user log in apge
username_label = tk.Label(root, text="Userid:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # Show asterisks for password
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login_validation)
login_button.pack(pady=20)









root.mainloop()









