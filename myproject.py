from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Good to learn')
root.iconbitmap('good.ico')
root.geometry("1000x750")
root.resizable(width=False, height=False)
root.configure(background='#d3d3d3')

show_command = Text(root,width=98,height=12)
show_command.place(x=5, y=175)

show_result = Label(root,width=112,height=15)
show_result.place(x=5, y=375)

def update_root_text(showtoroot):
    # Apply argument values to the text fields of the labels defined in the global namespace.
    # print(showtoroot)
    show_command.delete('1.0',END)
    show_command.insert('1.0',showtoroot)

def update_root_label(show_result_tuple):
    # Apply argument values to the text fields of the labels defined in the global namespace.
    # print(show_result_tuple
    show_result.config(text = show_result_tuple)

# Create insert Function for database
def insert():
    # into database
    # messagebox.insert('0.0',"INSERT INTO")
    # messagebox.insert(0,"INSERT INTO")
    print(messagebox.get())
    aaa = ''
    aaa = messagebox.get()
    if aaa == "Employee":   
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()  
        def submit_insert():
            a = ID_number.get()
            if(a == ''):
                a = None
            b = name.get()
            if(b == ''):
                b = None
            c = age.get()
            if(c == ''):
                c = None
            d = gender.get()
            if(d == ''):
                d = None
            e = address.get()
            if(e == ''):
                e = None
            f = salary.get()
            if(f == ''):
                f = None
            g = position.get()
            if(g == ''):
                g = None
            h = admit_date.get()
            if(h == ''):
                h = None
            i = phone.get()
            if(i == ''):
                i = None
            # conn = sqlite3.connect('petshop.db')
            # cur = conn.cursor()
            cur.execute("INSERT INTO Employee VALUES (:ID_number, :name, :age, :gender, :address, :salary, :position, :admit_date, :phone)",
                    {
                        'ID_number': a,
                        'name': b,
                        'age': c,
                        'gender': d,
                        'address': e,
                        'salary': f,
                        'position': g,
                        'admit_date': h,
                        'phone': i
                    })
            toshow = f"INSERT INTO Employee VALUES ({a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}, {i})"
            update_root_text(toshow)
            # update_root_labels(toshow)
            
            conn.commit()
              
        def clearentry():
            ID_number.delete(0,END)
            name.delete(0,END)
            age.delete(0,END)
            gender.delete(0,END)
            address.delete(0,END)
            salary.delete(0,END)
            position.delete(0,END)
            admit_date.delete(0,END)
            phone.delete(0,END)

        def exitinsert():
            conn.close()
            top.destroy()

        top= Toplevel(root)
        top.geometry("600x250")
        top.title("Insert Employee")
        top.resizable(width=False, height=False)

        submitbt = Button(top, text = "Submit", command = submit_insert)
        submitbt.grid(row=0, column=3, pady=3,padx=10, ipadx=30)

        clearbt = Button(top, text = "Clear", command = clearentry)
        clearbt.grid(row=1, column=3, pady=3, padx=10, ipadx=30)

        exit_button = Button(top, text="Done", command=exitinsert)
        exit_button.grid(row=2, column=3, pady=3, padx=10, ipadx=30)

        ID_number = Entry(top, width = 30)
        ID_number.grid(row = 0, column=1, padx=20)
        ID_number_label = Label(top, text="ID_number")
        ID_number_label.grid(row = 0, column = 0)
        
        name = Entry(top, width = 30)
        name.grid(row = 1, column=1, padx=20)
        name_label = Label(top, text="name")
        name_label.grid(row = 1, column = 0)

        age = Entry(top, width = 30)
        age.grid(row = 2, column=1, padx=20)
        age_label = Label(top, text="age")
        age_label.grid(row = 2, column = 0)

        gender = Entry(top, width = 30)
        gender.grid(row = 3, column=1, padx=20)
        gender_label = Label(top, text="gender")
        gender_label.grid(row = 3, column = 0)

        address = Entry(top, width = 30)
        address.grid(row = 4, column=1, padx=20)
        address_label = Label(top, text="address")
        address_label.grid(row = 4, column = 0)

        salary = Entry(top, width = 30)
        salary.grid(row = 5, column=1, padx=20)
        salary_label = Label(top, text="salary")
        salary_label.grid(row = 5, column = 0)

        position = Entry(top, width = 30)
        position.grid(row = 6, column=1, padx=20)
        position_label = Label(top, text="position")
        position_label.grid(row = 6, column = 0)

        admit_date = Entry(top, width = 30)
        admit_date.grid(row = 7, column=1, padx=20)
        admit_date_label = Label(top, text="admit_date")
        admit_date_label.grid(row = 7, column = 0)

        phone = Entry(top, width = 30)
        phone.grid(row = 8, column=1, padx=20)
        phone_label = Label(top, text="phone")
        phone_label.grid(row = 8, column = 0)


    elif aaa == "Animal":
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        def submit_insert():
            a = Pet_ID.get()
            if(a == ''):
                a = None
            b = species.get()
            if(b == ''):
                b = None
            c = breed.get()
            if(c == ''):
                c = None
            d = age.get()
            if(d == ''):
                d = None
            e = gender.get()
            if(e == ''):
                e = None
            f = from_suppiler.get()
            if(f == ''):
                f = None
            g = in_date.get()
            if(g == ''):
                g = None
            h = out_date.get()
            if(h == ''):
                h = None
            
            cur.execute("INSERT INTO Animal VALUES (:P_ID, :species, :breed, :age, :gender, :from_suppiler, :in_date, :out_date )",
                    {
                        'P_ID': a,
                        'species': b,
                        'breed': c,
                        'age': d,
                        'gender': e,
                        'from_suppiler': f,
                        'in_date': g,
                        'out_date': h,
                    })
            toshow = f"INSERT INTO Animal VALUES ({a}, {b}, {c}, {d}, {e}, {f}, {g}, {h} )"
            update_root_text(toshow)

            conn.commit()
            # conn.close()

        def clearentry():
            Pet_ID.delete(0,END)
            species.delete(0,END)
            breed.delete(0,END)
            age.delete(0,END)
            gender.delete(0,END)
            from_suppiler.delete(0,END)
            in_date.delete(0,END)
            out_date.delete(0,END)



        def exitinsert():
            conn.close()
            top.destroy()

        top= Toplevel(root)
        top.geometry("600x250")
        top.title("Insert Animal")
        top.resizable(width=False, height=False)

        submitbt = Button(top, text = "Submit", command = submit_insert)
        submitbt.grid(row=0, column=3, pady=3, padx=10, ipadx=30)

        clearbt = Button(top, text = "Clear", command = clearentry)
        clearbt.grid(row=1, column=3, pady=3, padx=10, ipadx=30)

        exit_button = Button(top, text="Done", command=exitinsert)
        exit_button.grid(row=2, column=3, pady=3, padx=10, ipadx=30)

        Pet_ID = Entry(top, width = 30)
        Pet_ID.grid(row = 0, column=1, padx=20)
        P_ID_label = Label(top, text="P_ID")
        P_ID_label.grid(row = 0, column = 0)
        
        species = Entry(top, width = 30)
        species.grid(row = 1, column=1, padx=20)
        species_label = Label(top, text="species")
        species_label.grid(row = 1, column = 0)

        breed = Entry(top, width = 30)
        breed.grid(row = 2, column=1, padx=20)
        breed_label = Label(top, text="breed")
        breed_label.grid(row = 2, column = 0)

        age = Entry(top, width = 30)
        age.grid(row = 3, column=1, padx=20)
        age_label = Label(top, text="age")
        age_label.grid(row = 3, column = 0)

        gender = Entry(top, width = 30)
        gender.grid(row = 4, column=1, padx=20)
        gender_label = Label(top, text="gender")
        gender_label.grid(row = 4, column = 0)

        from_suppiler = Entry(top, width = 30)
        from_suppiler.grid(row = 5, column=1, padx=20)
        from_suppiler_label = Label(top, text="from_suppiler")
        from_suppiler_label.grid(row = 5, column = 0)

        in_date = Entry(top, width = 30)
        in_date.grid(row = 6, column=1, padx=20)
        in_date_label = Label(top, text="in_date")
        in_date_label.grid(row = 6, column = 0)

        out_date = Entry(top, width = 30)
        out_date.grid(row = 7, column=1, padx=20)
        out_date_label = Label(top, text="out_date")
        out_date_label.grid(row = 7, column = 0)

    elif aaa == "Member_Customer":
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        def submit_insert():
            a = member_ID.get()
            if(a == ''):
                a = None
            b = name.get()
            if(b == ''):
                b = None
            c = age.get()
            if(c == ''):
                c = None
            d = gender.get()
            if(d == ''):
                d = None
            e = address.get()
            if(e == ''):
                e = None
            f = pet_ID.get()
            if(f == ''):
                f = None
            g = phone.get()
            if(g == ''):
                g = None
            h = member_join_date.get()
            if(h == ''):
                h = None

            cur.execute("INSERT INTO Member_Customer VALUES (:member_ID, :name, :age, :gender, :address, :pet_ID, :phone, :member_join_date )",
                    {
                        'member_ID': a,
                        'name': b,
                        'age': c,
                        'gender': d,
                        'address': e,
                        'pet_ID': f,
                        'phone': g,
                        'member_join_date': h,
                    })
            toshow = f"INSERT INTO Member_Customer VALUES ({a}, {b},{c}, {d}, {e}, {f}, {g}, {h})"
            update_root_text(toshow)
            
            conn.commit()
            # conn.close()

        def clearentry():
            member_ID.delete(0,END)
            name.delete(0,END)
            age.delete(0,END)
            gender.delete(0,END)
            address.delete(0,END)
            pet_ID.delete(0,END)
            phone.delete(0,END)
            member_join_date.delete(0,END)

        def exitinsert():
            conn.close()
            top.destroy()

        top= Toplevel(root)
        top.geometry("600x250")
        top.title("Insert Member_Customer")
        top.resizable(width=False, height=False)

        submitbt = Button(top, text = "Submit", command = submit_insert)
        submitbt.grid(row=0, column=3, pady=3, padx=10, ipadx=30)

        clearbt = Button(top, text = "Clear", command = clearentry)
        clearbt.grid(row=1, column=3, pady=3, padx=10, ipadx=30)

        exit_button = Button(top, text="Done", command=exitinsert)
        exit_button.grid(row=2, column=3, pady=3, padx=10, ipadx=30)

        member_ID = Entry(top, width = 30)
        member_ID.grid(row = 0, column=1, padx=20)
        member_ID_label = Label(top, text="member_ID")
        member_ID_label.grid(row = 0, column = 0)
        
        name = Entry(top, width = 30)
        name.grid(row = 1, column=1, padx=20)
        name_label = Label(top, text="name")
        name_label.grid(row = 1, column = 0)

        age = Entry(top, width = 30)
        age.grid(row = 2, column=1, padx=20)
        age_label = Label(top, text="age")
        age_label.grid(row = 2, column = 0)

        gender = Entry(top, width = 30)
        gender.grid(row = 3, column=1, padx=20)
        gender_label = Label(top, text="gender")
        gender_label.grid(row = 3, column = 0)

        address = Entry(top, width = 30)
        address.grid(row = 4, column=1, padx=20)
        address_label = Label(top, text="address")
        address_label.grid(row = 4, column = 0)

        pet_ID = Entry(top, width = 30)
        pet_ID.grid(row = 5, column=1, padx=20)
        pet_ID_label = Label(top, text="pet_ID")
        pet_ID_label.grid(row = 5, column = 0)

        phone = Entry(top, width = 30)
        phone.grid(row = 6, column=1, padx=20)
        phone_label = Label(top, text="phone")
        phone_label.grid(row = 6, column = 0)

        member_join_date = Entry(top, width = 30)
        member_join_date.grid(row = 7, column=1, padx=20)
        member_join_date_label = Label(top, text="member_join_date")
        member_join_date_label.grid(row = 7, column = 0)

    elif aaa == "Suppiler":
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        def submit_insert():
            a = company_name.get()
            if(a == ''):
                a = None
            b = manager.get()
            if(b == ''):
                b = None
            c = address.get()
            if(c == ''):
                c = None
            d = phone.get()
            if(d == ''):
                d = None
                
            
            cur.execute("INSERT INTO Suppiler VALUES (:company_name, :manager, :address, :phone)",
                    {
                        'company_name': a,
                        'manager': b,
                        'address': c,
                        'phone': d,
                    })
            toshow = f"INSERT INTO Suppiler VALUES ({a}, {b}, {c}, {d})"
            update_root_text(toshow)

            conn.commit()
            # conn.close()

        def clearentry():
            company_name.delete(0,END)
            manager.delete(0,END)
            address.delete(0,END)
            phone.delete(0,END)

        def exitinsert():
            conn.close()
            top.destroy()

        top= Toplevel(root)
        top.geometry("600x250")
        top.title("Insert Suppiler")
        top.resizable(width=False, height=False)

        submitbt = Button(top, text = "Submit", command = submit_insert)
        submitbt.grid(row=0, column=3, pady=3, padx=10, ipadx=30)

        clearbt = Button(top, text = "Clear", command = clearentry)
        clearbt.grid(row=1, column=3, pady=3, padx=10, ipadx=30)

        exit_button = Button(top, text="Done", command=exitinsert)
        exit_button.grid(row=2, column=3, pady=3, padx=10, ipadx=30)

        company_name = Entry(top, width = 30)
        company_name.grid(row = 0, column=1, padx=20)
        company_name_label = Label(top, text="company_name")
        company_name_label.grid(row = 0, column = 0)
        
        manager = Entry(top, width = 30)
        manager.grid(row = 1, column=1, padx=20)
        manager_label = Label(top, text="manager")
        manager_label.grid(row = 1, column = 0)

        address = Entry(top, width = 30)
        address.grid(row = 2, column=1, padx=20)
        address_label = Label(top, text="address")
        address_label.grid(row = 2, column = 0)

        phone = Entry(top, width = 30)
        phone.grid(row = 3, column=1, padx=20)
        phone_label = Label(top, text="phone")
        phone_label.grid(row = 3, column = 0)
  
    elif aaa == "Product":
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()
        
        def submit_insert():
            a = product_name.get()
            if(a == ''):
                a = None
            b = product_type.get()
            if(b == ''):
                b = None
            c = price.get()
            if(c == ''):
                c = None
            d = suppiler_name.get()
            if(d == ''):
                d = None
            e = in_stock.get()
            if(e == ''):
                e = None
                
            
            cur.execute("INSERT INTO Product VALUES (:product_name, :product_type, :price, :suppiler_name, :in_stock)",
                    {
                        'product_name': a,
                        'product_type': b,
                        'price': c,
                        'suppiler_name': d,
                        'in_stock': e
                    })
            toshow = f"INSERT INTO Product VALUES ({a}, {b}, {c}, {d}, {e})"
            update_root_text(toshow)

            conn.commit()
            # conn.close()

        def clearentry():
            product_name.delete(0,END)
            product_type.delete(0,END)
            price.delete(0,END)
            suppiler_name.delete(0,END)
            in_stock.delete(0,END)

        def exitinsert():
            conn.close()
            top.destroy()

        top= Toplevel(root)
        top.geometry("600x250")
        top.title("Insert Product")
        top.resizable(width=False, height=False)

        submitbt = Button(top, text = "Submit", command = submit_insert)
        submitbt.grid(row=0, column=3, pady=3, padx=10, ipadx=30)

        clearbt = Button(top, text = "Clear", command = clearentry)
        clearbt.grid(row=1, column=3, pady=3, padx=10, ipadx=30)

        exit_button = Button(top, text="Done", command=exitinsert)
        exit_button.grid(row=2, column=3, pady=3, padx=10, ipadx=30)

        product_name = Entry(top, width = 30)
        product_name.grid(row = 0, column=1, padx=20)
        product_name_label = Label(top, text="product_name")
        product_name_label.grid(row = 0, column = 0)
        
        product_type = Entry(top, width = 30)
        product_type.grid(row = 1, column=1, padx=20)
        product_type_label = Label(top, text="product_type")
        product_type_label.grid(row = 1, column = 0)

        price = Entry(top, width = 30)
        price.grid(row = 2, column=1, padx=20)
        price_label = Label(top, text="price")
        price_label.grid(row = 2, column = 0)

        suppiler_name = Entry(top, width = 30)
        suppiler_name.grid(row = 3, column=1, padx=20)
        suppiler_name_label = Label(top, text="suppiler_name")
        suppiler_name_label.grid(row = 3, column = 0) 

        in_stock = Entry(top, width = 30)
        in_stock.grid(row = 4, column=1, padx=20)
        in_stock_label = Label(top, text="in_stock")
        in_stock_label.grid(row = 4, column = 0)  


