from api import app, db, request
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema


# url: /users/<int:user_id>
@app.get('/users')
def get_users():
    users = UserModel.query.all()
    # authors_dict = [author.to_dict() for author in authors]
    return users_schema.dump(users), 200


@app.get('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = UserModel.query.get(user_id)
    if user is None:
        return {"message": f"User with id={user_id} not found"}, 404
    return user_schema.dump(user), 200


@app.post('/users')
def create_user():
    user_data = request.json
    user = UserModel(**user_data)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 200


@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user = db.session.query(UserModel).get(user_id)
    if user is None:
        return {"Error": f"User id={user_id} not found"}, 404
    db.session.delete(user)
    db.session.commit()
    return {"message": f"User with id={user_id} has deleted"}, 200
