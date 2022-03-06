"""TODO 3)	Assume a system includes a function named db_query to query a table in db.
 The following function is a mock function that prints the SQL statement that will run in the database.
 def db_query(table_name, **kwargs):
   where_clause = ' and '.join([
       f'{x} in ({",".join([t for t in y])})' for x, y in kwargs.items()])
   return f'SELECT * from {table_name} where {where_clause}'
 """
import os
# class MyDbClass:
#     @staticmethod
#     def my_db_query(table_name,**kwargs):
#         def wrapper(func):
#             pass
#
#     @staticmethod
def db_query(table_name, **kwargs):
    where_clause = ' and '.join([
        f'{x} in ({",".join([t for t in y])})' for x, y in kwargs.items()])
    return f'SELECT * from {table_name} where {where_clause}'


def my_db_query(table_name,**kwargs):
    limit = 2
    for i,v in kwargs.items():
        print(v)
        # if v > limit:
        #     print(limit)


# mydbclass = MyDbClass()
a = db_query('MyTable', departments=["R&D", "Sales", "Marketing"], category=['expense', 'income'])
c= db_query('MyTable', departments=["R&D", "Sales"], category=['expense', 'income'])
d = db_query('MyTable', departments=["Marketing"], category=['expense', 'income'])

print(a)
print(c)
print(d)

b = my_db_query('MyTable', departments=["R&D", "Sales", "Marketing"], category=['expense', 'income'])
print(b)