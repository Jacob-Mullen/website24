from flask import Flask,render_template, request
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

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/process', methods=['POST'])
def process():
    Make = request.form['Make']
    Model = request.form['Model']
    Engine = request.form['Engine']
    Stock_HP = request.form['Stock HP']
    Stock_Torque = request.form['Stock Torque']
    Image = request.form['Image']
    Drive = request.form['Drive']
    
    # Print for debugging purposes
    print("Make:", Make, "Model:", Model, "Engine:", Engine, "Stock_HP:", Stock_HP, "Stock_Torque:", Stock_Torque, "Image:", Image, "Drive:", Drive)
    
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    
    # Corrected INSERT statement with placeholders and tuple of values
    cur.execute("INSERT INTO car (make, model, engine, stockhp, stocktorque, image, drive) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                (Make, Model, Engine, Stock_HP, Stock_Torque, Image, Drive))
    
    conn.commit()  # Commit the transaction
    
    conn.close()   # Close the connection
    
    return render_template("makes.html", title="makes")


if __name__ == "__main__":
    app.run(debug=True)