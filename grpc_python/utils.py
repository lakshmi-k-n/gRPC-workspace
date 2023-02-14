import jwt
import bcrypt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/workspace') 

def verify_access_token(access_token):
    if not access_token:
        return {'message' : 'Token is missing !!'}
    try:
        # decoding the payload to fetch the stored details
        data = jwt.decode(access_token, "secret", algorithms=["HS256"])
        Session = sessionmaker(bind=engine)
        session = Session()
        current_user = session.get(User, data['userId'])
        session.close()
    except:
        return False
    return  data

def create_access_token(data):
    access_token = jwt.encode(data, "secret", algorithm="HS256")
    return  access_token

def hash_password(password):
    byte_input = password.encode()
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(byte_input, salt)
    return hashed_pass.decode()

def is_password_match(password, hashed):
    hashed = hashed.encode()
    password = password.encode()
    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False



# user_alias = aliased(User, name='user2')
# q = sess.query(User, User.id, user_alias)

# # this expression:
# q.column_descriptions

# # would return:
# [
#     {
#         'name':'User',
#         'type':User,
#         'aliased':False,
#         'expr':User,
#         'entity': User
#     },
#     {
#         'name':'id',
#         'type':Integer(),
#         'aliased':False,
#         'expr':User.id,
#         'entity': User
#     },
#     {
#         'name':'user2',
#         'type':User,
#         'aliased':True,
#         'expr':user_alias,
#         'entity': user_alias
#     }
# ]