# Create select_from_where Function for database
def select_from_where():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("SELECT-WHERE-FROM")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        sel = s.get()
        fro = f.get()
        wher = w.get()

        if(wher == ''):
            cur.execute(f"SELECT {sel} FROM {fro}")
            toshow = f"SELECT {sel} FROM {fro}"
        else:
            cur.execute(f"SELECT {sel} FROM {fro} WHERE {wher}")
            toshow = f"SELECT {sel} FROM {fro} WHERE {wher}"
        # cur.execute("SELECT * FROM Animal")

        update_root_text(toshow)

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        # print(print_records)
        update_root_label(print_records)

        conn.commit()
        conn.close()

    s = Entry(top, width = 30)
    s.grid(row = 0, column=1, padx=10 , ipadx=10)
    s_label = Label(top, text = "SELECT")
    s_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)
  
# Create delete Function for database
def delete():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("DELETE")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        fro = f.get()
        wher = w.get()

        if(wher == ''):
            cur.execute(f"DELETE FROM {fro}")
            toshow = f"DELETE FROM {fro}"
        else:
            cur.execute(f"DELETE FROM {fro} WHERE {wher}")
            toshow = f"DELETE FROM {fro} WHERE {wher}"

        update_root_text(toshow)

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
    
    # d = Entry(top, width = 30)
    # d.grid(row = 0, column=1, padx=10 , ipadx=10)
    # d_label = Label(top, text = "DELETE")
    # d_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=1, column=3, pady=10, padx=10, ipadx=30)

