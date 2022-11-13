from webapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, primary_key = True, nullable = False)
    email = db.Column(db.String(120), unique = True, primary_key = True, nullable = False)
    img_file = db.Column(db.String(20), nullable = False, default = 'default-avatar.png' )
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.img_file}')"