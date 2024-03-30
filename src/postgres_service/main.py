from sqlalchemy import create_engine
from sqlalchemy import text

print("ab")
engine = create_engine('postgresql://postgres:postgres@localhost:5431/dbname')

try:
    connection = engine.connect()
    print("Connection is established")
except exc.SQLAlchemyError as e:
    print(f"Connection error: {e}")
finally:
    engine.dispose()
