from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Database import create_model

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)

# Populate Customer Data
c1 = create_model.Customer(first_name='Toby',
                           last_name='Miller',
                           username='tmiller',
                           email='tmiller@example.com',
                           address='1662 Kinney Street',
                           town='Wolfden'
                           )

c2 = create_model.Customer(first_name='Scott',
                           last_name='Harvey',
                           username='scottharvey',
                           email='scottharvey@example.com',
                           address='424 Patterson Street',
                           town='Beckinsdale'
                           )

session.add(c1)
session.add(c2)
session.commit()
