from .core import app
from .core import find_user
from flask import Flask, render_template, request, url_for, redirect

vk_id = []


@app.route("/main", methods=["GET"])
def main():

    try:
        id_v = vk_id[-1]
        status_vk = find_user(id_v)

    except Exception as ex:
        print(ex)
        status_vk = ""

    return render_template("index.html", status=status_vk)


@app.route("/add_id", methods=["POST"])
def add_id():

    input_text = request.form["user_id"]
    vk_id.append(input_text)

    return redirect(url_for("main"))

