from flask import Flask,render_template,request
import pickle
import json
import requests
app= Flask(__name__)

@app.route("/")
def index ():
    return render_template("index.html")
@app.route("/predict",methods=["POST"])
def predict():
    n= request.form["n"]
    p= request.form["p"]
    k= request.form["k"]
    t= request.form["t"]
    h= request.form["h"]
    ph= request.form["ph"]
    r= request.form["r"]
    model= pickle.load(open("Crop.pkl","rb"))
    rusult=model.predict([[n,p,k,t,h,ph,r]])
    if rusult[0]== 1:
        return render_template("rice.html")
    elif rusult[0]== 2:
        return render_template("makka.html")
    elif rusult[0]== 3:
        return render_template("chickpea.html")
    
    elif rusult[0]==4:
         return render_template( "kidneybeans.html")
    elif rusult[0]== 5:
         return render_template( "pigeonpeas.html")
        
    elif rusult[0]== 6:
         return render_template( "mothbeans.html")
         
    elif rusult[0]== 7:
         return render_template( "mungbeans.html")

    elif rusult[0]== 8:
         return render_template( "blackgram.html")
        
    elif rusult[0]== 9:
         return render_template( "lentil.html")
         
    elif rusult[0]== 10:
         return render_template( "pomegranate.html")
         
    elif rusult[0]== 11:
        return render_template("banana.html")
    elif rusult[0]== 12:
         return render_template( "mango.html")
         
    elif rusult[0]== 13:
         return render_template( "grapes.html")
         
    elif rusult[0]== 14:
         return render_template( "watermelon.html")
         
    elif rusult[0]== 15:
         return render_template( "muskmelon.html")
         
    elif rusult[0]== 16:
         return render_template( "apple.html")
         
    elif rusult[0]== 17:
         return render_template( "orange.html")
        
    elif rusult[0]== 18:
         return render_template( "papaya.html")
         
    elif rusult[0]== 19 :
         return render_template( "coconut.html")
         
    elif rusult[0]== 20:
         return render_template( "cotton.html")
         
    elif rusult[0]== 21:
         return render_template( "jute.html")
         

    elif rusult[0]== 22:
         return render_template( "coffee.html") 
         
    
    
    

    
    
    


if __name__=='__main__':
    app.run(debug=True)