# Create update Function for database
def update():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("UPDATE")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        updat = u.get()
        se = s.get()
        wher = w.get()

        # if(wher == ''):
        #     cur.execute(f"UPDATE {updat} SET {se}")
        cur.execute(f"UPDATE {updat} SET {se} WHERE {wher}")

        update_root_text(f"UPDATE {updat} SET {se} WHERE {wher}")

        conn.commit()
        conn.close()
    
    u = Entry(top, width = 30)
    u.grid(row = 0, column=1, padx=10 , ipadx=10)
    u_label = Label(top, text = "UPDATE")
    u_label.grid(row = 0, column=0, ipadx=10)
    u_label_b = Label(top, text = "Table")
    u_label_b.grid(row = 0, column=2, ipadx=10)

    s = Entry(top, width = 30)
    s.grid(row = 1, column=1, padx=10 , ipadx=10)
    s_label = Label(top, text = "SET")
    s_label.grid(row = 1, column=0, ipadx=10)
    s_labelb = Label(top, text = "column1 = 'value1', ...")
    s_labelb.grid(row = 1, column=2, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)
    w_labelb = Label(top, text = " some_column = 'some_value', ...")
    w_labelb.grid(row = 2, column=2, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=3, column=1, pady=10, padx=10, ipadx=30)

