from psycopg2.extras import RealDictCursor
from psycopg2 import connect
from decouple import config


CONEXAO = connect(
    host=config("HOST"),
    database=config("DATABASE"),
    user=config("USER"),
    password=config("PASSWORD"),
    cursor_factory=RealDictCursor
)