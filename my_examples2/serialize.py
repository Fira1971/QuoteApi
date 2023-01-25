from student import Learner
from schema import LearnerSchema

learner = Learner(1, "Alex", "fine")
learner_schema = LearnerSchema()
result = learner_schema.dump(learner)
print(result)

learners = [
    Learner("1", "Alex"),
    Learner("2", "Ivan"),
    Learner("3", "Tom")
]
schemas = LearnerSchema(many=True)
res = schemas.dump(learners)
print(res)
