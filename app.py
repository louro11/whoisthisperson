from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (Replace with a database if needed)
items = ["Flask", "Django", "FastAPI", "Python", "JavaScript", "React", "Vue", "SQLAlchemy"]

@app.route("/", methods=["GET", "POST"])
def home():
    query = request.form.get("search", "").lower()
    results = [item for item in items if query in item.lower()] if query else []
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)