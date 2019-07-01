from flask import Flask, render_template, url_for, redirect
import os
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Category, File

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/challenge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

'''
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)
    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    def __init__(self, name):
        self.name = name

db.create_all()
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()
'''

@app.route('/')
def index():
    title_list = []
    the_data = {}
    the_files = File.query.all()    
    for the_file in the_files:
        the_data['id'] = the_file.id
        the_data['title'] = the_file.title        
        title_list.append(the_data)
        the_data = {}
    return render_template('index.html', titles=title_list)

@app.route('/files/<int:file_id>')
def file(file_id):
    the_files = File.query.all()
    id_list = []
    dict_data = {}
    for the_file in the_files:
        id_list.append(the_file.id)
    if file_id in id_list:
        one_file = File.query.get(file_id)
        dict_data['content'] = one_file.content
        dict_data['created_time'] = one_file.created_time
        the_category = Category.query.get(one_file.category_id)
        dict_data['category'] = the_category.name
        return render_template('file.html', the_data=dict_data)
    else:        
        return redirect('not_found')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', the_str='shiyanlou 404'), 404

if __name__ == '__main__':
    app.run()
