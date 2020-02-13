from .core import app

@app.route("/")
def main_page():
    return "main page"