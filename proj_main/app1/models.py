"""
proj_main/app1/models.py
Define los modelos de usuario y los métodos asociados para interactuar con la base de datos.

Uso:
1. Define una clase User que hereda de UserMixin.
2. Implementa los métodos necesarios para la autenticación de usuarios.
3. Utiliza PyMongo para interactuar con la base de datos.

Ejemplo:
from flask_login import UserMixin
from ..extensions import mongo

class User(UserMixin):
    def __init__(self, username, password, _id=None):
        self.username = username
        self.password = password
        self.id = _id
    
    @staticmethod
    def get(username):
        user_data = mongo.db.users.find_one({'username': username})
        if user_data:
            return User(
                username=user_data['username'], 
                password=user_data['password'],
                _id=str(user_data['_id'])
            )
        return None

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user_data:
        return User(
            username=user_data['username'],
            password=user_data['password'],
            _id=str(user_data['_id'])
        )
"""
