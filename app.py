from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)



def query_db(search_term):
    # Connect to the database (or create if it doesn't exist)
    print(search_term)
    print(type(search_term))
    conn = sqlite3.connect("tap_breach_tests.db")
    cursor = conn.cursor()

    query = "SELECT * FROM data where email = ?"

    # Replace 'your_table' with the actual table name
    cursor.execute(query, (search_term,))

    print(search_term)

    # Fetch all rows from the table
    rows = cursor.fetchall()

    conn.close()


    return rows


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    search_term = request.form.get("search", "")
    results = query_db(search_term)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)