from database import session
from models import *

if __name__ == "__main__":

    u = User(email="maria@email.com", password="123456")
    session.add(u)
    session.commit()
