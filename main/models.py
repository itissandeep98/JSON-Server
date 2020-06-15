from main import db

class Test1(db.Model):
	id = db.Column(db.Integer, primary_key = True)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), nullable = False)
	roll_num = db.Column(db.String(10), unique = True, nullable = False)
	email_id = db.Column(db.String(254), nullable = False)
	password = db.Column(db.String(60), nullable = False)

	def as_dict(self):
		return  {'id': self.id, 'name': self.name, 'roll_num': self.roll_num, 'email_id': self.email_id}

class Ad(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, nullable = False)
	book_name = db.Column(db.String(100), nullable = False)
	author = db.Column(db.String(50), nullable = False)
	transaction_type = db.Column(db.Integer, nullable = False)
	description = db.Column(db.String(254), nullable = True)
	price = db.Column(db.Integer, nullable = False)
	# date

	def as_dict(self):
		return  {'id': self.id, 'user_id': self.user_id, 'book_name': self.book_name, 'author': self.author, 'transaction_type': self.transaction_type, 'description': self.description, 'price': self.price}

class Tag(db.Model):
	name = db.Column(db.String(50), primary_key = True)

class AdTagRelation(db.Model):
	name = db.Column(db.String(50), primary_key = True)
	id = db.Column(db.Integer, primary_key = True)


class Course(db.Model):
	name = db.Column(db.String(50), primary_key = True)

