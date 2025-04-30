from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "leer", "done": False },
    { "label": "pintar", "done": True }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos), 200
    return jsonify({"error": "Index out of range"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
