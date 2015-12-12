import MySQLdb
import itertools

def fet(A):
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='test')
	cursor = db.cursor()
	cursor.execute("SELECT `hosp`.`name`, `hosp`.`age`, `hosp`.`gen`, `hosp`.`dob`, `hosp`.`dept` FROM `test`.`hosp` where PID='"+A+"'")
	lis = cursor.fetchall()
	d = list(itertools.chain(*lis))
	db.close()
	return d[0], d[1], d[2], d[3], d[4] 
def ins(a,b,c,d,e):
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='test')
	cursor = db.cursor()
	temp="INSERT INTO `test`.`hosp`(`name`,`age`,`gen`,`dob`,`dept`) VALUES ('"+a+"', '"+b+"', '"+c+"', '"+d+"', '"+e+"')"
	cursor.execute(temp)
	db.commit()
	db.close()
	return "inserted"
def stud():
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[];b=[];c=[];d=[];e=[];
	cursor.execute("select * from stud")
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
		b.append(i[1])
		c.append(i[2])
		d.append(i[3])
	db.close()
	return (a,b,c,d)
def pat():
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[];b=[];c=[];d=[];e=[];f=[];g=[];h=[];
	cursor.execute("select * from nri_medicalwing.pat")
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
		b.append(i[1])
		c.append(i[2])
		d.append(i[3])
		e.append(i[4])	
		f.append(i[5])
		g.append(i[6])
		h.append(i[7])	
	db.close()
	return (a,b,c,d,e,f,g,h)
def DocDep():
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[];b=[];c=[];
	cursor.execute("select `doc`.`iddoc`,`doc`.`name`,`dep`.`name` from `nri_medicalwing`.`doc`LEFT JOIN `nri_medicalwing`.`dep` ON `nri_medicalwing`.`dep`.`iddep`=`nri_medicalwing`.`doc`.`depid`")
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
		b.append(i[1])
		c.append(i[2])
	db.close()
	return (a,b,c)