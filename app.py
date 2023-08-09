from flask import Flask, jsonify
import uuid

app = Flask(__name__)

rooms = []

@app.route('/ping')
def flask_status():

    return jsonify('Flask is up')

@app.route('/join')
def join():

  return jsonify('Joining a room')

@app.route('/create')
def create():
  room_id = str(uuid.uuid4())
  #print(room_id)
  return jsonify(f'You created room: {room_id}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
