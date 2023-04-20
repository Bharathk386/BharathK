from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/v1/sanitized/input/', methods=['POST'])
def check_input():
    # Get the input from the JSON payload
    payload = request.json.get('payload')

    # Check for SQL injection characters
    sql_injection_chars = ["'", ";", "--", "/*", "*/"]
    for char in sql_injection_chars:
        if char in payload:
            return jsonify({'result': 'unsanitized'})

    # If no SQL injection characters are found, return 'sanitized'
    return jsonify({'result': 'sanitized'})


if __name__ == '__main__':
    app.run(debug=True)