# Create is_in Function for database
def is_in():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("IN")
    top.resizable(width=False, height=False)
    
    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        # sel = s.get()
        # fro = f.get()
        # wher = w.get()
        i_n = i.get()

        # if(wher == ''):
        #     cur.execute(f"UPDATE {updat} SET {se}")
        # update_root_text(f"SELECT {sel} FROM {fro} WHERE {wher} IN {i_n}")

        cur.execute(f"SELECT * FROM Animal WHERE species IN ({i_n})")

        update_root_text(f"SELECT * FROM Animal WHERE species IN ({i_n})")

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
    

    t_label = Label(top, text = "What Animal species you want to search")
    t_label.grid(row = 0, column=1, ipadx=10,pady=20)

    i = Entry(top, width = 30)
    i.grid(row = 1, column=1, padx=10 , ipadx=10)
    i_label_b = Label(top, text = "formate: ['VALUE'] or ['VALUE','VALUE',...] ")
    i_label_b.grid(row = 1, column=2, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=2, column=2, pady=10, padx=10, ipadx=30)

# Create not_in Function for database
def not_in():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("NOT IN")
    top.resizable(width=False, height=False)
    
    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

    
        i_n = i.get()

        cur.execute(f"SELECT * FROM Employee WHERE position NOT IN ({i_n})")

        update_root_text(f"SELECT * FROM Employee WHERE position NOT IN ({i_n})")

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
  
    t_label = Label(top, text = "The Employee with the position you don't care")
    t_label.grid(row = 0, column=0, ipadx=10,pady=20)

    i = Entry(top, width = 30)
    i.grid(row = 1, column=0, padx=10 , ipadx=10)
    i_label_b = Label(top, text = "formate: ['VALUE'] or ['VALUE','VALUE',...] ")
    i_label_b.grid(row = 1, column=1, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=2, column=1, pady=10, padx=10, ipadx=30)

