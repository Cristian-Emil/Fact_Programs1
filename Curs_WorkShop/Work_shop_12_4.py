import sqlite3

connection = sqlite3.connect("baza_date.db")

cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE continente(
        continent_id INTEGER,
        continant_name VARCHAR,
        continent_code TEXT
    )
''')

connection.commit()
connection.close()
#
# cursor.execute ( '''
#     INSERT INTO continets (continent_id, continent_name, continent_code) VALUES (
#
# (1, 'Africa', 'AF'),
# (2, 'Antarctica', 'AN'),
# (3, 'Asia', 'AS'),
# (4, 'Europe', 'EU'),
# (5, 'North America', 'NA'),
# (6, 'Oceania', 'OC'),
# (7, 'South America', 'SA');
#
#    )
# ''')
#
# connection.commit()
# connection.close()
#
# outcome = cursor.execute('''
# SELECT * from continents;
# ''')
#
# print(outcome.fetchall())
