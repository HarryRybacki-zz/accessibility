from flask import render_template
from main import app

# Begin view routes
@app.route('/')
@app.route('/index/')
def index():
    """Landing page for SES200 Accessibility Web Practices"""
    return render_template("index.html")

@app.route('/generic_image_examples/')
def generic_images():
    return render_template("generic_image_examples.html")

@app.route('/graph_image_examples/')
def graph_images():
    return render_template("graph_image_examples.html")