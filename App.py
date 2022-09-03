from flask import Flask, render_template,request
from flask_mysqldb import MySQL

import model


app =  Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "JAni_98124"
app.config['MYSQL_DB'] = "diseaseapp"

mysql = MySQL(app)
# @app.route('/')
# def home():
#     return render_template('projectfrontend2.html')

@app.route('/')
def get_symptoms():
    return render_template("projectfrontend2.html")

@app.route('/rgs')
def rgs():
    return render_template("register.html")

@app.route('/',methods=['POST'])
def display():
    if(request.method == "POST"):
        name = request.form['ownername']
        pet = request.form['petname']
        sym1 = request.form['sym1']
        sym2 = request.form['sym2']
        sym3 = request.form['sym3']
        sym4 = request.form['sym4']
        sym5 = request.form['sym5']
        # print(name)
        result = model.traning_model(sym1,sym2,sym3,sym4,sym5)
        # return render_template("Display.html",pet=pet,sym1=sym1,sym2=sym2,sym3=sym3,sym4=sym4,sym5=sym5,result=result)

        curr = mysql.connection.cursor()
        curr.execute("INSERT INTO disease_app(name,petname,sym1,sym2,sym3,sym4,sym5,disease) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(name,pet,sym1,sym2,sym3,sym4,sym5,result))
        mysql.connection.commit();

        result_values = curr.execute("SELECT * FROM disease_app")
        if result_values > 0:
            user_details = curr.fetchall()

        return render_template("show_disease.html",result=result)
        # return "success";
        curr.close();


@app.route('/users')
def users():
    curr = mysql.connection.cursor()
    result_values = curr.execute("SELECT * FROM disease_app ")
    if result_values >0:
        user_details = curr.fetchall()
        return render_template("users.html",user_details=user_details)

if __name__ == '__main__':
    app.run(debug=True)