from app import db
from app.models import User,Post

u = User(username='susan', email='susan@example.com')
u.set_password('mypassword')

u.check_password('anotherpassword')

u.check_password('mypassword')