import psycopg2

def init_rdbms():
    commands = (
        """
        CREATE TABLE categories (
	        id numeric NOT NULL,
	        category varchar(255) NOT NULL,
	        parent numeric,
	        PRIMARY KEY (id)
        )
        """,
        """ALTER TABLE categories ADD FOREIGN KEY (parent) REFERENCES categories (id)""",
        """CREATE SEQUENCE Category_Seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE"""
    )
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",database="i2",user="i2fwd",password="i2fwd")
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        print("DB Init Success")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    init_rdbms()
