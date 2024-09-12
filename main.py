from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizza_price = [
        {"name": "Pizza1", "description": "Tomato, cheese", "price": 100},
        {"name": "Pizza Yoruichi", "description": "Pepperoni, cheese", "price": 150},
        {"name": "Pizza de IT", "description": "Pineapple, meat", "price": 120},
    ]

    return render_template('menu.html', **pizza_price)

if __name__ == '__main__':
    app.run(debug=True)