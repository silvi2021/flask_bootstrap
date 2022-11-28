from app.extensions import db

class Message(db.Model):
    __tablename__ = 'messages'    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String(300))

    def __repr__(self):
        return f'<Message {self.title}>'