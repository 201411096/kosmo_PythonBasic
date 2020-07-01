import cx_Oracle as oci

def insert_data(name, addr):
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = """
        INSERT INTO STORE(NAME, ADDR)
        VALUES(:name, :addr)
    """
    for i in range(len(name)):
        cursor.execute(sql, (name[i], addr[i]))
    cursor.close()
    conn.commit()
    conn.close()