import sqlite3
import psycopg2


# Configurações
DB_PATH = "postgres://default:NgpZud4Xq2vw@ep-curly-pond-a4x7fala.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
#DB_PATH = "banco_escola.db"

def get_connection():
    #return sqlite3.connect(DB_PATH)
    return psycopg2.connect(DB_PATH)
