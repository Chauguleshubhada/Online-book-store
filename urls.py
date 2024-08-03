from main import app
import category_op as category
import book_op as book
import adminlogin as admin
import user as u

#--------------------Category Operation URLS--------------------------------------
app.add_url_rule("/addCategory",view_func=category.addCategory,methods=["GET","POST"])
app.add_url_rule("/showAllCategory",view_func=category.showAllCategory)
app.add_url_rule("/deleteCategory/<id>",view_func=category.deleteCategory,methods=["GET","POST"])
app.add_url_rule("/editCategory/<id>",view_func=category.editCategory,methods=["GET","POST"])

#-------------------Book operations URLS-----------------------------------------------
app.add_url_rule("/AddBooks",view_func=book.AddBooks , methods=["GET","POST"])
app.add_url_rule("/ShowAllBooks",view_func=book.ShowAllBooks)
app.add_url_rule("/showAuthor",view_func=book.showAuthor)
app.add_url_rule("/EditBook/<id>",view_func=book.EditBook , methods=["GET","POST"])
app.add_url_rule("/DeleteBook/<id>",view_func=book.DeleteBook,methods=["GET","POST"])

#------------------admin lOGIN URLS----------------------------------------------------------
app.add_url_rule("/adminLogin",view_func=admin.login,methods=["GET","POST"])
app.add_url_rule("/adminHome",view_func=admin.adminHome)
app.add_url_rule("/contact",view_func=admin.contact,methods=["GET","POST"])
app.add_url_rule("/showcontact",view_func=admin.showcontact)

#------------------users login urls-----------------------------------
app.add_url_rule("/",view_func=u.homepage)
app.add_url_rule("/showbooks/<cid>",view_func=u.showbooks)
app.add_url_rule("/Login",view_func=u.Login,methods=["GET","POST"])
app.add_url_rule("/Logout",view_func=u.Logout,methods=["GET","POST"])
app.add_url_rule("/Register",view_func=u.Register,methods=["GET","POST"])
app.add_url_rule("/ViewDetails/<book_id>",view_func=u.ViewDetails,methods=["GET","POST"])
app.add_url_rule("/showCartItems",view_func=u.showCartItems,methods=["GET","POST"])
app.add_url_rule("/MakePayment",view_func=u.MakePayment,methods=["GET","POST"])
app.add_url_rule("/like/<book_id>",view_func=u.user_like,methods=["GET","POST"])
app.add_url_rule("/showlikes",view_func=u.showlikes,methods=["GET","POST"])
app.add_url_rule("/account",view_func=u.account,methods=["GET","POST"])
app.add_url_rule("/forgotpassword",view_func=u.forgotpassword,methods=["GET","POST"])
app.add_url_rule("/showSave",view_func=u.showSave,methods=["GET","POST"])
app.add_url_rule("/user_save",view_func=u.user_save,methods=["GET","POST"])
