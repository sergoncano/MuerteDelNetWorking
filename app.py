from flask import Flask, render_template, url_for, request
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    img = request.get_json()['image']
    image_data = base64.b64decode(img)
    with open("image.jpeg", "wb") as file:
        file.write(image_data)
    return ('OK!')

if __name__ == '__main__':
    app.run(debug=True)