import tkinter as tk
from tkinter import Label, messagebox, ttk

import mysql.connector

import login_page

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="angel",
    database="finalproject"
)

mycursor = db.cursor()


# diapslya the buttons
def mainpage():

    main_window = tk.Tk()
    
    main_window.geometry("800x500")
    main_window.title("FINAL PROJECT")
    

    tabControl = ttk.Notebook(main_window)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)


    tabControl.add(tab1, text='Add a food review')
    tabControl.add(tab2, text='Edit a food review')
    tabControl.add(tab2, text='Add a food establishment')


    tabControl.pack(expand=1, fill="both")
       
   

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





    def viewFoodReviews(tab1):
       
        for widget in tab1.winfo_children():
            widget.destroy()



                

        def delete_foodreview(reviews, row, column):
            deletereviewno = reviews[row][column]
            sql = "DELETE FROM Review WHERE Review_no = %s"
            mycursor.execute(sql, (deletereviewno,))
            db.commit()
            messagebox.showinfo("Success", "Food review has been DELETED!")
            viewFoodReviews(tab1)

        def add_foodreview():
            def submit_data():
                review_description = description.get()
                review_rating = food_rating.get()
                review_businessid = businessid.get()
                review_foodid = foodid.get()
                review_userid = userid.get()

                sql = "INSERT INTO REVIEW (Description, Rating, Time, Date, Business_id, Food_id, User_id) VALUES (%s, %s, CURTIME(), CURDATE(), %s, %s, %s)"
                val = (review_description, review_rating, review_businessid, review_foodid, review_userid)
                mycursor.execute(sql, val)
                db.commit()
                messagebox.showinfo("Success", "Review has been recorded successfully!")
                foodreview.destroy()
                viewFoodReviews(tab1) 

            foodreview = tk.Toplevel(tab1)
            foodreview.geometry("700x300")
            foodreview.title("Add new food review")

            labels = ['Description:', 'Rating:', 'Business id:', 'Food id:', 'User id:']
            for i, label in enumerate(labels):
                tk.Label(foodreview, text=label).grid(row=i, column=0, padx=10, pady=10)

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

                sql = "UPDATE REVIEW SET Description = %s, Rating = %s WHERE Review_no = %s"
                val = (newdescription, newrating, reviewno)
                mycursor.execute(sql, val)
                db.commit()
                messagebox.showinfo("Success", "Food review has been edited successfully!")
                edit1.destroy()
                viewFoodReviews(tab1) 

            edit1 = tk.Toplevel(tab1)
            edit1.geometry("700x300")
            edit1.title("Edit food review")

            labels = ['Enter Description:', 'Rating:']
            for i, label in enumerate(labels):
                tk.Label(edit1, text=label).grid(row=i, column=0, padx=10, pady=10)

            editDescription = tk.Entry(edit1, width=40, font=('Arial', 14))
            editDescription.grid(row=0, column=1, columnspan=2)

            edit_rating = tk.Scale(edit1, from_=0, to=10, orient="horizontal", length=200)
            edit_rating.grid(row=1, column=1, columnspan=2)

            submit = tk.Button(edit1, text='Edit', command=edit_submit_data)
            submit.grid(row=2, column=1, pady=10)
        def viewAllFoodReviews():
            edit2 = tk.Toplevel(tab1)
            edit2.geometry("700x500")
            sql = "SELECT * FROM REVIEW"
            mycursor.execute(sql)
            reviews = mycursor.fetchall()

            for i, review in enumerate(reviews):
                for j, value in enumerate(review):
                    tk.Label(edit2, text=value).grid(row=i, column=j, padx=10, pady=10)
                tk.Button(edit2, text='Edit', command=lambda row=i, column=0: edit_foodreview(reviews, row, column)).grid(row=i, column=9)
                deletebutton = tk.Button(edit2, text='Delete', bg='red', fg='white', command=lambda row=i, column=0: delete_foodreview(reviews, row, column))
                deletebutton.grid(row=i, column=10, padx=10, pady=10) 

        def viewfooditemsbyestablishment(establishments,row,column):
            def submit_data():
                review_description = description.get()
                review_rating = food_rating.get()
                review_businessid = business_id
                review_foodid = item_dict[selected_item.get()]
                review_userid = userid.get()

                sql = "INSERT INTO REVIEW (Description, Rating, Time, Date, Business_id, Food_id, User_id) VALUES (%s, %s, CURTIME(), CURDATE(), %s, %s, %s)"
                val = (review_description, review_rating, review_businessid, review_foodid, review_userid)
                mycursor.execute(sql, val)
                db.commit()
                messagebox.showinfo("Success", "Review has been recorded successfully!")
          
            business_id = establishments[row][column]
            edit1 = tk.Toplevel(tab1)
            edit1.geometry("700x500")
            edit1.title("Add a food review")

            sql = "SELECT * FROM food_item WHERE Business_id = " + str(business_id)
            mycursor.execute(sql)
            items = mycursor.fetchall()
           
            if items:
                item_dict = {item[1]: item[0] for item in items} 
                item_names = list(item_dict.keys())

                selected_item = tk.StringVar(edit1)
                selected_item.set(item_names[0])  

                tk.Label(edit1, text="Select food item:").grid(row=0, column=0, padx=10, pady=20)
    
                item_dropdown = tk.OptionMenu(edit1, selected_item, *item_names)
                item_dropdown.grid(row=1, column=0, padx=10, pady=10)
            labels = ['Description:', 'Rating:',  'User id:']
            for i, label in enumerate(labels):
                tk.Label(edit1, text=label).grid(row=i+2, column=0, padx=10, pady=10)

            description = tk.Entry(edit1, width=40, font=('Arial', 14))
            description.grid(row=2, column=1, columnspan=2)

            food_rating = tk.Scale(edit1, from_=0, to=10, orient="horizontal", length=200)
            food_rating.grid(row=3, column=1, columnspan=2)

         

            userid = tk.Entry(edit1, width=40, font=('Arial', 14))
            userid.grid(row=4, column=1, columnspan=2)

            submit = tk.Button(edit1, text='Submit Now', command =submit_data)
            submit.grid(row=5, column=1)

        sql = "SELECT * FROM FOOD_ESTABLISHMENT"
        mycursor.execute(sql)
        establishments = mycursor.fetchall()
        tk.Label(tab1, text='RESTAURANTS').grid(row=0,column=1)
        numofrows =len(establishments)
        for i, establishment in enumerate(establishments):
            tk.Label(tab1, text=establishment[1]).grid(row=i+1, column=0, padx=10, pady=10)
            add_foodreview1 = tk.Button(tab1, text='Add new food review', command=lambda row=i, column=0:viewfooditemsbyestablishment(establishments,row,column))
            add_foodreview1.grid(row=i+1, column=1, pady=10)   

        viewAllFoodReviewsbutton = tk.Button(tab1, text='View all food reviews',bg='green', fg='white', command=viewAllFoodReviews)
        viewAllFoodReviewsbutton.grid(row=numofrows+1, column=1,pady=10)
   
        


    def viewFoodEstablishments(tab2):
        def add_foodestablishment():
            def submit_data():    
                
                business_name = businessname.get()
                business_address = address.get()
                
                # INSERT QUERY FOR FOOD ESTABLISHMENT TABLE
                sql = "INSERT INTO FOOD_ESTABLISHMENT (Name, Address) VALUES (%s, %s)"
                val = ( business_name, business_address)
                mycursor.execute(sql, val)
                db.commit()
                print("Record inserted successfully!")
                messagebox.showinfo("Success", "Food establishment has been recorded successfully!")
                new_window.destroy()
                
            new_window = tk.Toplevel(tab2)
            new_window.geometry("700x300")
            new_window.title("Add food establishment")
            
            labels = [ 'Business name:', 'Address:']
            for i in range(2):
                tk.Label(new_window, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
            

            businessname = tk.Entry(new_window, width=40, font=('Arial', 14))
            businessname.grid(row=0, column=1, columnspan=2)

            address = tk.Entry(new_window, width=40, font=('Arial', 14))
            address.grid(row=1, column=1, columnspan=2)

            submit = tk.Button(new_window, text='Submit Now', command=submit_data)
            submit.grid(row=2, column=1)  
    


        def delete_foodestablishment(businesses, row, col):
            businessid = businesses[row][col]
           
            sql4 = "UPDATE REVIEW SET Food_id = NULL WHERE Business_id =" +str(businessid)
            mycursor.execute(sql4)
            sql1 = "DELETE FROM FOOD_ITEM where Business_id =" + str(businessid)
            mycursor.execute(sql1)
            sql3 = "UPDATE REVIEW SET Business_id = NULL WHERE Business_id =" +str(businessid)
            mycursor.execute(sql3)
            
            sql = "DELETE FROM FOOD_ESTABLISHMENT where Business_id =" + str(businessid)
            mycursor.execute(sql)
            
        
            db.commit()
            messagebox.showinfo("Success", "Food establishment has been DELETED!")

        def edit_foodestablishment(items, row, col):
            def edit_submit_data(businessid):
                editbusiness_name = editbusinessname.get()
                editbusiness_address = editbusinessaddress.get()

                sql = "UPDATE FOOD_ESTABLISHMENT SET Name = %s, Address = %s where Business_id = " + str(businessid)
                val = ( editbusiness_name, editbusiness_address)
                mycursor.execute(sql, val)
                db.commit()
                messagebox.showinfo("Success", "Food establishment has been edited successfully!")
                edit1.destroy()


            edit1 = tk.Toplevel(main_window)
            edit1.geometry("700x300")
            edit1.title("Edit food establishment")
            businessid = items[row][col]

            labels = ['Enter new business name:', 'Enter new business address:']
            for i in range(2):
                tk.Label(edit1, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
        
            editbusinessname = tk.Entry(edit1, width=40, font=('Arial', 14))
            editbusinessname.grid(row=0, column=1, columnspan=2)

            editbusinessaddress = tk.Entry(edit1, width=40, font=('Arial', 14))
            editbusinessaddress.grid(row=1, column=1, columnspan=2)
            
            submit = tk.Button(edit1, text='Submit', command=lambda: edit_submit_data(businessid))
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

        def viewEstablishmentReviews(items, row, col):
            def delete_foodestablishmentreview(reviews, row, column):
                deletereviewno = reviews[row][column]
                sql = "DELETE FROM ESTABLISHMENTREVIEW WHERE Review_no = %s"
                mycursor.execute(sql, (deletereviewno,))
                db.commit()
                messagebox.showinfo("Success", "Food establishment review has been DELETED!")
      
            def edit_foodestablishmentreview(reviews, row, column):
                def edit_submit_data():
                    reviewno = reviews[row][column]
                    newdescription = editDescription.get()
                    newrating = edit_rating.get()

                    sql = "UPDATE ESTABLISHMENTREVIEW SET Description = %s, Rating = %s WHERE Review_no = %s"
                    val = (newdescription, newrating, reviewno)
                    mycursor.execute(sql, val)
                    db.commit()
                    messagebox.showinfo("Success", "Food establishment review has been edited successfully!")
                    edit1.destroy()
                    viewEstablishmentReviews(items, row,column)

                edit1 = tk.Toplevel(tab2)
                edit1.geometry("700x300")
                edit1.title("Edit food review")

                labels = ['Enter Description:', 'Rating:']
                for i, label in enumerate(labels):
                    tk.Label(edit1, text=label).grid(row=i, column=0, padx=10, pady=10)

                editDescription = tk.Entry(edit1, width=40, font=('Arial', 14))
                editDescription.grid(row=0, column=1, columnspan=2)

                edit_rating = tk.Scale(edit1, from_=0, to=10, orient="horizontal", length=200)
                edit_rating.grid(row=1, column=1, columnspan=2)

                submit = tk.Button(edit1, text='Edit', command=edit_submit_data)
                submit.grid(row=2, column=1, pady=10)

            def add_foodestablishmentreview():
                def submit_data():
                    review_description = description.get()
                    review_rating = food_rating.get()
                    businessid = items[row][col]
       
                    review_userid = userid.get()

                    sql = "INSERT INTO ESTABLISHMENTREVIEW (Description, Rating, Time, Date, Business_id, User_id) VALUES (%s, %s, CURTIME(), CURDATE(), %s, %s)"
                    val = (review_description, review_rating, businessid, review_userid)
                    mycursor.execute(sql, val)
                    db.commit()
                    messagebox.showinfo("Success", "Review has been recorded successfully!")
                    foodReviews.destroy()
                  
                foodestablishmentreview = tk.Toplevel(tab2)
                foodestablishmentreview.geometry("700x300")
                foodestablishmentreview.title("Add new food establishment review")
                
                labels = ['Description:', 'Rating:','User id:']
                for i in range(3):
                    tk.Label(foodestablishmentreview, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
                    

                description = tk.Entry(foodestablishmentreview, width=40, font=('Arial', 14))
                description.grid(row=0, column=1, columnspan=2)

                food_rating = tk.Scale(foodestablishmentreview, from_=0, to=10, orient="horizontal", length=200)
                food_rating.grid(row=1, column=1, columnspan=2)

                

                userid = tk.Entry(foodestablishmentreview, width=40, font=('Arial', 14))
                userid.grid(row=2, column=1, columnspan=2)
                submit = tk.Button(foodestablishmentreview, text='Submit Now', command = submit_data)
                submit.grid(row=3, column=1)  
            
            foodReviews = tk.Toplevel(tab2)
            foodReviews.geometry("700x500")
            foodReviews.title("Establishment reviews")
        
            businessid = items[row][col]
            sql = "SELECT * FROM ESTABLISHMENTREVIEW WHERE Business_id ="+str(businessid)
            mycursor.execute(sql)
            reviews = mycursor.fetchall()
            numofrows= len(reviews)
            for i, review in enumerate(reviews):
                    for j, value in enumerate(review):
                        tk.Label(foodReviews, text=value).grid(row=i, column=j, padx=10, pady=10) 
                    tk.Button(foodReviews, text='Edit' , command=lambda row=i, column=0: edit_foodestablishmentreview(reviews, row, column)).grid(row=i, column=8)
                    
                    deletebutton = tk.Button(foodReviews, text='Delete', bg='red', fg='white', command=lambda row=i, column=0: delete_foodestablishmentreview(reviews, row, column))
                    deletebutton.grid(row=i, column=9, padx=10, pady=10)
            button = tk.Button(foodReviews, text='Add a food establishment review', command=add_foodestablishmentreview)
            button.grid(row=numofrows+1, column=1, pady=10) 





        sql = "SELECT * FROM FOOD_ESTABLISHMENT"
        mycursor.execute(sql)
        establishments = mycursor.fetchall()

        
        numofrows = len(establishments)
        
        for i, establishment in enumerate(establishments):
            for j, value in enumerate(establishment):
                tk.Label(tab2, text=value).grid(row=i, column=j, padx=10, pady=10) 
            
                edit_foodEstablishment = tk.Button(tab2, text='Edit', command= lambda row=i, column=0: edit_foodestablishment(establishments, row, column))
                edit_foodEstablishment.grid(row=i, column=9, padx=10, pady=10)  

                view_foodItems = tk.Button(tab2, text='View all food items', command= lambda row=i, column=0: viewFoodItems(establishments, row, column))
                view_foodItems.grid(row=i, column=10, padx=10) 

                view_foodReviews = tk.Button(tab2, text='View all establishment reviews', command= lambda row=i, column=0: viewEstablishmentReviews(establishments, row, column))
                view_foodReviews.grid(row=i, column=11, padx=10, pady=10) 

                delete_foodEstablishment = tk.Button(tab2, text='Delete', bg='red', fg='white', command= lambda row=i, column=0: delete_foodestablishment(establishments,row, column))
                delete_foodEstablishment.grid(row=i, column=12, padx=10, pady=10) 
        AddFoodEstablishment = tk.Button(tab2, text='Add a new food establishment', command=add_foodestablishment)
        AddFoodEstablishment.grid(row=numofrows+1, column=1, pady=10) 
    
 


    viewFoodReviews(tab1)
    viewFoodEstablishments(tab2)

    main_window.mainloop()




# login_page.login_page(mainpage)
mainpage()











