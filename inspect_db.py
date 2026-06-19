import psycopg2
import traceback

try:
    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='Calebe@7676')
    cur = conn.cursor()
    cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_schema='public' AND table_name='produtos'")
    cols = cur.fetchall()
    print('columns:', cols)
    try:
        cur.execute("SELECT * FROM produtos LIMIT 1")
        rows = cur.fetchall()
        print('sample_row_count:', len(rows))
        if cur.description:
            print('column_names_from_select:', [d[0] for d in cur.description])
    except Exception as e:
        print('select error:', e)
    cur.close()
    conn.close()
except Exception:
    traceback.print_exc()
