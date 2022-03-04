"""TODO 3)	Assume a system includes a function named db_query to query a table in db.
 The following function is a mock function that prints the SQL statement that will run in the database.
 def db_query(table_name, **kwargs):
   where_clause = ' and '.join([
       f'{x} in ({",".join([t for t in y])})' for x, y in kwargs.items()])
   return f'SELECT * from {table_name} where {where_clause}'
 """