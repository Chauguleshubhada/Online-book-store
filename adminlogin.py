import mysql.connector
from flask import render_template,request,redirect,url_for,session


def login():
    if request.method == "GET":
        return render_template("adminLogin.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        sql = '''select count(*) from userinfo where username=
                    %s and  password=%s and role=%s'''
        con = mysql.connector.connect(host="localhost",user="root",password="shubhada",database="onlinebookstore")
        cursor = con.cursor() 
        val = (uname,pwd,'admin')       
        cursor.execute(sql,val)
        count = cursor.fetchone()
        if(int(count[0]) == 1):
            session["uname"]=uname
            return redirect("/adminHome")
        else:
            return redirect(url_for("adminLogin"))
        

def adminHome():
    if "uname" in session:
        return render_template("adminHome.html")
    else:
        return redirect(url_for("adminLogin"))
    
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        mobile_number = request.form["mobile_number"]
        msg = request.form["message"]
        con = mysql.connector.connect(host="localhost", user="root", password="shubhada", database="onlinebookstore")
        cursor = con.cursor()
        val = (name, email, mobile_number, msg)
        sql = "INSERT INTO contact (name, email, mobile_number, message) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, val)
        con.commit()
        con.close() 
        message = "Message sent successfully!"
    return render_template("homepage.html",message= message )

def showcontact():
    con = mysql.connector.connect(host="localhost", user="root", password="shubhada", database="onlinebookstore")
    cursor = con.cursor()
    sql = "select * from contact"
    cursor.execute(sql)
    contacts= cursor.fetchall()
    con.close() 
    return render_template("message.html",contacts = contacts)

