import psycopg2
from read_config import read_config

def connect_to_psql(filename):
    """
    Takes in kev-value file containing HOST, PORT, DB, USER, and PASSWORD needed to connect to your postgresql database.
    Returns connection.
    """
    HOST, PORT, DB, USER, PASSWORD = read_config('psql.config')
    connect_str =  "host=" + HOST + " port=" + str(PORT) + " dbname=" + DB + " user=" + USER + " password=" + PASSWORD 
    conn = psycopg2.connect(connect_str)
    return conn


def create_table(conn, table_name, schema_string):
    """
    Creates a table w/ table_name and schema schema_string in database.
    """
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE " + table_name + schema_string + ";")
    cursor.close()
    return None






def main():

    # conn = connect_to_psql('psql.config')
    #  create_table(conn, 'test_table', '(name text, age int)')
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO test_table values ('vincent', 54);")
    # cursor.execute("COMMIT")
    # cursor.execute("""SELECT * from test_table;""")
    # rows = cursor.fetchall()
    # print("-----------------")
    # print(rows)
    # print("-----------------")
    # cursor.close()
    # conn.close()
    
    ## read price from files
    print(read_open('AB.csv'))
    print(read_open('BC.csv'))
    print(read_open('AD.csv'))
    print(read_open('AC.csv'))
    print(read_open('CD.csv'))


    ## cycles
    cycle1 = [('A','B'), ('B','C'), ('C','A')]
    cycle2 = [('A','B'), ('B','C'), ('C','D'), ('D','A')]
    cycle3 = [('A','C'), ('C','D'), ('D','A')]
    cycles = [cycle1, cycle2, cycle3]

def read_open(filename):
    """
    Takes in filename (of form AB.csv), where 1st letter refers to base currency and 2nd letter refers to the quoted currency.

    For example, if the price listed in AB.csv is 1.3, then that means B is worth 1.3 A.

    Returns a triplet: (base currency, quoted currency, price)
    """
    tmp = filename[:-3]
    base, quoted = tmp[0], tmp[1]

    with open(filename, 'r') as file:
        file.readline()
        price = float(file.readline().split(',')[1].strip())
        return (base, quoted, price)

main()
