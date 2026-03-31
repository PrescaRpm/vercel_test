from flask import Flask, render_template
from modules.bio_provider import get_biography_data

app = Flask(__name__)

@app.route('/')
def index():
    my_bio = get_biography_data()
    return render_template('index.html', data=my_bio)

if __name__ == "__main__":
    app.run(debug=True)
