from flask import Flask,render_template 


app = Flask(__name__)




#this is the route to the home page/landing page
@app.route('/')
def landingpage():
    return render_template('landing_page.html')

if __name__ == "__main__":
    app.run(debug=True)