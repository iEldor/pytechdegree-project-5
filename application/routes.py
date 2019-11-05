from application import app
from flask import render_template

# / - Known as the root page, homepage, landing page but will act as the Listing route.
# /entries - Also will act as the Listing route just like /
@app.route('/')
@app.route('/entries')
def index():
    return render_template('index.html')

# /entries/<id> - The Detail route
@app.route('/entries/<id>')
def detail(id):
    return render_template('detail.html')

# /entries/new - The Create route

# /entries/<id>/edit - The Edit or Update route
# /entries/<id>/delete - Delete route