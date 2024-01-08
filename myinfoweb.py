from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Замените эти данные своими
    personal_info = {
        'name': 'Владимир',
        'surname': "Толокнов",
        'age': '18',
        'city': 'Омск',
        'about_me': 'студент-первокурсник',
    }
    image_path = 'static/profile_picture.jpg'

    # Встроенные строки HTML и стилей в коде Python
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Обо мне</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }}
                .container {{
                    max-width: 800px;
                    margin: 20px auto;
                    background-color: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    text-align: center;
                }}
                #personal-info {{
                    text-align: center;
                }}
                img {{
                    max-width: 100%;
                    border-radius: 70%;
                    margin-bottom: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Моя страница</h1>
                <div id="personal-info">
                    <img src="{image_path}" alt="фото">
                    <p><strong>Имя:</strong> {personal_info['name']}</p>
                    <p><strong>Фамилия:</strong> {personal_info['surname']}</p>
                    <p><strong>Возраст:</strong> {personal_info['age']}</p>
                    <p><strong>Город:</strong> {personal_info['city']}</p>
                    <p><strong>Обо мне:</strong> {personal_info['about_me']}</p>
                </div>
            </div>
        </body>
        </html>
    """

if __name__ == '__main__':
    # Замените host и port на необходимые значения
    app.run(host='0.0.0.0', port=8800, debug=True)
