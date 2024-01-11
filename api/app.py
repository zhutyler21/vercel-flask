from flask import Flask, render_template, request, send_from_directory
from PIL import Image, ImageFilter
import os

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "static/images/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            # save the image
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            # read the image via PIL
            img = Image.open(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            # apply image filters
            img = img.convert('L') # convert image to grayscale
            img = img.filter(ImageFilter.BLUR) # blur the image

            # save the image
            img.save(os.path.join(app.config["IMAGE_UPLOADS"], 'processed_'+image.filename))

            return render_template("index.html", image='processed_'+image.filename)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.config["IMAGE_UPLOADS"], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)