 # for Sqlite only 3'c correct code
 # call dynamic query
from RDBMS_pro import orcl_build_query,run_query,connect,create_insert

if __name__ == "__main__":
    cursor = connect('db1.db')
    qry = orcl_build_query('student','name','Anand')
    print(qry)
    create_insert(cursor)
    result = run_query(qry,cursor)   # run query
    if result:
        print(result)
    else:
        print("No record")

    cursor = connect('db1.db')
    qry = orcl_build_query('student','id','4')
    create_insert(cursor)
    result = run_query(qry,cursor)
    if result:
        print(result)
    else:
        print("No record")

    cursor = connect('db1.db')
    qry = orcl_build_query('student','id','5')
    create_insert(cursor)
    result = run_query(qry,cursor)
    if result:
        print(result)
    else:
        print("No record")
