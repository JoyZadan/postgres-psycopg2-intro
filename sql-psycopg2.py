"""
Imports psycopg2 libraries
"""
import psycopg2


# connect to "chinook" database
# can also include addl connection values ie
# host, username, password
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
# a cursor object is another way of saying a 'set' or 'list'
# similar to 'array' in JavaScript
# anything that we query from the db will become part of this cursor object,
# and to read that data, we should iterate over the cursor using a for-loop
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# After our cursor variable is defined, but before our results are fetched,
# we need to perform our queries using the .execute() method
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# Since we need to specify a particular record, any combination of single or
# double quotes just won't work
# We need to use a Python string placeholder, %s,
# and then define the desired string within a list
# We can have multiple placeholders, depending on how detailed the
# query needs to be and each placeholder would be added to this list.
# Technically, since we know there should only be one result,
# we could use the .fetchone() method.
# This would print each column individually,
# instead of part of a tuple of column results.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# Use a Python placeholder, %s, and list, [],
# to specify that we need only the primary key of 51
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" # 51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen"
# from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 challenge - select only "Aerosmith" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Aerosmith"])

# Query 8 challenge - select all tracks where the composer is "Test"
# from the "Track" table. "Test" is not not listed in the database
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch or retrieve the results (single)
# results = cursor.fetchone()

# close the connection
# once our results have been fetched, we need to end the connection to the
# database so the connection isn't always persistent
connection.close()

# print ressults
# our data sits within a cursor object, similar to an array, so in order to
# retrieve each record individually, we need to iterate
# over the results using a for-loop
for result in results:
    print(result)
