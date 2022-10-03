import psycopg2
from psycopg2.extensions import connection
from tabulate import tabulate

def connect_ratings():
    """
    Connect to the ratings database and return the connection object
    Function exits the program if there is an error
    :return: connection object
    """
    # read the password file
    try:
        pwd_file = open('.pwd')  # password file should be in a secure location
    except OSError:
        print("Error: No authorization")
        exit()

    # what can go wrong?
    try:
        conn = psycopg2.connect(
            dbname = "ehar_books",
            user = "cslabtes",
            password = pwd_file.readline(),
            host = "ada.hpc.stlawu.edu"
        )
    except psycopg2.Error:
        print("Error: cannot connect to database")
        exit()
    finally:
        pwd_file.close()

    return conn

def menu():
    """
    Present the user with a menu and return selection
    only if valid.
    :return: option selected
    """
    while True:
        print("1) Look up book by title")
        print("2) Look up book by author")
        print("Q) Quit")
        opt = input("> ")
        if opt in  ['1', '2', 'q', 'Q']:
            break

    return opt

def lookup_title(conn:connection) -> None:
    print ("lookup book by title")

def lookup_title1(conn:connection) -> None:
    def f():
        print("lookup title")
    return f

# if this file is being run as a program and *not* imported
# as a module
if __name__ == "__main__":

    conn = connect_ratings()

    opt_map = { '1' : lookup_title}
    opt_map1 = { '1' : lookup_title1(conn)}

    while True:
        opt = menu()
        if opt.lower() == 'q': break
        #opt_map[opt](conn)
        opt_map1[opt]()

    # next class
