from flask import Flask, render_template, request
from custom_modules.api_functions import import_cars_by_brand


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return "This is about Dirk"


@app.route('/car_brands', methods=['GET', 'POST'])
def car_brands():

    if request.method == 'POST':
        # get the value from the form
        selected_brand = request.form.get('brand')


        # execute the api function
        cars_list = import_cars_by_brand(selected_brand)
        return render_template("car_brands.html", cars_list=cars_list)
    

    return render_template("car_brands.html")


if __name__ == "__main__":
    app.run()