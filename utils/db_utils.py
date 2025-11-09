"""Utilidades para optimizar las conexiones a la base de datos"""
import mysql.connector
from mysql.connector import pooling
import config

def create_connection_pool(pool_name="mypool", pool_size=5):
    """
    Crea un pool de conexiones a la base de datos para mejorar el rendimiento
    """
    dbconfig = {
        "pool_name": pool_name,
        "pool_size": pool_size,
        "host": config.DB_CONFIG['host'],
        "user": config.DB_CONFIG['user'],
        "password": config.DB_CONFIG['password'],
        "database": config.DB_CONFIG['database'],
        "port": config.DB_CONFIG['port']
    }
    
    return mysql.connector.pooling.MySQLConnectionPool(**dbconfig)

# Pool global
connection_pool = None

def get_connection():
    """
    Obtiene una conexión del pool
    """
    global connection_pool
    if connection_pool is None:
        connection_pool = create_connection_pool()
    return connection_pool.get_connection()