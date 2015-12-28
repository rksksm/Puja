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
@app.route('/regDoc', methods=['POST'])
def regDoc():
    name = request.form['name'];
    print name
    gen = request.form['gen'];
    print gen
    res=ins(str(name),str(gen))
    print res
    return hello()
#>>>>>>> HEAD
@app.route('/conferm', methods=['POST'])
def conferm():
    name = request.form['enroll'];
    print name
    gen = request.form['dis'];
    print gen
    dep = request.form['dep'];
    print dep
    res=insPrt(str(name),str(gen),str(dep))
    r=det(str(dep))
    print res
    return r
#>>>>>>>
#>>>>>>> 12101d318b1769587018ea9949d576a7a6dfaca8
@app.route('/insStud')
def insStud():
    return render_template('studReg.html')
@app.route('/insDoc')
def insDoc():
    a,b=dep()
    f=len(b)
    print a
    print b
    return render_template('insDoc.html',sr=a,enroll=b,count=f)
@app.route('/viewPat')
def viewPat():
    a,b,c,d,e,i,g=pat()
    f=len(b)
    return render_template('viewPat.html',sr=a,enroll=b,name=c,gen=e,dob=d,des=i,crt=g,count=f)
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
#>>>>>>> HEAD
	a,b,c,d=fet(str(q))
	print a,b,c,d
	return jsonify({"name":b,"enroll":a,"gen":c,"dob":d})
@app.route('/give')
def give():
	a,b,c,d,e=fet(str(q))
	print a,b,c,d,e
	return render_template('print.html',name=a,age=b,gen=c,dob=d)
#>>>>>>>
	a,b,c,d,e=fet(str(q))
	print a,b,c,d,e
	return render_template('print.html',name=a,age=b,gen=c,dob=d,dept=e)
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
    enroll = request.form['enroll'];
    print enroll
    gen = request.form['gen'];
    print gen
    dob = request.form['dob'];
    print dob
    res=ins_stud(str(name),str(enroll),str(gen),str(dob))
    print res
    return hello()
if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
