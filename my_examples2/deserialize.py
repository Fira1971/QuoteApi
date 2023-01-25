from student import Learner
from schema import LearnerSchema


json_data = """
[
   {
       "id": 1,
       "name": "Alex",
       "final_test": "exept"
   },
   {
       "id": 2,
       "name": "Ivan",
       "final_test": "fine"
   },
   {
       "id": 4,
       "name": "Tom",
       "final_test": "fine"
   }
]
"""

schema = LearnerSchema(many=True)
result = schema.loads(json_data)
print(result)

learners = [
    Learner("1", "Alex"),
    Learner("1", "Ivan"),
    Learner("1", "Tom")
]
schemas = LearnerSchema(many=True)
res = schemas.dump(learners)
print(res)
