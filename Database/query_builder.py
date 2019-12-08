from sqlalchemy import *
from sqlalchemy.orm import Session

from Database import create_model

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)

print("=========Customers=========")
# prints all the records of  the Customers table
result = session.query(create_model.Customer).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)
print("===========================")

print("=========Item=========")
# prints all the records of  the Item table
result = session.query(create_model.Item).all()
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)
print("===========================")
