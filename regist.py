from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Регистрация нового пользователя
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    email = data['email']
    password = data['password']  # Лучше захэшировать пароль!

    # Подключение к базе данных
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Сохраняем данные
    cursor.execute('INSERT INTO users (username, email, password, telegram_id) VALUES (?, ?, ?, ?)',
                   (username, email, password, t.me/CrispRegistrationBot))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "User registered successfully!"})

if __name__ == '__main__':
    app.run(debug=True)