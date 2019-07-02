from flask import Flask, render_template, url_for, redirect
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    title_list = []
    dirname = '/home/shiyanlou/files'
    list_of_article = os.listdir(dirname)
    for the_article in list_of_article:
        with open(os.path.join(dirname, the_article), 'r') as f:
            dict_data = json.load(f)
            title_list.append(dict_data['title'])
    return render_template('index.html', titles=title_list)

@app.route('/files/<filename>')
def file(filename):
    dirname = '/home/shiyanlou/files'
    real_filename = filename + '.json'
    real_filedir = os.path.join(dirname, real_filename)
    if os.path.exists(real_filedir):
        with open(real_filedir, 'r') as f:
            dict_data = json.load(f)
        return render_template('file.html', the_data=dict_data)
    else:        
        return redirect('not_found')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', the_str='shiyanlou 404'), 404

if __name__ == '__main__':
    app.run()