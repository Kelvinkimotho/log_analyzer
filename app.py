from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import pandas as pd
from utils.log_parser import parse_logs
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "logs"
RESULT_FOLDER = "results"
ALLOWED_EXTENSIONS = {"log", "txt", "csv"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "logfile" not in request.files:
            return render_template("error.html", message="No file uploaded")

        file = request.files["logfile"]

        if file.filename == "":
            return render_template("error.html", message="No file selected")

        if not allowed_file(file.filename):
            return render_template("error.html", message="Invalid file type. Please upload a .log, .txt, or .csv file.")

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Analyze log file
        result_filename = parse_logs(filepath)
        return redirect(url_for("results", filename=result_filename, page=1))

    return render_template("index.html")

@app.route("/results/<filename>")
def results(filename):
    result_path = os.path.join(app.config["RESULT_FOLDER"], filename)
    df = pd.read_csv(result_path)

    # Get search query
    search_query = request.args.get("search", "").strip().lower()
    if search_query:
        df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(search_query).any(), axis=1)]

    # Pagination logic
    page = request.args.get("page", 1, type=int)
    per_page = 10
    total_pages = (len(df) // per_page) + (1 if len(df) % per_page > 0 else 0)

    # Get only the data for the current page
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    df_page = df.iloc[start_idx:end_idx]

    table_html = df_page.to_html(classes="table table-striped", index=False).replace("\n", "")

    return render_template(
        "results.html",
        tables=table_html,
        filename=filename,
        page=page,
        total_pages=total_pages,
        search_query=search_query
    )

@app.route("/download/<filename>")
def download(filename):
    result_path = os.path.join(app.config["RESULT_FOLDER"], filename)
    return send_file(result_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
