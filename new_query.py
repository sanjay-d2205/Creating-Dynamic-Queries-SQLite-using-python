import sqlite3
def connect():
    '''
    creating connect
    :return:
    '''
    conn = sqlite3.connect(':memory:')
    return (conn.cursor())

def create_insert(c):
    '''
    create and insert data into table having name 'table1'
    :return:
    '''
    c.execute(
        "CREATE TABLE table1 (type_c text, column_c text, db_c text,identifier_c text, mtdata_obj_id_c INTEGER, subquery_c text )")
    c.execute(
        "INSERT into table1 (type_c , column_c , db_c,identifier_c,mtdata_obj_id_c,subquery_c) VALUES ('SQL','request','Sqlite','pass','53444','XXX')")

def orcl_build_query(type,column,db,identifier,mtdata_obj_id,subquery):
    '''
    build query
    :return: builded query
    '''
    built_query = f"SELECT * FROM table1 WHERE type_c = '{type}' AND column_c = '{column}' AND db_c = '{db}' AND identifier_c = '{identifier}' AND mtdata_obj_id_c = {mtdata_obj_id} AND subquery_c = '{subquery}'"
    return built_query
def rdbms_read(qry,c):
    '''
    creating connection and execute query
    :return: resultant data
    '''
    c.execute(qry)
    k=c.fetchall()
    return k

#start -> get parameters to build query --> generate query --> connetc to db -> run query -> return results -> end