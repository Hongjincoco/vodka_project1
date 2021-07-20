import mysql.connector
from mysql.connector import Error
import sys
sys.path.insert(0, 'tourists/config')
from config import db_config

def get_mysql_connection():

    try :
        connection = mysql.connector.connect( **db_config ) 

        if connection.is_connected() :
            print('connection OK!')

        return connection

           

    except Error as e :
        print('Error while connecting MySQL',e)
        return None
