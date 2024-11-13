from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
