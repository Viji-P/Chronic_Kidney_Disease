from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle

app=Flask(__name__)
model=pickle.load(open('CKD.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/submit')
def predict():
    return render_template('predict.html') 

@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('/content/index1.html')

@app.route('/home',methods=['POST','GET'])
def my_home():
    return render_template('/content/indexnew.html') 

@app.route('/predict',methods=['POST'])
def predicted():
    input_features=[float(x) for x in request.form.values()]
    features_value=[np.array(input_features)]
    features_names=['red_blood_cells','pus_cell','blood_glucose_random','blood_urea','pedal_edema','anemia','diabetesmellitus','coronary_artery_disease']
    df=pd.DataFrame(features_value,columns=features_names)
    output=model.predict(df)
    print(output)
    if format(output) == 1:
        return render_template('result.html', prediction_text='Patient condition: {}'.format(output))
    else:
        return render_template('result1.html', prediction_text='Patient condition: {}'.format(output))

#def result():
#  return render_template('result.html',prediction_text=output)

app.run()