from app.extensions import db

class Message(db.Model):
    __tablename__ = 'messages'    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String(300))
    price = db.Column(db.Integer)
    link = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Message {self.title}>'