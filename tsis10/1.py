import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='poiu0987uiop'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook1(
        username VARCHAR(20),
        number VARCHAR(12)
    )
    '''
)
config.commit()

current.close()
config.close()
