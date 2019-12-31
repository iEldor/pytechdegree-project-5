from application import app
from flask import render_template, url_for
import models

entry_list = [ 
        {'id': 1, 'title': 'The best day I\'ve ever had', 'date': '2016-01-31'},
        {'id': 2, 'title': 'The absolute worst day I\'ve ever had', 'date': '2016-01-31'},
        {'id': 3, 'title': 'That time at the mall', 'date': '2016-01-31'},
        {'id': 4, 'title': 'Dude, where\'s my car?', 'date': '2016-01-31'}
    ]

# / - Known as the root page, homepage, landing page but will act as the Listing route.
# /entries - Also will act as the Listing route just like /
@app.route('/')
@app.route('/entries')
def index():
    return render_template('index.html', entry_list = entry_list)

# /entries/<id> - The Detail route
@app.route('/entries/<id>')
def detail(id):
    return render_template('detail.html', id = id)

# /entries/new - The Create route

# /entries/<id>/edit - The Edit or Update route
# /entries/<id>/delete - Delete route