import mysql.connector
from flask import render_template,request,redirect,url_for,session,make_response,flash

def homepage():
    con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
    cursor = con.cursor()
    sql = '''select book_id,book_name,price,author_name,description,book_img,cat.category_name 
            from books as b inner join book_category as cat  
            on b.category_id = cat.category_id;'''
    cursor.execute(sql)
    books = cursor.fetchall()
    book_cat = "select * from book_category"
    cursor.execute(book_cat)
    cats = cursor.fetchall()
    return render_template("homepage.html",books=books,cats= cats)

def showbooks(cid):
    con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
    cursor = con.cursor()
    sql = '''select * from books_vw where cat_id = %s'''
    val= (cid,) 
    cursor.execute(sql,val)

    books = cursor.fetchall()
    book_cat = "select * from book_category"
    cursor.execute(book_cat)
    cats = cursor.fetchall()
    return render_template("homepage.html",books=books,cats=cats)

    
def Login():
    if request.method == "GET":
        return render_template("Login.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        sql = '''select count(*) from userinfo where username=
                    %s and  password=%s and role=%s'''
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor() 
        val = (uname,pwd,'user')       
        cursor.execute(sql,val)
        count = cursor.fetchone()
        if(int(count[0]) == 1):
            session["uname"]=uname
            return redirect("/")            
        else:
            return redirect(url_for("Login"))
        
def Register():
    if request.method == "GET":
        return render_template("Register.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        email = request.form["email"]
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "insert into UserInfo (username,password,email_id,role) values (%s,%s,%s,%s)"
        val = (uname,pwd,email,'user')
        try:
            cursor.execute(sql,val)
        except:
            message = "User already exists!!"
            return render_template("Register.html",message=message)
        else:
            con.commit()
        return redirect("/Login")

def forgotpassword():
    if request.method == "GET":
        return render_template("forgotpassword.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
         # Check if the username exists in the database
        sql_check = "SELECT COUNT(*) FROM UserInfo WHERE username = %s"
        val_check = (uname,)
        cursor.execute(sql_check, val_check)
        result = cursor.fetchone()[0]
        
        if result == 0:
            flash("Username does not exist. Please try again.")
            return redirect("/forgotpassword")
        else:
            sql_fetch_role = "SELECT role FROM UserInfo WHERE username = %s"
            cursor.execute(sql_fetch_role, (uname,))
            role = cursor.fetchone()[0]

            sql = "update UserInfo set password = %s where username = %s "
            val = (pwd,uname)
            cursor.execute(sql,val)
            con.commit()
            
            if role == 'user':
                flash("Password updated successfully.")
                return redirect("/Login")
            else:
                flash("Password updated successfully.")
                return redirect("/adminLogin")
            
    
def Logout():
    session.clear()
    return redirect("/")

def ViewDetails(book_id):
    if request.method == "GET":
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = '''select * from books_vw where book_id=%s'''
        val = (book_id,)
        cursor.execute(sql,val)
        book = cursor.fetchone()
        return render_template("ViewDetails.html",book=book)
    else:
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        uname = session["uname"]
        qty = request.form["qty"]
        if "uname" in session:            
            sql = "select count(*) from mycart where username=%s and book_id=%s"
            val = (session["uname"],book_id)
            cursor.execute(sql,val)
            count = cursor.fetchone()
            if(int(count[0]) == 1):
                message = "Item already in cart"
            else:
                sql = "insert into MyCart (username,book_id,qty) values (%s,%s,%s)"
                val = (uname,book_id,qty)
                cursor.execute(sql,val)
                con.commit()
                message = "Item added to cart successfully"   
            return redirect(url_for("showCartItems",message=message))
        else:
            return redirect("/Login")
  

def showCartItems():
    if request.method == "GET":
        if "uname" in session:     
            if "message" in request.args :
                message = request.args["message"]
            else:
                message = ""
            uname = session["uname"]
            sql = "select * from Cart_vw where username=%s"
            val = (uname,)
            con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
            cursor = con.cursor()
            cursor.execute(sql,val)
            items = cursor.fetchall()

            sql = "select sum(subtotal) from cart_vw where username=%s"
            val = (session["uname"],)
            cursor.execute(sql,val)
            total = cursor.fetchone()[0]
            session["total"] = total

            return render_template("Cart.html",items=items,message=message)
        else:
            return redirect("/Login")
    else:
        action = request.form["action"]
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        if action == "update":
            qty = request.form["qty"]
            sql = "update MyCart set qty = %s where username=%s and book_id=%s"
            val =  ( qty,session["uname"],request.form["book_id"])            
            cursor.execute(sql,val)
            con.commit()    
        else:
            sql = "delete from MyCart where username=%s and book_id=%s"
            val = ( session["uname"],request.form["book_id"])            
            cursor.execute(sql,val)
            con.commit()
        return redirect("/showCartItems")
    
def MakePayment():
    if request.method == "GET":
        return render_template("Makepayment.html")
    else:
        cardno = request.form["cardno"]
        cvv = request.form["cvv"]
        expiry = request.form["expiry"]
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "select count(*) from payment where cardno=%s and cvv=%s and expiry=%s"
        val = (cardno,cvv,expiry)
        cursor.execute(sql,val)
        count = int(cursor.fetchone()[0])
        if count == 1:
            total = session["total"]
            #Perform transaction
            sql1 = "update payment set balance = balance - %s where cardno=%s and cvv=%s and expiry=%s"
            val1 = (total,cardno,cvv,expiry)
            sql2 = "update payment set balance = balance + %s where cardno=%s and cvv=%s and expiry=%s"
            val2 = (total,'5111111111111111','123','12/2031')
            cursor.execute(sql1,val1)
            cursor.execute(sql2,val2)

            # Clear the user's cart after successful payment
            sql_clear_cart = "delete from MyCart where username=%s"
            val_clear_cart = (session["uname"],)
            cursor.execute(sql_clear_cart, val_clear_cart)

            con.commit()
            return redirect("/")
        else:
            return redirect(url_for("MakePayment"))
        
def connect_to_database():
    return mysql.connector.connect(host="localhost", user="root", password="shubhada", database="onlinebookstore")

def user_like(book_id):
        if 'uname' in session:
            con = connect_to_database()
            cursor = con.cursor()
            uname = session["uname"]
            cursor.execute("SELECT COUNT(*) FROM user_likes WHERE username = %s AND book_id = %s", (uname, book_id))
            count = cursor.fetchone()[0]

            if count == 0:
                cursor.execute("INSERT INTO user_likes (username, book_id) VALUES (%s, %s)", (uname, book_id))
                con.commit()
                message = "Item added to liked items successfully"
            else:
                message = "Item already liked"

            cursor.close()
            con.close()
            return redirect(url_for("showlikes", message=message))
        else:
            return redirect("/Login") 

def showlikes():
    if request.method == "GET":
        if "uname" in session:     
            if "message" in request.args :
                message = request.args["message"]
            else:
                message = ""
            uname = session["uname"]
            sql = "select * from userlikes_vw where username=%s"
            val = (uname,)
            con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
            cursor = con.cursor()
            cursor.execute(sql,val)
            items = cursor.fetchall()

            return render_template("showlikes.html",items=items,message=message)
        else:
            return redirect("/Login")
    else:
        action = request.form["action"]
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()

        if action == "delete":
            sql = "delete from user_likes where username=%s and book_id=%s"
            val = ( session["uname"],request.form["book_id"])            
            cursor.execute(sql,val)
            con.commit()
        return redirect("/showlikes")
    
def account():
    if "uname" in session:
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = '''select * from userinfo where role ="user" and username = %s '''
        val = (session["uname"],)
        cursor.execute(sql,val)
        users = cursor.fetchone()
        return render_template("account.html",users=users)
    else:
        return redirect("/Login")

def user_save(book_id):
        if 'uname' in session:
            con = connect_to_database()
            cursor = con.cursor()
            uname = session["uname"]
            cursor.execute("SELECT COUNT(*) FROM save WHERE username = %s AND book_id = %s", (uname, book_id))
            count = cursor.fetchone()[0]

            if count == 0:
                cursor.execute("INSERT INTO save (username, book_id) VALUES (%s, %s)", (uname, book_id))
                con.commit()
                message = "Item added to save later"
            else:
                message = "Item already saved"

            cursor.close()
            con.close()
            return redirect(url_for("showSave", message=message))
        else:
            return redirect("/Login") 

def showSave():
    if request.method == "GET":
        if "uname" in session:     
            if "message" in request.args :
                message = request.args["message"]
            else:
                message = ""
            uname = session["uname"]
            sql = "select * from save_vw where username=%s"
            val = (uname,)
            con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
            cursor = con.cursor()
            cursor.execute(sql,val)
            items = cursor.fetchall()

            return render_template("saves.html",items=items,message=message)
        else:
            return redirect("/Login")
    else:
        action = request.form["action"]
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()

        if action == "delete":
            sql = "delete from save where username=%s and book_id=%s"
            val = ( session["uname"],request.form["book_id"])            
            cursor.execute(sql,val)
            con.commit()
        return redirect("/showSave")