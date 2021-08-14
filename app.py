from flask import Flask , render_template,request
import joblib
app=Flask(__name__)
model=joblib.load('diabetic_79.sav')
#@app.route('/')
#def hello():
   # return render_template('landing.html')

#@app.route('/contact')
#def contact():
 #   return render_template('contact.html')
@app.route('/diabetic')
def diabetic():
    return render_template('diabetic.html')


@app.route('/data',methods=['POST'])
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    

    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)
    
    
    result=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if result[0] == 1:
       output=('Person is diabetic')
    else:
       output=('not diabetic')

    

    return render_template('result.html', predict=output)



if __name__=='__main__':
    app.run(debug=True)#jst refresh to run the code