# Create exists Function for database
def exists():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("EXIST")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()


        # 找出Member_Customer由此petshop購買的動物的tuple
        iidd = ii.get()
        cur.execute(f"SELECT * FROM Animal WHERE EXISTS (SELECT * FROM Member_Customer WHERE Member_Customer.pet_ID = Animal.P_ID AND Animal.P_ID = {iidd})")
        update_root_text(f"SELECT * FROM Animal WHERE EXISTS (SELECT * FROM Member_Customer WHERE Member_Customer.pet_ID = Animal.P_ID AND Animal.P_ID = {iidd})")

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
    
    ii = Entry(top, width = 30)
    ii.grid(row = 0, column=1, padx=10 , ipadx=10)
    ii_label = Label(top, text = "Member Customer Pet ID")
    ii_label.grid(row = 0, column=0, ipadx=10)

    

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# Create not_exists Function for database
def not_exists():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("NOT EXIST")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM Member_Customer WHERE NOT EXISTS (SELECT * FROM Animal WHERE Member_Customer.pet_ID = Animal.P_ID)")
        update_root_text(f"SELECT * FROM Member_Customer WHERE NOT EXISTS (SELECT * FROM Animal WHERE Member_Customer.pet_ID = Animal.P_ID)")

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
    
    ii_label = Label(top, text = "Member whose pet are not from this shop")
    ii_label.grid(row = 0, column=0, ipadx=10)

    

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=1, column=0, pady=10, padx=10, ipadx=30)

