
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             port=3306,
                             password='123456',
                             db='bank',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `bank`.`subject` (`subject_no`, `subject_name`, `ks`, `term_no`) " \
	# 		  " VALUES (%s, %s, %s, %s);"
    #     cursor.execute(sql, ('5', 'GUI', '100', '5'))
	#
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT * FROM `subject` as a WHERE a.subject_no=%s"
		cursor.execute(sql, ('1',))
		result = cursor.fetchone()
		print(result)
finally:
    connection.close()
