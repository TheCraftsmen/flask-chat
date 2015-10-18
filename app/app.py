from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
from models import *


@app.route('/',  methods=['GET', 'POST'])
def home():
    chat_query = Chat.query.all()
    if request.method == 'POST':
        print request.form
        ch = Chat(user=request.form['user'],message=request.form['message'])
        db.session.add(ch)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('index.html', chats=chat_query)

if __name__ == '__main__':
    app.run(debug=True)