# Create count Function for database
def count_db():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("COUNT")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        coun = c.get()
        fro = f.get()
        wher = w.get()

        if(wher == ''):
            cur.execute(f"SELECT COUNT({coun}) FROM {fro}")
            toshow = f"SELECT COUNT({coun}) FROM {fro}"
        else:
            cur.execute(f"SELECT COUNT({coun}) FROM {fro} WHERE {wher}")
            toshow = f"SELECT COUNT({coun}) FROM {fro}"

        update_root_text(toshow)


        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)


        conn.commit()
        conn.close()
    
    c = Entry(top, width = 30)
    c.grid(row = 0, column=1, padx=10 , ipadx=10)
    c_label = Label(top, text = "COUNT")
    c_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# Create sum Function for database
def sum_db():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("SUM")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        su = s.get()
        fro = f.get()
        wher = w.get()

        if(wher == ''):
            cur.execute(f"SELECT SUM({su}) FROM {fro}")
            toshow = f"SELECT SUM({su}) FROM {fro}"
        else:
            cur.execute(f"SELECT SUM({su}) FROM {fro} WHERE {wher}")
            toshow = f"SELECT SUM({su}) FROM {fro} WHERE {wher}"

        update_root_text(toshow)

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
    
    s = Entry(top, width = 30)
    s.grid(row = 0, column=1, padx=10 , ipadx=10)
    s_label = Label(top, text = "SUM")
    s_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# Create max Function for database
