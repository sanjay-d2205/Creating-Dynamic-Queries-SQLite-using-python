# for Sqlite only
from new_query import orcl_build_query,rdbms_read,connect,create_insert

if __name__ == "__main__":

    qry = orcl_build_query( 'SQL','request','Sqlite','pass',53444,'XXX' )
    print(qry)
    c=connect()   # connect
    create_insert(c)
    run_qry = rdbms_read(qry,c)   # run query
    print(run_qry)

    qry = orcl_build_query('SQL2', 'request2', 'Sqlite2', 'pass2', 53441, 'XXX2')
    print(qry)
    res = rdbms_read(qry,c)
    print(res)

    qry = orcl_build_query("SQL1", "request1", "Sqlite1", "request_id1", 53445, "XXX1")
    print(qry)
    res = rdbms_read(qry,c)
    print(res)