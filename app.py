from flask import Flask, render_template, request, send_file
import process_data
from werkzeug.utils import secure_filename
import logging as log
import pandas as pd
from zipfile import ZipFile
import os

app = Flask(__name__)

log.basicConfig(filename='api.log', format='%(asctime)s', level=log.DEBUG)


@app.route("/")
def home():
    log.info("Inside home endpoint")
    return render_template("index.html")


@app.route("/uploader", methods=['POST'])
def upload_input():
    log.info("Inside upload_input endpoint")
    global file
    if request.method == 'POST':
        file = request.files["file_name"]
        file.save(secure_filename(file.filename))
        service = request.form.get("service_name")
        env = request.form.get("env_name")
        key = request.form.get("key_name")

        data = pd.read_csv(file.filename, sep='|', header=0)
        pass_df, fail_df = process_data.process_data(data, env, service, key)
        pass_df.to_csv("processed.csv")
        fail_df.to_csv("failed.csv")

        with ZipFile("output.zip", "w") as zipobj:
            zipobj.write("processed.csv")
            zipobj.write("failed.csv")

        os.remove("processed.csv")
        os.remove("failed.csv")
        os.remove(file.filename)
        del pass_df, fail_df

        return render_template("index.html", filed="download.html", logd="log_download.html",
                               reset="reset.html")


@app.route("/downloader")
def download_output():
    log.info("Inside download_input endpoint")
    return send_file("output.zip", attachment_filename="output.zip", as_attachment=True)


@app.route("/logdownload")
def download_log():
    log.info("Inside download_log endpoint")
    return send_file("api.log", attachment_filename="web_log.log", as_attachment=True)


@app.route("/reset")
def reset():
    log.info("Inside reset endpoint")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
