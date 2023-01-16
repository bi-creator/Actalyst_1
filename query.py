import psycopg2
def executeQuery(query,datatoinsert=[]):
    conn = psycopg2.connect(
        database="actalyst_demo_1", user='postgres', password='manjith', host='localhost', port= '5432'
        )
    cursor = conn.cursor()
    if(datatoinsert):
        print(query,datatoinsert)
        cursor.execute(query,datatoinsert)
        conn.commit()
        return "data inserted"
    else:
        cursor.execute(query)
        data=[]
        column_names = [desc[0] for desc in cursor.description]
        for row in cursor:
            a={}
            for col in  column_names:
                a[col]=row[column_names.index(col)]
            data.append(a)
        conn.close()
        return(data)