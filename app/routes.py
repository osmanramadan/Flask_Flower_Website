from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Product, Basket
from . import db
# from flask_login import , UserMixin

# login_manager = LoginManager()


def register_routes(app):

 
    @app.route('/')
    def home():
        # products = Product.query.all()
        return render_template('home.html')
    
    @app.route('/payment')
    def paymentnow():
       
        return render_template('payment.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            print(user.email)
            if user.email:
                # login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Login failed. Check your credentials.')
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            # hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            # login_user(new_user)
            
            return redirect(url_for('home'))
        return render_template('register.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('home'))

    @app.route('/basket', methods=['GET', 'POST'])
    @login_required
    def basket():
        if request.method == 'POST':
            product_id = request.form.get('product_id')
            quantity = request.form.get('quantity')
            new_item = Basket(user_id=current_user.id, product_id=product_id, quantity=quantity, payment_method='')
            db.session.add(new_item)
            db.session.commit()
        basket_items = Basket.query.filter_by(user_id=current_user.id).all()
        return render_template('basket.html', items=basket_items)

    @app.route('/payment', methods=['GET', 'POST'])
    @login_required
    def payment():
        if request.method == 'POST':
            payment_method = request.form.get('payment_method')
            items = Basket.query.filter_by(user_id=current_user.id).all()
            for item in items:
                item.payment_method = payment_method
            db.session.commit()
            flash('Payment successful!')
            return redirect(url_for('home'))
        return render_template('payment.html')

    @app.route('/admin')
    @login_required
    def admin():
        if current_user.username != 'admin':
            return redirect(url_for('home'))
        users = User.query.all()
        baskets = Basket.query.all()
        return render_template('admin.html', users=users, baskets=baskets)
