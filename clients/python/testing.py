from gosnu import Connection

with Connection('127.0.0.1') as conn:
    conn.connect()
    consumey = conn.Consumer()
    print(consumey.consume())
    print(consumey.consume())
