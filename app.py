import os
import datetime
from flask import *
from library.db import *
app = Flask(__name__)
now = datetime.datetime.now()
@app.route('/')
def hello():
    return render_template('table.html')
q=1
@app.route('/insStud')
def insStud():
    return render_template('studReg.html')
@app.route('/insDoc')
def insDoc():
    return render_template('insDoc.html')
@app.route('/viewPat')
def viewPat():
    a,b,c,d,e,i,g,h=pat()
    f=len(b)
    return render_template('viewPat.html',sr=a,enroll=b,name=c,gen=e,dob=d,des=i,doc=g,cet=h,count=f)
@app.route('/viewStud')
def viewStud():
    b,c,d,e=stud()
    f=len(b)
    return render_template('viewStud.html',enroll=b,name=c,gen=d,dob=e,count=f)
@app.route('/viewDocDep')
def viewDocDep():
    a,b,c=DocDep()
    f=len(b)
    return render_template('viewDocDep.html', sr=a, doc=b, dep=c,count=f)





@app.route('/show', methods=['POST'])
def show():
	global q
	q = request.form['user'];
	print q
	a,b,c,d,e=fet(str(q))
	print a,b,c,d,e
	return render_template('print.html',name=a,age=b,gen=c,dob=d,dept=e)
@app.route('/home/give')
def give():
	a,b,c,d,e=fet(str(q))
	print a,b,c,d,e
	return render_template('print.html',name=a,age=b,gen=c,dob=d,dept=e,today=str(now))
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/prt')
def prt():
	return render_template('print.html')
@app.route('/save', methods=['POST'])
def save():
    name = request.form['name'];
    print name
    age = request.form['age'];
    print age
    gen = request.form['gen'];
    print gen
    dob = request.form['dob'];
    print dob
    dept = request.form['dept'];
    print dept
    res=ins(str(name),str(age),str(gen),str(dob),str(dept))
    print res
    return hello()
if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
