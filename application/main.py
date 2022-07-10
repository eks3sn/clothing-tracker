from tkinter.tix import Select
from unicodedata import category
from xxlimited import new
from flask import Flask, render_template, request, flash, url_for, redirect
from testing import *
from xmlrpc.client import DateTime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'jd is crow king'
migrate = Migrate(app, db)




class Clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), unique=False, nullable=False) # category = top, etc.
    type = db.Column(db.String(80), unique=False, nullable=False) # type = tank top, t shirt, etc.
    color = db.Column(db.String(80), unique=False, nullable=False)
    brand = db.Column(db.String(80), unique=False, nullable=False)
    wears = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    #time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self) -> str:
        return "(%s, %s, %s)" % (self.type, self.brand, self.color)



@app.route('/') 
def hello():
    return render_template('home.html')


@app.route('/closet/all') 
def all():
    return render_template('all.html', my_list = Clothes.query.all())


@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        if not request.form['category'] or not request.form['type'] or not request.form['color']:
            flash('Please enter all the fields', 'error')
        else:
         new_item = Clothes(category=request.form['category'],type=request.form['type'], color=request.form['color'], brand=request.form['brand'],wears=0)
         
         db.session.add(new_item)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('all'))
    return render_template('add.html')


class enter_wears_form(FlaskForm):
    category = SelectField('category', choices =[('Top','Top'),('Bottom','Bottom'),('Gym','Gym'),('Outerwear','Outerwear')])
    type = SelectField('type',choices=[])
    brand = SelectField('brand',choices=[])
    color = SelectField('color',choices=[])


@app.route('/wears', methods = ['GET', 'POST'])
def enter_wears():
    form = enter_wears_form()
    form.type.choices = [(Clothes.id, Clothes.type)for Clothes in Clothes.query.filter_by
                                    (category='top').all()]
    form.brand.choices = [(Clothes.id, Clothes.brand)for Clothes in Clothes.query.filter_by
                                    (category='top',type='tank top',).all()]
    form.color.choices = [(Clothes.id, Clothes.color)for Clothes in Clothes.query.filter_by
                                    (category='top',type='tank top',brand='aritzia').all()]

    return render_template('wears.html', form=form)