def max_db():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("MAX")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        ma = m.get()
        fro = f.get()
        wher = w.get()

        if(wher == ''):
            cur.execute(f"SELECT MAX({ma}) FROM {fro}")
            toshow = f"SELECT MAX({ma}) FROM {fro}"
        else:
            cur.execute(f"SELECT MAX({ma}) FROM {fro} WHERE {wher}")
            toshow = f"SELECT MAX({ma}) FROM {fro} WHERE {wher}"

        update_root_text(toshow)

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"

        update_root_label(print_records)

        conn.commit()
        conn.close()
    
    m = Entry(top, width = 30)
    m.grid(row = 0, column=1, padx=10 , ipadx=10)
    m_label = Label(top, text = "MAX")
    m_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# Create min Function for database
def min_db():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("MIN")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        mi = m.get()
        fro = f.get()
        wher = w.get()

        if(wher == ''):
            cur.execute(f"SELECT MIN({mi}) FROM {fro}")
            toshow = f"SELECT MIN({mi}) FROM {fro}"
        else:
            cur.execute(f"SELECT MIN({mi}) FROM {fro} WHERE {wher}")
            toshow = f"SELECT MIN({mi}) FROM {fro} WHERE {wher}"

        update_root_text(toshow)

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
    
    m = Entry(top, width = 30)
    m.grid(row = 0, column=1, padx=10 , ipadx=10)
    m_label = Label(top, text = "MIN")
    m_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# Create avg Function for database
def avg_db():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("AVG")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        av = a.get()
        fro = f.get()
        wher = w.get()

        if(wher == ''):
            cur.execute(f"SELECT AVG({av}) FROM {fro}")
            toshow = f"SELECT AVG({av}) FROM {fro}"
        else:
            cur.execute(f"SELECT AVG({av}) FROM {fro} WHERE {wher}")
            toshow = f"SELECT AVG({av}) FROM {fro} WHERE {wher}"

        update_root_text(toshow)

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)

        conn.commit()
        conn.close()
    
    a = Entry(top, width = 30)
    a.grid(row = 0, column=1, padx=10 , ipadx=10)
    a_label = Label(top, text = "AVERAGE")
    a_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# Create having Function for database
def having_db():
    top= Toplevel(root)
    top.geometry("600x250")
    top.title("HAVING")
    top.resizable(width=False, height=False)

    def submit_command():
        conn = sqlite3.connect('petshop.db')
        cur = conn.cursor()

        sel = s.get()
        fro = f.get()
        wher = w.get()
        gro = g.get()
        hav = h.get()
        

        if(wher == ''):
            cur.execute(f"SELECT {sel} FROM {fro} GROUP BY {gro} HAVING {hav}")
            toshow = f"SELECT {sel} FROM {fro} GROUP BY {gro} HAVING {hav}"
        else:
            cur.execute(f"SELECT {sel} FROM {fro} WHERE {wher} GROUP BY {gro} HAVING {hav}")
            toshow = f"SELECT {sel} FROM {fro} WHERE {wher} GROUP BY {gro} HAVING {hav}"

        update_root_text(toshow)

        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        
        update_root_label(print_records)
        
        conn.commit()
        conn.close()
    
    s = Entry(top, width = 30)
    s.grid(row = 0, column=1, padx=10 , ipadx=10)
    s_label = Label(top, text = "SELECT")
    s_label.grid(row = 0, column=0, ipadx=10)

    f = Entry(top, width = 30)
    f.grid(row = 1, column=1, padx=10 , ipadx=10)
    f_label = Label(top, text = "FROM")
    f_label.grid(row = 1, column=0, ipadx=10)

    w = Entry(top, width = 30)
    w.grid(row = 2, column=1, padx=10 , ipadx=10)
    w_label = Label(top, text = "WHERE")
    w_label.grid(row = 2, column=0, ipadx=10)

    g = Entry(top, width = 30)
    g.grid(row = 3, column=1, padx=10 , ipadx=10)
    g_label = Label(top, text = "GROUP BY")
    g_label.grid(row = 3, column=0, ipadx=10)

    h = Entry(top, width = 30)
    h.grid(row = 4, column=1, padx=10 , ipadx=10)
    h_label = Label(top, text = "HAVING")
    h_label.grid(row = 4, column=0, ipadx=10)

    submitbt = Button(top, text = "Submit", command = submit_command)
    submitbt.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# Create having Function for database
