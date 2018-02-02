import psycopg2
from trader.config import cfg

POSTGRES_CONNECTION_TIMEOUT = 600


def create_new_connection(host=cfg['DATABASE']['HOST'],
                          pg_user=cfg['DATABASE']['USER'],
                          pg_pass=cfg['DATABASE']['PASSWORD']):

    conn = psycopg2.connect(
        dbname            = cfg['DATABASE']['DB_NAME'],
        user              = pg_user,
        password          = pg_pass,
        host              = host,
        port              = cfg['DATABASE']['PORT'],
        connect_timeout   = POSTGRES_CONNECTION_TIMEOUT
    )

    conn.set_session(autocommit = True)
    return conn
