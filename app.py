from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sketches')
def sketches():
    # Path to the sketches folder
    sketches_folder = os.path.join(app.static_folder, 'sketches')

    # Get a list of all files in the sketches folder
    sketches_images = [f for f in os.listdir(sketches_folder)  if os.path.isfile(os.path.join(sketches_folder, f))]

    return render_template('sketches.html', sketches_images=sketches_images)



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
