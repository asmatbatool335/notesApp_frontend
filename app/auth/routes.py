from flask import render_template, redirect, url_for, flash
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')

@auth_bp.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home')) 