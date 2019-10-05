import psycopg2
import json

try:
    connection: psycopg2.extensions.connection = psycopg2.connect(user="data_db_admin",
                                                                  password="P@@sw0rd",
                                                                  host="91.217.194.184",
                                                                  port="5432",
                                                                  database="edu_power")

    print(f'type(connection) = {type(connection)}')
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    # cursor.execute("SELECT * FROM pg_stat_activity;")
    # record = cursor.fetchone()
    # print("You are connected to - ", record, "\n")

    cursor.execute("SELECT * FROM pg_stat_activity;")
    results = []
    for row in cursor.fetchall():
        print(f'row = {row}')
        # results.append(dict(zip(columns, row)))

    print(f'json.dumps(results) = {json.dumps(results)}')

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
