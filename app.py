# Adding dependencies
from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Defining Flask App
app = Flask(__name__)
model = pickle.load(open('model/model_rs.pkl', 'rb'))
@app.route('/', methods=['GET'])

# Defining home function for rendering index page
def Home():
    return render_template('index.html')

@app.route("/contact")
def Contact():
    return render_template('contact.html')
@app.route("/create-account")
def newAccount():
    return render_template("create-account.html")


standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        CreditScore = int(request.form['credit_score'])
        Age = int(request.form['age'])
        Tenure = int(request.form['tenure'])
        Balance = float(request.form['balance'])
        NumOfProducts = int(request.form['products_number'])
        HasCrCard = int(request.form['credit_card'])
        IsActiveMember = int(request.form['active_member'])
        EstimatedSalary = float(request.form['estimated_salary'])
        Geography_Germany = request.form['country_Germany']
        if(Geography_Germany == 'Germany'):
            Geography_Germany = 1
            Geography_Spain= 0
            Geography_France = 0
                
        elif(Geography_Germany == 'Spain'):
            Geography_Germany = 0
            Geography_Spain= 1
            Geography_France = 0
        
        else:
            Geography_Germany = 0
            Geography_Spain= 0
            Geography_France = 1
        Gender_Male = request.form['gender_Male']
        if(Gender_Male == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1
        prediction = model.predict([[CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography_Germany,Geography_Spain,Gender_Male]])

        if prediction==0:
            return render_template('index.html',prediction_text="The Customer will not leave the bank")
        else:
             return render_template('index.html',prediction_text="The Customer will leave the bank")

if __name__=="__main__":
    app.run(debug=True)


    