#correct code
# create Dynamic query
import sqlite3

def connect(db_name):
    '''
    create connect with database
    :return: cursor object
    '''
    conn = sqlite3.connect(db_name)
    return (conn.cursor())

def create_insert(cursor):
    '''
    create and insert data into table
    '''
    #cursor.execute("CREATE TABLE student (id INTEGER, name text, location text,grade text)")
    cursor.execute("INSERT into student (id, name, location, grade) VALUES (1,'Anand','Chennai','A')")
    cursor.execute("INSERT into student (id, name, location, grade) VALUES (2,'Anand','HYD','A')")
    cursor.execute("INSERT into student (id, name, location, grade) VALUES (3,'mayank','Kol','A')")
    cursor.execute("INSERT into student (id, name, location, grade) VALUES (4,'Oohanad','HYD','A')")
def orcl_build_query(table_name,id,value):
    '''
    build query
    :param table_name: table_name
    :param id: column name
    :param value: value
    :return: builded query  
    '''
    built_query = f"SELECT * FROM  {table_name} WHERE {id} = '{value}' "
    return built_query

def run_query(qry,cursor):
    '''
    execute query
    :return: resultant data
    '''
    cursor.execute(qry)
    result=cursor.fetchall()
    return result

#start -> get parameters to build query --> generate query --> connetc to db -> run query -> return results -> end
