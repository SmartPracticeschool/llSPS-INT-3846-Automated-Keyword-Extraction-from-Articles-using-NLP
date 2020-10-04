import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
app = Flask(__name__)
model = keras.models.load_model('mymodel.h5')
tks = load('Demo.save')
@app.route('/')
def home():
    
    return render_template('index.html')
   
@app.route('/y_predict',methods=['POST'])
def y_predict():
    
    
    
    demo=request.form.values()
    if demo == model.keywords.keys():
        print("yes")
    else:
        print("no")
        
   
    
    

if __name__ == "__main__":
    app.run(debug=True)
