from student import Learner
from schema import LearnerSchema

learner = Learner(1, "Alex", "alex5@mail.ru")
learner_schema = LearnerSchema()
result = learner_schema.dump(learner)
print(result)
