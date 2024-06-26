from flask import Flask,render_template 
import sqlite3


app = Flask(__name__)

#this is the route to the home page/landing page

@app.route('/')
def landingpage():
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('select * FROM car')
    results = cur.fetchall()
    print(results)
    return render_template("landing_page.html", title="home", results=results)

@app.route('/car/<int:car_id>')
def carinfo(car_id):  
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('select car.make, car.model, car.engine, car.stockhp, car.stocktorque, make.whatmake, engine.engine_name, car.image from car join make on car.make = make.make_id join engine on car.engine = engine.engine_id WHERE car_id=?', (car_id,))
    results = cur.fetchall()
    print(results)
    return render_template("carinfo.html", title="car", results=results)
   # return render_template('carinfo.html')


# renders make table
@app.route('/make')
def make():
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM make')
    results = cur.fetchall()
    print(results)
    return render_template('make.html', title="make", results=results)
   #return render_template('make.html')


@app.route('/make/<int:make_id>')
def makes(make_id):  
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car where make=?', (make_id,))
    results = cur.fetchall()
    print(results)
    return render_template("makes.html", title="makes", results=results)



@app.route('/admin')
def admin():
    return render_template('adminpasswall.html')

if __name__ == "__main__":
    app.run(debug=True)