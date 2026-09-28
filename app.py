import os
from flask import Flask, request, render_template
from resume import extract_text
from resume_analyzer import model, prompt

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def upload_resume():

    if request.method == "POST":

        file = request.files["resume"]

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(file_path)

        text = extract_text(file_path)

        formatted_prompt = prompt.format(resume=text)

        response = model.invoke(formatted_prompt)

        feedback = response.text

        return render_template("index.html", feedback=feedback)

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)