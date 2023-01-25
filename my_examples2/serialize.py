from pprint import pprint
from student import Learner
from schema import LearnerSchema

learner = Learner(1, "Alex", "fine")
learner_schema = LearnerSchema()
result = learner_schema.dump(learner)
pprint(result)

learners = [
    Learner("1", "Alex", True),
    Learner("2", "Ivan", False),
    Learner("3", "Tom", True)
]
schemas = LearnerSchema(many=True)
res = schemas.dump(learners)
pprint(res)
