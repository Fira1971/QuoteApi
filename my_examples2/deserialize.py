from student import Learner
from schema import LearnerSchema
from pprint import pprint


json_data = """
[
   {
       "uid": 1,
       "name": "Alex",
       "final_test": true
   },
   {
       "uid": 2,
       "name": "Ivan",
       "final_test": false
   },
   {
       "uid": 4,
       "name": "Tom",
       "final_test": true
   }
]
"""

schema = LearnerSchema(many=True)
result = schema.loads(json_data)
pprint(result)
