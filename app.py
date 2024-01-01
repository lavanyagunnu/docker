from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
def fetch_sketches_data():
    # Replace these with your actual database connection details
    db_params = {
        'dbname': 'lava_world',
        'user': 'postgres',
        'password': 'password123',
        'host': 'postgres',
        'port': '5432'
    }

    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Fetch data from the database
    query = sql.SQL("SELECT Date_created, Artist_name, Title, File_name, Id FROM sketches_data order by Id;")
    cursor.execute(query)
    result = cursor.fetchall()

    # Separate the fetched data into individual lists
    date_created_list = [row[0] for row in result]
    artist_name_list = [row[1] for row in result]
    title_list = [row[2] for row in result]
    images_list = [row[3] for row in result]
    id_list = [row[4] for row in result]
   


    # Close the database connection
    cursor.close()
    connection.close()

    return date_created_list, artist_name_list, title_list, images_list, id_list


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sketches')
def sketches():


    # Fetch the three lists from the database
    date_created_list, artist_name_list, title_list, images_list, id_list= fetch_sketches_data()

    # You should also pass these lists to the template
    return render_template('sketches.html', sketches_images=images_list,
                            date_created_list=date_created_list,
                            artist_name_list=artist_name_list,
                            title_list=title_list,
                            id_list=id_list)


@app.route('/edit_sketch/<int:sketch_id>', methods=['GET', 'POST'])
def edit_sketch(sketch_id):
    # Fetch sketch data for the specific ID
    db_params = {
        'dbname': 'lava_world',
        'user': 'postgres',
        'password': 'password123',
        'host': 'postgres',
        'port': '5432'
    }

    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    query = sql.SQL("SELECT Id, Date_created, Artist_name, Title, File_name FROM sketches_data WHERE Id = %s;")
    cursor.execute(query, (sketch_id,))
    sketch_data = cursor.fetchone()

    # Close the database connection
    cursor.close()
    connection.close()

    if request.method == 'POST':
        # Update the sketch with the new information
        new_title = request.form['title']

        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        update_query = sql.SQL("UPDATE sketches_data SET Title = %s WHERE Id = %s;")
        cursor.execute(update_query, (new_title, sketch_id))
        connection.commit()

        # Close the database connection
        cursor.close()
        connection.close()

        return redirect(url_for('sketches'))

    # Render the edit_sketch template with the sketch data
    return render_template('edit_sketch.html', sketch_id=sketch_id, sketch_data=sketch_data)


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
