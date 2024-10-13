from flask import Flask,render_template, request, redirect, url_for
import sqlite3
import os


app = Flask(__name__)
UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


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
    cur.execute('select car.make, car.model, car.engine, car.stockhp, car.stocktorque, make.whatmake, engine.engine_name, car.image, car.drive, car.image_, car.vidlink from car join make on car.make = make.make_id join engine on car.engine = engine.engine_id WHERE car_id=?', (car_id,))
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
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM make')
    makes = cur.fetchall()
    print(makes)
    cur = conn.cursor()
    cur.execute('SELECT * FROM drive')
    drive = cur.fetchall()
    print(drive)
    cur = conn.cursor()
    cur.execute('SELECT * FROM engine')
    engine = cur.fetchall()
    print(engine)

    return render_template('add.html', makes=makes, drive=drive, engine=engine)

@app.route('/process', methods=['POST'])
def process():


    Make = request.form['Make']
    Model = request.form['Model']
    Engine = request.form['Engine']
    Stock_HP = request.form['Stock HP']
    Stock_Torque = request.form['Stock Torque']
    Image = request.form['Image']
    Imageii = request.form['Imageii']
    video = request.form['Video']
    Drive = request.form['Drive']
    
    # Handle file upload
    if 'car_image' not in request.files:
        return "No file part"
    file = request.files['car_image']
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the file to the upload folder
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(f"Image saved at {file_path}")

    # Handle file upload2
    if 'car_image2' not in request.files:
        return "No file part"
    file = request.files['car_image2']
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the file to the upload folder
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(f"Image saved at {file_path}")

    # Save form data and file path to the database
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO car (make, model, engine, stockhp, stocktorque, image, image_, vidlink, drive) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                (Make, Model, Engine, Stock_HP, Stock_Torque, Image, Imageii, video, Drive))
    conn.commit()
    conn.close()

    return render_template("makes.html", title="makes")

@app.route('/engine')
def engine():
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('select * from engine')
    results = cur.fetchall()
    print(results)
    return render_template("engine.html", title="engine", results=results)


if __name__ == "__main__":
    app.run(debug=True)