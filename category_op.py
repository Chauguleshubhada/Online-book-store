from flask import redirect, render_template, session, request,url_for
import mysql.connector

def addCategory():
    if request.method == "GET":
        return render_template("addCategory.html")
    else:
        category_name = request.form["category_name"]
        session["category_name"] = category_name 

        mydb = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="OnlineBookStore")
        cur = mydb.cursor()
        str = "insert into Book_Category (category_name) values (%s)"
        val = (category_name,)
        cur.execute(str,val)
        mydb.commit()
        mydb.close()
        return "inserted category!!!"

def showAllCategory():
        mydb = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="OnlineBookStore")
        cur = mydb.cursor()
        str = "select * from Book_Category"
        cur.execute(str)
        records = cur.fetchall()
        mydb.close()
        return render_template("showAllCategory.html",records= records)

def deleteCategory(id):
    if request.method == "POST":
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "delete from Book_Category where category_Id = %s"
        val = (id,)
        cursor.execute(sql,val)
        con.commit()
    return redirect(url_for("showAllCategory"))

def editCategory(id):
    if request.method == "GET":
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "select * from Book_Category where category_Id=%s"
        val = (id,)
        cursor.execute(sql,val)
        cat = cursor.fetchone()
        return render_template("Editcategory.html",cat=cat)
    else:
        category_name = request.form["category_name"]
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor()
        sql = "update Book_Category  set category_name =%s where category_Id=%s"
        val = (category_name,id)
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("showAllCategory"))