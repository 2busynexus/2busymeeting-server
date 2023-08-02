from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def flask_status():

    return jsonify('Flask is up')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
