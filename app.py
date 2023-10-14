from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to SQLite database
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Render HTML template and pass items to it
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
