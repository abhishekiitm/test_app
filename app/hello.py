from flask import Flask
from mysql.connector import connect, Error

app = Flask(__name__)

@app.route('/')
def hello_world():
	print ('Hello')
	try:
		with connect(
			host = 'localhost', 
			user = 'root',
			password = 'my-secret-pw',
			port = 3000,
			auth_plugin='mysql_native_password'
		) as connection:
			print ('Here')
			with connection.cursor() as cursor:
				cursor.execute('use cats;')
				cursor.execute('select * from cats;')
				cats = []
				result = cursor.fetchall()
				for elem in result:
					print (elem)
					cats.append(elem)
			
			# print (connection)
	except Error as e:
		print (e)
		return str(e)



	return '''Hello, World! Let's get started with CI CD\n The cats in our database are - ''' + str(cats)