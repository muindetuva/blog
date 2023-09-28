from app import app
from flask import render_template
from app.models import Article


@app.route('/')
@app.route('/index')
def index():

    user = {'username': 'Alfred Tuva'}

    return render_template('index.html', user=user)


@app.route('/articles')
def articles():

    articles = Article.query.all()

    return render_template('articles.html', articles=articles)
