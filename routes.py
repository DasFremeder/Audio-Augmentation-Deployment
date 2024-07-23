#!/usr/bin/env python3

from flask import Blueprint, abort, render_template, request, current_app
from audio_augmentation_website.augmentation import search_for_method, bulk_process
main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    return render_template(
        "index.html"
    )

@main.post("/checkbox")
def get_augmentation_methods():
    if request.method == "POST":
        f = request.files["file"] 
        f.save(f"audio_augmentation_website/output/{f.filename}")   
        return render_template("checkbox.html")

@main.post("/process")
def process():
    if request.method == "POST":
        print(request.form)
        return render_template("loading.html")

# @main.get("/login")
# def get_index():
#     return render_template(
#         "login.html"
#     )
# @main.get("/loading")
# def get_index():
#     return render_template(
#         "loading.html"
#     )
# @main.get("/done")
# def get_index():
#     return render_template(
#         "finished.html"
#     )


@main.get("/function/<string:function_name>")
def parameter_api(function_name: str):
    print(function_name)
    _, plist = search_for_method(function_name)
    return plist

