from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title="Главная страница")

@app.route("/about")
def about():
    return render_template('aboutUs.html', title="Про нас")
@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title="Галерея")

@app.route("/catalog")
def catalog():
    return render_template('katalog.html', title="Каталог")

@app.route("/registration")
def registration():
    return render_template('registration.html', title="Регистрация")

@app.route("/trash")
def trash():
    return render_template('trash.html', title="Корзина")


if __name__ == "__main__":
    app.run(debug=True)
