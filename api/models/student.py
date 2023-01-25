from api import db


class LearnerModel(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    final_test = db.Column(db.Boolen, nullable=False)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "uid": self.id,
            "name": self.name
        }
