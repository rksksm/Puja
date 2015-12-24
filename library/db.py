import MySQLdb
import itertools

def fet(A):
<<<<<<< HEAD
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	cursor.execute("SELECT `stud`.`enroll`,`stud`.`name`,`stud`.`gen`,`stud`.`dob` FROM `nri_medicalwing`.`stud` where `stud`.`enroll`='"+A+"';")
	lis = cursor.fetchall()
	d = list(itertools.chain(*lis))
	db.close()
	return d[0], d[1], d[2], d[3]
=======
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='test')
	cursor = db.cursor()
	cursor.execute("SELECT `hosp`.`name`, `hosp`.`age`, `hosp`.`gen`, `hosp`.`dob`, `hosp`.`dept` FROM `test`.`hosp` where PID='"+A+"'")
	lis = cursor.fetchall()
	d = list(itertools.chain(*lis))
	db.close()
	return d[0], d[1], d[2], d[3], d[4] 
>>>>>>> 12101d318b1769587018ea9949d576a7a6dfaca8
def ins(a,b):
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	temp="INSERT INTO `nri_medicalwing`.`doc`(`name`,`depid`) VALUES ('"+a+"', '"+b+"')"
	cursor.execute(temp)
	db.commit()
	db.close()
	return "inserted"
<<<<<<< HEAD
def insPrt(a,b,c):
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	temp="INSERT INTO `nri_medicalwing`.`pat` (`enroll`,`desiese`,`iddep`) VALUES ('"+a+"', '"+b+"', "+c+")"
	cursor.execute(temp)
	db.commit()
	db.close()
	return "inserted"
=======
>>>>>>> 12101d318b1769587018ea9949d576a7a6dfaca8
def ins_stud(a,b,c,d):
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	temp="INSERT INTO `nri_medicalwing`.`stud`(`name`,`enroll`,`gen`,`dob`) VALUES ('"+a+"', '"+b+"','"+c+"', '"+d+"')"
	cursor.execute(temp)
	db.commit() 
	db.close()
	return "inserted"
def stud():
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[];b=[];c=[];d=[];e=[];
	cursor.execute("select * from stud order by enroll")
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
		b.append(i[1])
		c.append(i[2])
		d.append(i[3])
	db.close()
	return (a,b,c,d)
def dep():
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[];b=[];
	cursor.execute("select * from dep order by iddep")
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
		b.append(i[1])
	db.close()
	return (a,b)
def pat():
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[];b=[];c=[];d=[];e=[];f=[];g=[];h=[];
<<<<<<< HEAD
	cursor.execute("select patid,stud.enroll,stud.name,stud.gen,stud.dob,desiese,created FROM nri_medicalwing.pat LEFT JOIN nri_medicalwing.stud ON nri_medicalwing.pat.enroll=nri_medicalwing.stud.enroll;")
=======
	cursor.execute("select * from nri_medicalwing.pat")
>>>>>>> 12101d318b1769587018ea9949d576a7a6dfaca8
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
		b.append(i[1])
		c.append(i[2])
		d.append(i[3])
		e.append(i[4])	
		f.append(i[5])
		g.append(i[6])
<<<<<<< HEAD
	db.close()
	return (a,b,c,d,e,f,g)
=======
		h.append(i[7])	
	db.close()
	return (a,b,c,d,e,f,g,h)
>>>>>>> 12101d318b1769587018ea9949d576a7a6dfaca8
def DocDep():
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[];b=[];c=[];
	cursor.execute("select `doc`.`iddoc`,`doc`.`name`,`dep`.`name` from `nri_medicalwing`.`doc`LEFT JOIN `nri_medicalwing`.`dep` ON `nri_medicalwing`.`dep`.`iddep`=`nri_medicalwing`.`doc`.`depid` order by `nri_medicalwing`.`doc`.`depid`")
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
		b.append(i[1])
		c.append(i[2])
	db.close()
<<<<<<< HEAD
	return (a,b,c)
def det(a1):
	db = MySQLdb.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='nri_medicalwing')
	cursor = db.cursor()
	a=[]
	cursor.execute("select dep.name from nri_medicalwing.dep where dep.iddep="+a1)
	lis = cursor.fetchall()
	for i in lis:
		a.append(i[0])
	db.close()
	return "".join(a)
=======
	return (a,b,c)
>>>>>>> 12101d318b1769587018ea9949d576a7a6dfaca8
