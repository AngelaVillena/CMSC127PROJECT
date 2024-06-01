import tkinter as tk
from tkinter import messagebox, ttk

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hershey",
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
    main_window.title("FINAL PROJECT")
    
       
    def add_foodestablishment():
      def edit_foodestablishment():
         def edit_submit_data():
            editid = editbusinessid.get()
            editbusiness_name = editbusinessname.get()
            editbusiness_address = editbusinessaddress.get()
            sql = "UPDATE FOOD_ESTABLISHMENT SET Name = %s, Address = %s where Business_id = %s"
            val = ( editbusiness_name, editbusiness_address, editid)
            mycursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Success", "Food establishment has been edited successfully!")
            edit1.destroy()


         edit1 = tk.Toplevel(main_window)
         edit1.geometry("700x300")
         edit1.title("Edit food establishment")
         labels = ['Enter business id:', 'Enter new business name:', 'Enter new business address:']
         for i in range(3):
            tk.Label(edit1, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
      
         editbusinessid = tk.Entry(edit1, width=40, font=('Arial', 14))
         editbusinessid.grid(row=0, column=1, columnspan=2)

    
         editbusinessname = tk.Entry(edit1, width=40, font=('Arial', 14))
         editbusinessname.grid(row=1, column=1, columnspan=2)

        
        # select * from FOOD ESTABLISHMENT where business id = %s
         editbusinessaddress = tk.Entry(edit1, width=40, font=('Arial', 14))
         editbusinessaddress.grid(row=2, column=1, columnspan=2)
         
         submit = tk.Button(edit1, text='Submit', command=edit_submit_data)
         submit.grid(row=3, column=1)  



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
      new_window.geometry("700x300")
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
      submit.grid(row=3, column=1)  
# add implementation for edit button
      edit = tk.Button(new_window, text='Edit', command=edit_foodestablishment)
      edit.grid(row=3, column=2)  



    AddFoodEstablishment = tk.Button(main_window, text='Add a new food establishment', command=add_foodestablishment)
    AddFoodEstablishment.pack(pady=20)

    def add_fooditem():
 
      def submit_data():
        
          food_name = foodname.get()
          food_price = price.get()
          type_of_food = typeoffood_list.get()
          food_description = description.get()
          food_businessid =businessid.get()
          
          # INSERT QUERY FOR FOOD ESTABLISHMENT TABLE
          sql = "INSERT INTO FOOD_ITEM (Name, Price, Type_of_food, Description, Business_id) VALUES ( %s, %s, %s,%s,%s)"
          val = ( food_name, food_price,type_of_food,food_description,food_businessid)
          mycursor.execute(sql, val)
          db.commit()
          print("Record inserted successfully!")
          messagebox.showinfo("Success", "Food item has been recorded successfully!")
          fooditem.destroy()
      fooditem = tk.Toplevel(main_window)
      fooditem.geometry("700x300")
      fooditem.title("Add new food item")
      typeoffood_list = ttk.Combobox(fooditem,state="readonly",
        values=["Appetizer", "Entree/ Main Dish", "Sides", "Dessert"]
      )

      
   
      
      labels = ['Food name:', 'Price:','Type of food:', 'Description','Business id:']
      for i in range(5):
          tk.Label(fooditem, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
      

      foodname = tk.Entry(fooditem, width=40, font=('Arial', 14))
      foodname.grid(row=0, column=1, columnspan=2)

      price = tk.Entry(fooditem, width=40, font=('Arial', 14))
      price.grid(row=1, column=1, columnspan=2)

      typeoffood_list.grid(row=2, column=1,columnspan=2)

      description = tk.Entry(fooditem, width=40, font=('Arial', 14))
      description.grid(row=3, column=1, columnspan=2)

      businessid = tk.Entry(fooditem, width=40, font=('Arial', 14))
      businessid.grid(row=4, column=1, columnspan=2)

      submit = tk.Button(fooditem, text='Submit Now', command=submit_data)
      submit.grid(row=5, column=1)  

      edit_fooditem = tk.Button(fooditem, text='Edit')
      edit_fooditem.grid(row=5, column=2)  

      delete_fooditem = tk.Button(fooditem, text='Delete')
      delete_fooditem.grid(row=5, column=3)  



    AddFoodItem = tk.Button(main_window, text='Add a new food item', command=add_fooditem)
    AddFoodItem.pack(pady=20)

    def viewFoodReviews():
          def add_foodreview():
                def submit_data():
                    review_description = description.get()
                    review_rating = food_rating.get()
                    review_businessid = businessid.get()
                    review_foodid = foodid.get()
                    review_userid = userid.get() 
                
                    sql = "INSERT INTO REVIEW (Description, Rating, Time, Date, Business_id,Food_id,User_id) VALUES (%s, %s, curtime(), curdate(), %s,%s,%s)"
                    val = (review_description, review_rating,review_businessid,review_foodid, review_userid)
                    mycursor.execute(sql, val)
                    db.commit()
                    print("Record inserted successfully!")
                    messagebox.showinfo("Success", "Review has been recorded successfully!")
                    foodreview.destroy()
                foodreview = tk.Toplevel(main_window)
                foodreview.geometry("700x300")
                foodreview.title("Add new food review")
                
                labels = ['Description:', 'Rating:','Business id:','Food id:','User id:']
                for i in range(5):
                    tk.Label(foodreview, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)


                description = tk.Entry(foodreview, width=40, font=('Arial', 14))
                description.grid(row=0, column=1, columnspan=2)

                food_rating = tk.Scale(foodreview, from_=0, to=10, orient="horizontal", length=200)
                food_rating.grid(row=1, column=1, columnspan=2)

                businessid = tk.Entry(foodreview, width=40, font=('Arial', 14))
                businessid.grid(row=2, column=1, columnspan=2)

                foodid = tk.Entry(foodreview, width=40, font=('Arial', 14))
                foodid.grid(row=3, column=1, columnspan=2)

                userid = tk.Entry(foodreview, width=40, font=('Arial', 14))
                userid.grid(row=4, column=1, columnspan=2)
                submit = tk.Button(foodreview, text='Submit Now', command=submit_data)
                submit.grid(row=5, column=1)  
          def edit_foodreview(reviews, row, column):
                def edit_submit_data():
                    reviewno = reviews[row][column]
                    newdescription = editDescription.get()
                    newrating = edit_rating.get()
                   
                    sql = "UPDATE REVIEW SET Description = %s, Rating = %s where Review_no ="+ str(reviewno)
                    val = (newdescription, newrating)
                    mycursor.execute(sql, val)
                    db.commit()
                    messagebox.showinfo("Success", "Food review has been edited successfully!")
                    edit1.destroy()
          
                edit1 = tk.Toplevel(main_window)
                edit1.geometry("700x300")
                edit1.title("Edit food review")
                labels = ['Enter Description:', 'Rating:']
                for i in range(2):
                    tk.Label(edit1, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
            
                editDescription = tk.Entry(edit1, width=40, font=('Arial', 14))
                editDescription.grid(row=0, column=1, columnspan=2)

            
                edit_rating = tk.Scale(edit1, from_=0, to=10, orient="horizontal", length=200)
                edit_rating.grid(row=1, column=1, columnspan=2)
                
                submit = tk.Button(edit1, text='Edit', command=edit_submit_data)
                submit.grid(row=2, column=1, pady=10) 
          allFoodReviews = tk.Toplevel(main_window)
          allFoodReviews.geometry("700x700")
          allFoodReviews.title("Food reviews")

          
          sql = "SELECT * FROM REVIEW"
          mycursor.execute(sql)
          reviews = mycursor.fetchall()

          numofrows = len(reviews)
          for i, review in enumerate(reviews):
                for j, value in enumerate(review):
                    tk.Label(allFoodReviews, text=value).grid(row=i, column=j, padx=10, pady=10) 
                    tk.Button(allFoodReviews, text='Edit', command= lambda row=i, column=0: edit_foodreview(reviews, row, column)).grid(row=i, column=9)
          add_foodreview = tk.Button(allFoodReviews, text='Add new food review',command=add_foodreview)
          add_foodreview.grid(row=numofrows, column=1, pady=10) 

    def viewFoodEstablishments():
        def delete_foodestablishment(items, row, col):
            businessid = items[row][col]
            sql = "DELETE FROM FOOD_ESTABLISHMENT where Business_id =" + str(businessid)
            mycursor.execute(sql)
            db.commit()
            messagebox.showinfo("Success", "Food establishment has been DELETED!")

        def edit_foodestablishment():
            def edit_submit_data():
                editid = editbusinessid.get()
                editbusiness_name = editbusinessname.get()
                editbusiness_address = editbusinessaddress.get()
                sql = "UPDATE FOOD_ESTABLISHMENT SET Name = %s, Address = %s where Business_id = %s"
                val = ( editbusiness_name, editbusiness_address, editid)
                mycursor.execute(sql, val)
                db.commit()
                messagebox.showinfo("Success", "Food establishment has been edited successfully!")
                edit1.destroy()


            edit1 = tk.Toplevel(main_window)
            edit1.geometry("700x300")
            edit1.title("Edit food establishment")
            labels = ['Enter business id:', 'Enter new business name:', 'Enter new business address:']
            for i in range(3):
                tk.Label(edit1, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
        
            editbusinessid = tk.Entry(edit1, width=40, font=('Arial', 14))
            editbusinessid.grid(row=0, column=1, columnspan=2)

        
            editbusinessname = tk.Entry(edit1, width=40, font=('Arial', 14))
            editbusinessname.grid(row=1, column=1, columnspan=2)

            
            # select * from FOOD ESTABLISHMENT where business id = %s
            editbusinessaddress = tk.Entry(edit1, width=40, font=('Arial', 14))
            editbusinessaddress.grid(row=2, column=1, columnspan=2)
            
            submit = tk.Button(edit1, text='Submit', command=edit_submit_data)
            submit.grid(row=3, column=1)  

        def viewFoodItems(items, row, col):
            def viewByType(businessid):
                for label in allFoodItems.grid_slaves():  #deletes the current table
                    if int(label.grid_info()["row"]) > 0:
                        label.grid_forget()

                sql = "SELECT * FROM food_item WHERE Business_id = " + str(businessid) + " AND Type_of_food = '%s'" % str(var.get())
                mycursor.execute(sql)
                items = mycursor.fetchall()
                for i, item in enumerate(items):
                    for j, value in enumerate(item):
                        item2 = tk.Label(allFoodItems, text=value)
                        item2.grid(row=i+1, column=j, padx=10, pady=10)

            def viewByPrice(businessid):
                for label in allFoodItems.grid_slaves(): #deletes the current table
                    if int(label.grid_info()["row"]) > 0:
                        label.grid_forget()
                
                sql = "SELECT * FROM food_item WHERE Business_id = " + str(businessid) + " ORDER BY Price"
                mycursor.execute(sql)
                items = mycursor.fetchall()

                for i, item in enumerate(items):
                    for j, value in enumerate(item):
                        item2 = tk.Label(allFoodItems, text=value)
                        item2.grid(row=i+1, column=j, padx=10, pady=10)

            allFoodItems = tk.Toplevel(main_window)
            allFoodItems.geometry("700x700")
            allFoodItems.title("Food Items")

            tk.Label(allFoodItems, text = "Sort by: ").grid(row=0, column=0, padx=10, pady=10)
            
            businessid = items[row][col]

            sql = "SELECT * FROM food_item WHERE Business_id = " + str(businessid)
            mycursor.execute(sql)
            items = mycursor.fetchall()
            numofrows = len(items)
            for i, item in enumerate(items):
                for j, value in enumerate(item):
                    item1 = tk.Label(allFoodItems, text=value)
                    item1.grid(row=i+1, column=j, padx=10, pady=10) 
            AddFoodItem = tk.Button(allFoodItems, text='Add a new food item', command=add_fooditem)
            AddFoodItem.grid(row=numofrows+1, column=1, pady=10) 
           
            
            tk.Button(allFoodItems, text='Price', command= lambda: viewByPrice(businessid)).grid(row=0, column=1, padx=10, pady=10)
            tk.Label(allFoodItems, text = "Food Type: ").grid(row=0, column=2, padx=10, pady=10)
            var = tk.StringVar()
            typeoffood = ttk.Combobox(allFoodItems, textvariable = var)
            typeoffood['values'] = ["Appetizer", "Entree/ Main Dish", "Sides", "Dessert"]
            typeoffood['state'] = 'readonly'
            typeoffood.grid(row=0, column=3, columnspan=2)
            
            tk.Button(allFoodItems, text='OK', command= lambda: var.trace('w', viewByType(businessid))).grid(row=0, column=5, padx=5, pady=5)

        allFoodEstablishments = tk.Toplevel(main_window)
        allFoodEstablishments.geometry("800x800")
        allFoodEstablishments.title("Food Establishments")
   

        sql = "SELECT * FROM FOOD_ESTABLISHMENT"
        mycursor.execute(sql)
        establishments = mycursor.fetchall()
        for i, establishment in enumerate(establishments):
            for j, value in enumerate(establishment):
                tk.Label(allFoodEstablishments, text=value).grid(row=i, column=j, padx=10, pady=10) 
            
                edit_foodEstablishment = tk.Button(allFoodEstablishments, text='Edit', command=edit_foodestablishment)
                edit_foodEstablishment.grid(row=i, column=9, padx=10, pady=10)  

                view_foodEstablishment = tk.Button(allFoodEstablishments, text='View all food items', command= lambda row=i, column=0: viewFoodItems(establishments, row, column))
                view_foodEstablishment.grid(row=i, column=10, padx=10) 

                delete_foodEstablishment = tk.Button(allFoodEstablishments, text='Delete', bg='red', fg='white', command= lambda row=i, column=0: delete_foodestablishment(establishments, row, column))
                delete_foodEstablishment.grid(row=i, column=11) 
                
                view_foodEstablishment.grid(row=i, column=10) 

                view_foodEstablishment = tk.Button(allFoodEstablishments, text='View all food reviews',)
                view_foodEstablishment.grid(row=i, column=11, padx=10, pady=10) 
       
       
    def add_foodreview():
      def submit_data():

          review_description = description.get()
          review_rating = food_rating.get()
          review_businessid = businessid.get()
          review_foodid = foodid.get()
          review_userid = userid.get() 
      
          
          # INSERT QUERY FOR FOOD ESTABLISHMENT TABLE
          sql = "INSERT INTO REVIEW (Description, Rating, Time, Date, Business_id,Food_id,User_id) VALUES (%s, %s, curtime(), curdate(), %s,%s,%s)"
          val = (review_description, review_rating,review_businessid,review_foodid, review_userid)
          mycursor.execute(sql, val)
          db.commit()
          print("Record inserted successfully!")
          messagebox.showinfo("Success", "Review has been recorded successfully!")
          foodreview.destroy()

      foodreview = tk.Toplevel(main_window)
      foodreview.geometry("700x300")
      foodreview.title("Add new food review")
      
      labels = ['Description:', 'Rating:','Business id:','Food id:','User id:']
      for i in range(5):
          tk.Label(foodreview, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
      


      description = tk.Entry(foodreview, width=40, font=('Arial', 14))
      description.grid(row=0, column=1, columnspan=2)

      food_rating = tk.Scale(foodreview, from_=0, to=10, orient="horizontal", length=200)
      food_rating.grid(row=1, column=1, columnspan=2)

      businessid = tk.Entry(foodreview, width=40, font=('Arial', 14))
      businessid.grid(row=2, column=1, columnspan=2)

      foodid = tk.Entry(foodreview, width=40, font=('Arial', 14))
      foodid.grid(row=3, column=1, columnspan=2)

      userid = tk.Entry(foodreview, width=40, font=('Arial', 14))
      userid.grid(row=4, column=1, columnspan=2)
      submit = tk.Button(foodreview, text='Submit Now', command=submit_data)
      submit.grid(row=5, column=1)  





    # AddReview = tk.Button(main_window, text='Add a new food review', command=add_foodreview)
    # AddReview.pack(pady=20)

    # view all food reviews
    viewAllFoodReviews = tk.Button(main_window, text='View all food reviews', command=viewFoodReviews)
    viewAllFoodReviews.pack(pady=20)

    # view all food establishments
    viewAllFoodReviews = tk.Button(main_window, text='View all food establishments', command=viewFoodEstablishments)
    viewAllFoodReviews.pack(pady=20)









mainpage()




root.mainloop()









