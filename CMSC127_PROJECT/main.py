import tkinter as tk
from functools import partial
from tkinter import Label, messagebox, ttk

import login_page
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="finalproject",
    password="hershey",
    database="finalproject"
)

mycursor = db.cursor()


def mainpage():

    main_window = tk.Tk()
    
    main_window.geometry("1000x500")
    main_window.title("FINAL PROJECT")
    

    tabControl = ttk.Notebook(main_window)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)


    tabControl.add(tab1, text='Add a food review')
    tabControl.add(tab2, text='Edit a food review')
    tabControl.add(tab2, text='Add a food establishment')


    tabControl.pack(expand=1, fill="both")
    def deletefooditem(items, row, column):
            
            deletefoodid = items[row][column]
            sql1 = "DELETE FROM review WHERE Food_id = %s"
            mycursor.execute(sql1, (deletefoodid,))
            sql = "DELETE FROM Food_item WHERE Food_id = %s"
            mycursor.execute(sql, (deletefoodid,))
            db.commit()
            messagebox.showinfo("Success", "Food item has been DELETED!")
            
    def editfooditem(items, row, column):
        def submit_data():
            foodid = items[row][column]
           
            food_name = foodname.get()
            food_price = price.get()
            type_of_food = typeoffood_list.get()
            food_description = description.get()
            food_businessid =items[row][5]
            
       
            sql = "UPDATE FOOD_ITEM SET Name = %s, Price = %s, Type_of_food = %s, Description = %s, Business_id = %s WHERE Food_id = %s"
            val = ( food_name, food_price,type_of_food,food_description,food_businessid, foodid)
            mycursor.execute(sql, val)
            db.commit()
            print("Record inserted successfully!")
            messagebox.showinfo("Success", "Food item has been recorded successfully!")
            editfooditem.destroy()
        editfooditem = tk.Toplevel(tab2)
        editfooditem.geometry("700x300")
        editfooditem.title("Edit food item")
        typeoffood_list = ttk.Combobox(editfooditem,state="readonly",
            values=["Appetizer", "Entree/ Main Dish", "Sides", "Dessert"]
        )
        
        labels = ['Food name:', 'Price:','Type of food:','Description:']
        for i in range(4):
            tk.Label(editfooditem, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
        

        foodname = tk.Entry(editfooditem, width=40, font=('Arial', 14))
        foodname.grid(row=0, column=1, columnspan=2)

        price = tk.Entry(editfooditem, width=40, font=('Arial', 14))
        price.grid(row=1, column=1, columnspan=2)

        typeoffood_list.grid(row=2, column=1,columnspan=2)

        description = tk.Entry(editfooditem, width=40, font=('Arial', 14))
        description.grid(row=3, column=1, columnspan=2)


        submit = tk.Button(editfooditem, text='Submit Now', command=submit_data)
        submit.grid(row=4, column=1)  


    def add_fooditem(businessid):
 
      def submit_data():
        
          food_name = foodname.get()
          food_price = price.get()
          type_of_food = typeoffood_list.get()
          food_description = description.get()
          food_businessid =businessid
          
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
      
      labels = ['Food name:', 'Price:','Type of food:', 'Description']
      for i in range(4):
          tk.Label(fooditem, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
      

      foodname = tk.Entry(fooditem, width=40, font=('Arial', 14))
      foodname.grid(row=0, column=1, columnspan=2)

      price = tk.Entry(fooditem, width=40, font=('Arial', 14))
      price.grid(row=1, column=1, columnspan=2)

      typeoffood_list.grid(row=2, column=1,columnspan=2)

      description = tk.Entry(fooditem, width=40, font=('Arial', 14))
      description.grid(row=3, column=1, columnspan=2)

    #   businessid = tk.Entry(fooditem, width=40, font=('Arial', 14))
    #   businessid.grid(row=4, column=1, columnspan=2)

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

        def viewFoodReviewsPerEstablishment(reviews, row, col):
            businessid = reviews[row][col]
            edit2 = tk.Toplevel(tab1)
            edit2.geometry("700x500")
            sql = "SELECT * FROM REVIEW WHERE Business_id = %s"
            val = (businessid,)
            mycursor.execute(sql, val)
            reviews = mycursor.fetchall()

            for i, review in enumerate(reviews):
                for j, value in enumerate(review):
                    tk.Label(edit2, text=value).grid(row=i, column=j, padx=10, pady=10)
                tk.Button(edit2, text='Edit', command=lambda row=i, column=0: edit_foodreview(reviews, row, column)).grid(row=i, column=9)
                deletebutton = tk.Button(edit2, text='Delete', bg='red', fg='white', command=lambda row=i, column=0: delete_foodreview(reviews, row, column))
                deletebutton.grid(row=i, column=10, padx=10, pady=10)



        def viewAllFoodReviews():
            def filterByDate():
                selected_date = date_entry.get()
                filter_type = filter_type_var.get()

                if filter_type == "Year":
                    sql = "SELECT * FROM REVIEW WHERE YEAR(Date) = %s"
                elif filter_type == "Month":
                    sql = "SELECT * FROM REVIEW WHERE MONTH(Date) = %s"
                elif filter_type == "Day":
                    sql = "SELECT * FROM REVIEW WHERE DAY(Date) = %s"
                else:
                    messagebox.showerror("Error", "Please select a filter type.")
                    return

                mycursor.execute(sql, (selected_date,))
                reviews = mycursor.fetchall()
                displayReviews(reviews)

            def displayReviews(reviews):
                for widget in review_frame.winfo_children():
                    widget.destroy()

                for i, review in enumerate(reviews):
                    for j, value in enumerate(review):
                        tk.Label(review_frame, text=value).grid(row=i, column=j, padx=10, pady=10)
                    tk.Button(review_frame, text='Edit', command=lambda row=i, column=0: edit_foodreview(reviews, row, column)).grid(row=i, column=9)
                    delete_button = tk.Button(review_frame, text='Delete', bg='red', fg='white', command=lambda row=i, column=0: delete_foodreview(reviews, row, column))
                    delete_button.grid(row=i, column=10, padx=10, pady=10)

            edit2 = tk.Toplevel(tab1)
            edit2.geometry("700x500")
            edit2.title("All Food Reviews")

            date_frame = tk.Frame(edit2)
            date_frame.grid(row=0, column=0, pady=10)

            date_label = tk.Label(date_frame, text="Select Filter Type:")
            date_label.grid(row=0, column=0)

            filter_type_var = tk.StringVar()
            filter_type_var.set("Year")  # Default selection
            filter_type_options = ["Year", "Month", "Day"]
            filter_type_dropdown = tk.OptionMenu(date_frame, filter_type_var, *filter_type_options)
            filter_type_dropdown.grid(row=0, column=1)

            date_label = tk.Label(date_frame, text="Enter Date:")
            date_label.grid(row=1, column=0)

            date_entry = tk.Entry(date_frame, width=15)
            date_entry.grid(row=1, column=1)

            date_button = tk.Button(date_frame, text="Filter", command=filterByDate)
            date_button.grid(row=1, column=2)

            review_frame = tk.Frame(edit2)
            review_frame.grid(row=1, column=0)

            sql = "SELECT * FROM REVIEW"
            mycursor.execute(sql)
            reviews = mycursor.fetchall()
            displayReviews(reviews)

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
      
        tk.Label(tab1, text='RESTAURANTS').grid(row=1,column=1)
  
        numofrows =len(establishments)
        for i, establishment in enumerate(establishments):
            tk.Label(tab1, text=establishment[1]).grid(row=i+2, column=0, padx=10, pady=10)
            add_foodreview1 = tk.Button(tab1, text='Add new food review', command=lambda row=i, column=0:viewfooditemsbyestablishment(establishments,row,column))
            add_foodreview1.grid(row=i+2, column=1, pady=10)   
            view_foodReviews = tk.Button(tab1, text='View food reviews', bg='chartreuse4', fg='white', command=lambda row=i, column=0:viewFoodReviewsPerEstablishment(establishments,row,column))
            view_foodReviews.grid(row=i+2, column=2, padx=10, pady=10) 

        viewAllFoodReviewsbutton = tk.Button(tab1, text='View all food reviews',bg='green', fg='white', command=viewAllFoodReviews)
        viewAllFoodReviewsbutton.grid(row=numofrows+2, column=1,pady=10)
        
   
    def viewFoodEstablishments(tab2, establishments, min_rating=None):
        def searchestablishments(search_entry, establishments, tab2):
            search_query = search_entry.get()
            filtered_establishments = [est for est in establishments if search_query.lower() in est[1].lower()]
            viewFoodEstablishments(tab2, filtered_establishments)

        def calculate_average_rating(business_id, min_rating=None):
            sql = "SELECT AVG(Rating) FROM ESTABLISHMENT_REVIEW WHERE Business_id = %s"
            mycursor.execute(sql, (business_id,))
            average_rating = mycursor.fetchone()[0]
            return average_rating if average_rating and (not min_rating or average_rating >= min_rating) else 0

        for widget in tab2.winfo_children():
            widget.destroy()

        numofrows = len(establishments)

        headers = ['Business ID', 'Name', 'Address', 'Average Rating']
        for i, header in enumerate(headers):
            tk.Label(tab2, text=header).grid(row=0, column=i, padx=10, pady=10)

        for i, establishment in enumerate(establishments):
            business_id = establishment[0]
            name = establishment[1]
            address = establishment[2]
            avg_rating = calculate_average_rating(business_id, min_rating)

            tk.Label(tab2, text=business_id).grid(row=i + 1, column=0, padx=10, pady=10)
            tk.Label(tab2, text=name).grid(row=i + 1, column=1, padx=10, pady=10)
            tk.Label(tab2, text=address).grid(row=i + 1, column=2, padx=10, pady=10)
            tk.Label(tab2, text=avg_rating).grid(row=i + 1, column=3, padx=10, pady=10)

        def filterByRating(tab2, establishments):
            rating_filter_window = tk.Toplevel(tab2)
            rating_filter_window.geometry("300x100")
            rating_filter_window.title("Filter by Rating")

            tk.Label(rating_filter_window, text="Minimum Rating:").grid(row=0, column=0, padx=10, pady=10)
            min_rating_entry = tk.Entry(rating_filter_window)
            min_rating_entry.grid(row=0, column=1, padx=10, pady=10)

            apply_filter_button = tk.Button(rating_filter_window, text="Apply Filter", command=lambda: applyRatingFilter(tab2, establishments, min_rating_entry))
            apply_filter_button.grid(row=1, column=0, columnspan=2, pady=10)

        def applyRatingFilter(tab2, establishments, min_rating_entry):
            try:
                min_rating = float(min_rating_entry.get())
                filtered_establishments = [est for est in establishments if calculate_average_rating(est[0], min_rating) >= min_rating]
                viewFoodEstablishments(tab2, filtered_establishments, min_rating)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for minimum rating.")

        
        def add_foodestablishment():
            def submit_data():
                business_name = businessname.get()
                business_address = address.get()
                
                # INSERT QUERY FOR FOOD ESTABLISHMENT TABLE
                sql = "INSERT INTO FOOD_ESTABLISHMENT (Name, Address) VALUES (%s, %s)"
                val = (business_name, business_address)
                mycursor.execute(sql, val)
                db.commit()
                print("Record inserted successfully!")
                messagebox.showinfo("Success", "Food establishment has been recorded successfully!")
                new_window.destroy()
                
            new_window = tk.Toplevel(tab2)
            new_window.geometry("700x300")
            new_window.title("Add food establishment")
            
            labels = ['Business name:', 'Address:']
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
            
            sql4 = "UPDATE REVIEW SET Food_id = NULL WHERE Business_id =" + str(businessid)
            mycursor.execute(sql4)
            sql1 = "DELETE FROM FOOD_ITEM where Business_id =" + str(businessid)
            mycursor.execute(sql1)
            sql3 = "UPDATE REVIEW SET Business_id = NULL WHERE Business_id =" + str(businessid)
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
                val = (editbusiness_name, editbusiness_address)
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

            def search_items():
                search_query = search_entry.get().lower()
                if not search_query:
                    update_food_items(items)
                filtered_items = [item for item in items if search_query in item[1].lower()]
                update_food_items(filtered_items)
                

            def filter_by_price_range():
                min_price = min_price_entry.get().strip()
                max_price = max_price_entry.get().strip()

                filtered_items = items

                if min_price:
                    filtered_items = [item for item in filtered_items if float(item[2]) >= float(min_price)]

                if max_price:
                    filtered_items = [item for item in filtered_items if float(item[2]) <= float(max_price)]

                update_food_items(filtered_items)

            def update_food_items(display_items):
                for widget in food_items_frame.winfo_children():
                    widget.destroy()
                for i, item in enumerate(display_items):
                    for j, value in enumerate(item):
                        item_label = tk.Label(food_items_frame, text=value)
                        item_label.grid(row=i, column=j, padx=10, pady=5, sticky="w")
                        tk.Button(food_items_frame, text='Edit', command=partial(editfooditem, items, i, 0)).grid(row=i, column=7)
                        deletebutton = tk.Button(food_items_frame, text='Delete', bg='red', fg='white', command=partial(deletefooditem, items, i, 0))
                        deletebutton.grid(row=i, column=8, padx=10, pady=10)
 

            def viewByType(businessid):
                sql = "SELECT * FROM food_item WHERE Business_id = %s AND Type_of_food = %s"
                mycursor.execute(sql, (businessid, var.get()))
                filtered_items = mycursor.fetchall()
                update_food_items(filtered_items)

            def viewByPrice(businessid):
                sql = "SELECT * FROM food_item WHERE Business_id = %s ORDER BY Price"
                mycursor.execute(sql, (businessid,))
                sorted_items = mycursor.fetchall()
                update_food_items(sorted_items)

            if row is not None and col is not None:
                businessid = items[row][col]
            else:
                businessid = items[0][0]  

            allFoodItems = tk.Toplevel(tab2)
            allFoodItems.geometry("700x700")
            allFoodItems.title("Food Items")

            # Button to add a new food item
            tk.Button(allFoodItems, text='Add a new food item', command=partial(add_fooditem, businessid)).pack(pady=5)
         

            # Sort by price button
            tk.Button(allFoodItems, text='Sort by Price', command=lambda: viewByPrice(businessid)).pack(pady=5)

            # Food type label and combobox
            tk.Label(allFoodItems, text="Filter by Food Type: ").pack(pady=5)
            var = tk.StringVar()
            typeoffood = ttk.Combobox(allFoodItems, textvariable=var)
            typeoffood['values'] = ["Appetizer", "Entree/ Main Dish", "Sides", "Dessert"]
            typeoffood['state'] = 'readonly'
            typeoffood.pack()

            # OK button for applying food type filter
            tk.Button(allFoodItems, text='Apply Filter', command=lambda: viewByType(businessid)).pack(pady=5)

            # Search frame
            search_frame = tk.Frame(allFoodItems)
            search_frame.pack(pady=10)

            search_entry = tk.Entry(search_frame, width=50)
            search_entry.pack(side=tk.LEFT, padx=5)

            search_button = tk.Button(search_frame, text="Search", command=search_items)
            search_button.pack(side=tk.LEFT)

            # Price range filter frame
            price_range_frame = tk.Frame(allFoodItems)
            price_range_frame.pack(pady=10)

            tk.Label(price_range_frame, text="Min Price:").pack(side=tk.LEFT, padx=5)
            min_price_entry = tk.Entry(price_range_frame, width=8)
            min_price_entry.pack(side=tk.LEFT)

            tk.Label(price_range_frame, text="Max Price:").pack(side=tk.LEFT, padx=5)
            max_price_entry = tk.Entry(price_range_frame, width=8)
            max_price_entry.pack(side=tk.LEFT)

            filter_price_button = tk.Button(price_range_frame, text="Filter by Price Range", command=filter_by_price_range)
            filter_price_button.pack(side=tk.LEFT, padx=5)

            # Frame for displaying food items
            food_items_frame = tk.Frame(allFoodItems)
            food_items_frame.pack(pady=10)

            # Fetch and display food items from the database
            sql = "SELECT * FROM food_item WHERE Business_id = %s"
            mycursor.execute(sql, (businessid,))
            items = mycursor.fetchall()
            
            numofrows = len(items)
            for i, item in enumerate(items):
                for j, value in enumerate(item):
                    tk.Label(food_items_frame, text=value).grid(row=i+1, column=j, padx=10, pady=10)
                tk.Button(food_items_frame, text='Edit', command=partial(editfooditem, items, i, 0)).grid(row=i+1, column=8)
                deletebutton = tk.Button(food_items_frame, text='Delete', bg='red', fg='white', command=partial(deletefooditem, items, i, 0))
                deletebutton.grid(row=i+1, column=9, padx=10, pady=10)

            # AddFoodItem.grid(row=numofrows+1, column=1, pady=10)

            tk.Button(allFoodItems, text='Sort by Price', command=lambda: viewByPrice(businessid)).grid(row=0, column=1, padx=10, pady=10)
            tk.Label(allFoodItems, text="Food Type: ").grid(row=0, column=2, padx=10, pady=10)
            var = tk.StringVar()
            typeoffood = ttk.Combobox(allFoodItems, textvariable=var)
            typeoffood['values'] = ["Appetizer", "Entree/ Main Dish", "Sides", "Dessert"]
            typeoffood['state'] = 'readonly'
            typeoffood.grid(row=0, column=3, columnspan=2)
            tk.Button(allFoodItems, text='Apply Filter', command=lambda: viewByType(businessid)).grid(row=0, column=5, padx=10, pady=10)


        def viewEstablishmentReviews(items, row, col):
            def delete_foodestablishmentreview(reviews, row, column):
                deletereviewno = reviews[row][column]
                sql = "DELETE FROM ESTABLISHMENT_REVIEW WHERE Review_no = %s"
                mycursor.execute(sql, (deletereviewno,))
                db.commit()
                messagebox.showinfo("Success", "Food establishment review has been DELETED!")

            def edit_foodestablishmentreview(reviews, row, column):
                def edit_submit_data():
                    reviewno = reviews[row][column]
                    newdescription = editDescription.get()
                    newrating = edit_rating.get()

                    sql = "UPDATE ESTABLISHMENT_REVIEW SET Description = %s, Rating = %s WHERE Review_no = %s"
                    val = (newdescription, newrating, reviewno)
                    mycursor.execute(sql, val)
                    db.commit()
                    messagebox.showinfo("Success", "Food establishment review has been edited successfully!")
                    edit1.destroy()
                    viewEstablishmentReviews(items, row, column)

                edit1 = tk.Toplevel(tab2)
                edit1.geometry("700x300")
                edit1.title("Edit food review")

                labels = ['Enter Description:', 'Rating:']
                for i, label in enumerate(labels):
                    tk.Label(edit1, text=label).grid(row=i, column=0, padx=10, pady=10)

                editDescription = tk.Entry(edit1, width=40, font=('Arial', 14))
                editDescription.grid(row=0, column=1, columnspan=2)

                edit_rating = tk.Scale(edit1, from_=0, to=5, orient="horizontal", length=150)
                edit_rating.grid(row=1, column=1, columnspan=2)

                submit = tk.Button(edit1, text='Edit', command=edit_submit_data)
                submit.grid(row=2, column=1, pady=10)

            def add_foodestablishmentreview():
                def submit_data():
                    review_description = description.get()
                    review_rating = food_rating.get()
                    businessid = items[row][col]

                    review_userid = userid.get()

                    sql = "INSERT INTO ESTABLISHMENT_REVIEW (Description, Rating, Time, Date, Business_id, User_id) VALUES (%s, %s, CURTIME(), CURDATE(), %s, %s)"
                    val = (review_description, review_rating, businessid, review_userid)
                    mycursor.execute(sql, val)
                    db.commit()
                    messagebox.showinfo("Success", "Review has been recorded successfully!")
                    foodReviews.destroy()

                foodestablishmentreview = tk.Toplevel(tab2)
                foodestablishmentreview.geometry("700x300")
                foodestablishmentreview.title("Add new food establishment review")

                labels = ['Description:', 'Rating:', 'User id:']
                for i in range(3):
                    tk.Label(foodestablishmentreview, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

                description = tk.Entry(foodestablishmentreview, width=40, font=('Arial', 14))
                description.grid(row=0, column=1, columnspan=2)
# tk.Scale(edit1, from_=0, to=5, orient="horizontal", length=150)
                food_rating = tk.Scale(foodestablishmentreview, from_=0, to=5, orient="horizontal", length=150)
                food_rating.grid(row=1, column=1, columnspan=2)

                userid = tk.Entry(foodestablishmentreview, width=40, font=('Arial', 14))
                userid.grid(row=2, column=1, columnspan=2)
                submit = tk.Button(foodestablishmentreview, text='Submit Now', command=submit_data)
                submit.grid(row=3, column=1)

            foodReviews = tk.Toplevel(tab2)
            foodReviews.geometry("700x500")
            foodReviews.title("Establishment reviews")

            businessid = items[row][col]
            sql = "SELECT * FROM ESTABLISHMENT_REVIEW WHERE Business_id = " + str(businessid)
            mycursor.execute(sql)
            reviews = mycursor.fetchall()
            numofrows = len(reviews)
            for i, review in enumerate(reviews):
                for j, value in enumerate(review):
                    tk.Label(foodReviews, text=value).grid(row=i, column=j, padx=10, pady=10)
                tk.Button(foodReviews, text='Edit', command=partial(edit_foodestablishmentreview, reviews, i, 0)).grid(row=i, column=8)

                deletebutton = tk.Button(foodReviews, text='Delete', bg='red', fg='white', command=partial(delete_foodestablishmentreview, reviews, i, 0))
                deletebutton.grid(row=i, column=9, padx=10, pady=10)
            button = tk.Button(foodReviews, text='Add a food establishment review', command=add_foodestablishmentreview)
            button.grid(row=numofrows + 1, column=1, pady=10)

        for widget in tab2.winfo_children():
            widget.destroy()

        numofrows = len(establishments)
        search_frame = tk.Frame(tab2)
        search_frame.grid(row=0, column=0)

        search_entry = tk.Entry(search_frame, width=20)
        search_entry.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(search_frame, text="Search", command=lambda: searchestablishments(search_entry, establishments, tab2))
        search_button.pack(side=tk.LEFT)
        sql = "SELECT * FROM FOOD_ESTABLISHMENT"
        mycursor.execute(sql)
        establishments1 = mycursor.fetchall()

        view = tk.Button(tab2, text="View all establishments", command=lambda: viewFoodEstablishments(tab2, establishments1))
        view.grid(row=0, column=1)

        for i, establishment in enumerate(establishments):
            for j, value in enumerate(establishment):
                tk.Label(tab2, text=value).grid(row=i + 1, column=j, padx=10, pady=10)

            edit_foodEstablishment = tk.Button(tab2, text='Edit', command=partial(edit_foodestablishment, establishments, i, 0))
            edit_foodEstablishment.grid(row=i + 1, column=9, padx=10, pady=10)

            view_foodItems = tk.Button(tab2, text='View all food items', command=partial(viewFoodItems, establishments, i, 0))
            view_foodItems.grid(row=i + 1, column=10, padx=10)

            view_foodReviews = tk.Button(tab2, text='View all establishment reviews', command=partial(viewEstablishmentReviews, establishments, i, 0))
            view_foodReviews.grid(row=i + 1, column=11, padx=10, pady=10)

            delete_foodEstablishment = tk.Button(tab2, text='Delete', bg='red', fg='white', command=partial(delete_foodestablishment, establishments, i, 0))
            delete_foodEstablishment.grid(row=i + 1, column=12, padx=10, pady=10)

            filter_by_rating_button = tk.Button(tab2, text="Filter by Rating", command=lambda: filterByRating(tab2, establishments))
            filter_by_rating_button.grid(row=0, column=2)

        AddFoodEstablishment = tk.Button(tab2, text='Add a new food establishment', command=add_foodestablishment)
        AddFoodEstablishment.grid(row=numofrows + 1, column=1, pady=10)

    viewFoodReviews(tab1)
    sql = "SELECT * FROM FOOD_ESTABLISHMENT"
    mycursor.execute(sql)
    establishments = mycursor.fetchall()
    viewFoodEstablishments(tab2,establishments)

    main_window.mainloop()




login_page.login_page(mainpage)











