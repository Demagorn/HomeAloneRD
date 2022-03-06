"""TODO 3)	Assume a system includes a function named db_query to query a table in db.
 The following function is a mock function that prints the SQL statement that will run in the database.
 def db_query(table_name, **kwargs):
   where_clause = ' and '.join([
       f'{x} in ({",".join([t for t in y])})' for x, y in kwargs.items()])
   return f'SELECT * from {table_name} where {where_clause}'
 """

from math import ceil


def db_query(table_name, **kwargs):
    where_clause = ' and '.join([
        f'{x} in ({",".join([t for t in y])})' for x, y in kwargs.items()])
    return f'SELECT * from {table_name} where {where_clause}'


def my_db_query(table_name, **kwargs):
    limit = 2
    param = kwargs["departments"]
    chunks = ceil(len(param)/limit)
    starting_index = 0
    for chunk in range(chunks):
        # in case there is a need to split the request it will be splited to the most possible equal parts
        if chunk == chunks-1:
            indexes = [starting_index, None]
        else:
            indexes = [starting_index, starting_index+ceil(len(param)/chunks)]
        chunks_department = param[indexes[0]:indexes[1]]
        yield db_query(table_name, departments=chunks_department, category=kwargs["category"])
        starting_index = indexes[1]


b = my_db_query('MyTable', departments=["R&D", "Sales", "Marketing"], category=['expense', 'income'])
print(b.__next__())
print(b.__next__())


# mydbclass = MyDbClass()
# a = db_query('MyTable', departments=, category=['expense', 'income'])
# c= db_query('MyTable', departments=["R&D", "Sales"], category=['expense', 'income'])
# d = db_query('MyTable', departments=["Marketing"], category=['expense', 'income'])

# # print(a)
# print(c)
# print(d)

# import os
#
# CHUNK_SIZE=os.getenv("CHUNK_SIZE")

# class MyDbClass:
#     @staticmethod
#     def my_db_query(table_name,**kwargs):
#         def wrapper(func):
#             pass
#
#     @staticmethod