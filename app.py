from flask import Flask, request, jsonify

app = Flask(__name__)




@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


@app.route('/goodbye', methods=['GET'])
def goodbye():
    return jsonify({'messsage': 'Goodbye, World!'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
