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

print("=========Orders=========")
# prints all the records of  the Order table
result = session.query(create_model.Order).all()
for row in result:
    print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
print("===========================")

print("=========SQL Query for Customer=========")
print(session.query(create_model.Customer))
print("===========================")

print("=========count()=========")
print(session.query(create_model.Customer).count())  # get the total number of records in the customers table
print(session.query(create_model.Item).count())  # get the total number of records in the items table
print(session.query(create_model.Order).count())  # get the total number of records in the orders table
print("===========================")

print("=========first()=========")
result = session.query(create_model.Customer).first()
print("Name: ", result.first_name, " ", result.last_name, " Address:", result.address, " Email:", result.email)

result = session.query(create_model.Item).first()
print("Name: ", result.name, " Cost Price:", result.cost_price, " Selling Price:", result.selling_price, " Quantity:",
      result.quantity)

result = session.query(create_model.Order).first()
print("ID: ", result.id, " Date Placed:", result.date_placed, " Customer Id:", result.customer_id)
print("===========================")

print("=========get()=========")
result = session.query(create_model.Customer).get(1)
print("Name: ", result.first_name, " ", result.last_name, " Address:", result.address, " Email:", result.email)
result = session.query(create_model.Item).get(1)
print("Name: ", result.name, " Cost Price:", result.cost_price, " Selling Price:", result.selling_price, " Quantity:",
      result.quantity)
result = session.query(create_model.Order).get(100)
if result is not None:
    print("ID: ", result.id, " Date Placed:", result.date_placed, " Customer Id:", result.customer_id)
else:
    print(result)
print("===========================")

print("=========filter()=========")
result = session.query(create_model.Customer).filter(create_model.Customer.first_name == 'John').all()
print("\n~~All customers with name starting with John:~~")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

result = session.query(create_model.Customer).filter(create_model.Customer.id <= 5,
                                                     create_model.Customer.town.like("Nor%")).all()
print("\n~~All customers with id less than or equal to 5 and living in Norfolk town:~~")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

print("\n~~find all customers who either live in Peterbrugh or Norfolk~~")
result = session.query(create_model.Customer).filter(
    or_(create_model.Customer.town == 'Peterbrugh', create_model.Customer.town == 'Norfolk')).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

print("\n~~find all customers whose first name is John and live in Norfolk~~")
result = session.query(create_model.Customer).filter(
    and_(create_model.Customer.first_name == 'John', create_model.Customer.town == 'Norfolk')).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

print("\n~~find all johns who don't live in Peterbrugh~~")
result = session.query(create_model.Customer).filter(
    and_(create_model.Customer.first_name == 'John', not_(create_model.Customer.town == 'Peterbrugh', ))).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)
print("===========================")
print("\n")
