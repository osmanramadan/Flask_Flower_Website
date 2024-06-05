
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Product, Basket
from  app import create_app



	

app =create_app()

# app = Flask(__name__,template_folder='app/templates')

# @app.route('/')
# def home():
#     # products = Product.query.all()
#     # print(products,'______+++++++++++++_____________________________________>>>>>>>>>')
#     return render_template('home.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         username = request.form.get('username')
#         print(email,username,'0---------------------------')
#         password = request.form.get('password')
#         user = User.query.filter_by(email=email).first()
#         print(user,'USER USET---------------------------> SUUSER')
#         if user and check_password_hash(user.password, password):
#             login_user(user)
            
#             return redirect(url_for('home.html'))
#         else:
#             flash('Login failed. Check your credentials.')
    
#     return render_template('login.html')



if __name__ == "__main__": 
	app.run(debug=True) 
