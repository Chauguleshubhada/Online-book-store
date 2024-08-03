from flask import redirect, render_template, request, session, url_for
import mysql.connector
from werkzeug.utils import secure_filename

def AddBooks():
    if request.method == "GET":
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "select * from Book_category"
        cursor.execute(sql)
        cats = cursor.fetchall()
        return render_template("addBooks.html",cats=cats)
    else:
        book_name = request.form["book_name"]
        price = request.form["price"]
        Author_Name = request.form["Author_Name"]
        description = request.form["description"]
        f = request.files['image'] 
        filename = secure_filename(f.filename)
        filename = "static/Images/"+f.filename
        #This will save the file to the specified location
        f.save(filename)   
        filename = "Images/"+f.filename
        category_id = request.form["book_category"]

        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "insert into Books (Book_name,price,Author_name,description,Book_img,category_Id) values (%s,%s,%s,%s,%s,%s)"
        val = (book_name,price,Author_Name,description,filename,category_id)
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("showAllBooks"))
        # return "book inserted"

def ShowAllBooks():
    con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
    cursor = con.cursor()
    sql = '''select book_id,book_name,price,author_name,description,book_img,cat.category_name 
            from books as b inner join book_category as cat  
            on b.category_id = cat.category_id;'''
    cursor.execute(sql)
    books = cursor.fetchall()
    return render_template("showAllBooks.html",books=books)

def DeleteBook(id):
    if request.method == "POST":
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "delete from Books where book_Id = %s"
        val = (id,)
        cursor.execute(sql,val)
        con.commit()
    return redirect(url_for("ShowAllBooks"))

def EditBook(id):
    if request.method == "GET":
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        # sql = "select * from Books where book_Id=%s"
        sql = '''select book_id,book_name,price,author_name,description,book_img,cat.category_name 
            from books as b inner join book_category as cat  
            on b.category_id = cat.category_id where book_id = %s;'''
        val = (id,)
        cursor.execute(sql,val)
        book = cursor.fetchone()
        return render_template("EditBook.html",book=book)
    else:
        book_name = request.form["book_name"]
        price = request.form["price"]
        Author_Name = request.form["Author_Name"]
        description = request.form["description"]
        f = request.files['image'] 
        filename = secure_filename(f.filename)
        filename = "static/Images/"+f.filename
        #This will save the file to the specified location
        f.save(filename)   
        filename = "Images/"+f.filename
        # category_id = request.form["book_category"]

        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "update Books  set Book_name=%s,price=%s,Author_name=%s,description=%s,Book_img=%s where book_Id=%s"
        val = (book_name,price,Author_Name,description,filename,id)
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("ShowAllBooks"))
    
def showAuthor():
    con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
    cursor = con.cursor()
    sql= "select distinct trim(author_name) from books;"
    cursor.execute(sql)
    books = cursor.fetchall()
    return render_template("showAuthor.html",books=books)
