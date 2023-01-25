from student import Learner
from schema import LearnerSchema

learner = Learner(1, "Alex", "fine")
learner_schema = LearnerSchema()
result = learner_schema.dump(learner)
print(result)
