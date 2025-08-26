from flask import Flask,render_template,request,redirect,url_for

'''
It created an instance of the FLask class,
which will be your WSGI (Web Server Gateway Interface) Application'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}"
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
        
    exp={'score':score,"result":res}
    return render_template('result1.html',result=exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)
    
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method =='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        english=float(request.form['english'])
        tamil=float(request.form['tamil'])
        social=float(request.form['social'])
        
        total_score = (science+maths+english+tamil+social)/5
    else:
        return render_template('results_sub.html')
    return redirect(url_for('success',score=total_score))
        

if __name__ == "__main__":
    app.run(debug=True)