def submit():
    # into database
    # Create a database or connect to one
    conn = sqlite3.connect('petshop.db')
    # create a cursor
    cur = conn.cursor()

    command = show_command.get('1.0',END) 
    print(command)
    a = command
    # Insert into Table 
    cur.execute(f"{a}")

    records = cur.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    
    update_root_label(print_records)

    # commit change 
    conn.commit()
    # Close connection
    conn.close()




# basic
# create text boxes
# messagebox = Text(root,width=80,height=5)
messagebox = Entry(root,width=10)
messagebox.grid(row=0, column=0, pady=10, padx=10, ipadx=30)

# create insert button
insert_btn = Button(root, text = "INSERT", command = insert)
insert_btn.grid(row=0, column=1, pady=10, padx=10, ipadx=30)

# create select_from_where button
select_from_where_btn = Button(root, text = "SELECT-FROM-WHERE", command = select_from_where)
select_from_where_btn.grid(row=0, column=2, pady=10, padx=10, ipadx=30)

# create delete button
delete_btn = Button(root, text = "DELETE", command = delete)
delete_btn.grid(row=0, column=3, pady=10, padx=10, ipadx=30)

# create update button
update_btn = Button(root, text = "UPDATE", command = update)
update_btn.grid(row=0, column=4, pady=10, padx=10, ipadx=30)

#nest
# create submit button
is_in_btn = Button(root, text = "IN", command = is_in)
is_in_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=30)

# create submit button
not_in_btn = Button(root, text = "NOT IN", command = not_in)
not_in_btn.grid(row=1, column=1, pady=10, padx=10, ipadx=30)

# create submit button
exists_btn = Button(root, text = "EXISTS", command = exists)
exists_btn.grid(row=1, column=2, pady=10, padx=10, ipadx=30)

# create submit button
not_exists_btn = Button(root, text = "NOT EXISTS", command = not_exists)
not_exists_btn.grid(row=1, column=3, pady=10, padx=10, ipadx=30)

# Aggregate
# create count_db button
count_btn = Button(root, text = "COUNT", command = count_db)
count_btn.grid(row=2, column=0, pady=10, padx=10, ipadx=30)

# create sum_db button
sum_btn = Button(root, text = "SUM", command = sum_db)
sum_btn.grid(row=2, column=1, pady=10, padx=10, ipadx=30)

# create max_db button
max_btn = Button(root, text = "MAX", command = max_db)
max_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=30)

# create min_db button
min_btn = Button(root, text = "MIN", command = min_db)
min_btn.grid(row=2, column=3, pady=10, padx=10, ipadx=30)

# create avg_db button
avg_btn = Button(root, text = "AVG", command = avg_db)
avg_btn.grid(row=2, column=4, pady=10, padx=10, ipadx=30)

# create having_db button
having_btn = Button(root, text = "HAVING", command = having_db)
having_btn.grid(row=2, column=5, pady=10, padx=10, ipadx=30)


# create submit button
submit_btn = Button(root, text = "SUBMIT", command = submit,width=10,height=5)
submit_btn.place(x=800, y=250)




root.mainloop()