from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    # Здесь можно добавить обработку данных (например, сохранение в БД)
    
    return jsonify({"message": f"Hello {name}, your email {email} has been received."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
