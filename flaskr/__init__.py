import os

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "./uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024 # 16 MB

ALLOWED_EXTENSIONS = {"snbt", "zip"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"])
def page():
    if request.method == "POST":
        if "files[]" not in request.files:
            flash("No file part")
            return redirect(request.url)
        
        files = request.files.getlist("files[]")
        if not files or all(f.filename == "" for f in files):
            flash("No selected file")
            return redirect(request.url)
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                flash(f"{filename} uploaded successfully!")
    return render_template("index.html")