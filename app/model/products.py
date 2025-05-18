from app import db

class Products (db.Model):
    __tablename__ = "products"
    __table_args__ = {'sqlite_autoincrement':True}
    id = db.Column(db.Integer, primery_key=True)
    nome = db.Column (db.String(255))
    price = db.Coloumn (db.Float)