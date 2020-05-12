import pandas as pd
import psycopg2
from sqlalchemy import *
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Date,DateTime, Float, MetaData, 
from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy import text

connectionString ='sqlite:///C:\\Users\\NT_WIN10\\Desktop\\Coball\\Website\\testDatabase.db'
databaseConnectionEngine = create_engine(connectionString,echo=True)

databaseSession = sessionmaker(bind=databaseConnectionEngine)
databaseSession = scoped_session(databaseSession)

db = databaseSession()
metaData = MetaData()

class connectionInstantiator():
    def __init__(self,connectionString: str):
        self.databaseConnectionEngine = create_engine(connectionString,echo=True)
        self.databaseSession = sessionmaker(bind=self.databaseConnectionEngine)
        self.scopedSession = self.databaseSession()

class contactFormModel:
    def __init__(self,firstName,lastName,email,organization,phoneNumber,message):
        self.contactId = None
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.organization = organization
        self.phoneNumber = phoneNumber
        self.message = message
    

# class ContactFormTable(declarative_base()):
#     __tablename__ = 'contactform'
#     contactId = Column(Integer, primary_key=True)
#     firstName  = Column(String(45))
#     lastName = Column(String(45))
#     email = Column(String(45))
#     organization = Column(String(45))
#     phoneNumber = Column(String(45))
#     message = Column(String(1000))
    
#     def __init__(self,currentSession: connectionInstantiator):
#         self.databaseConnection = connectionInstantiator
        

#     def __rep__(self):
#         return f"<ContactFormTable(self.databaseConnection='{self.databaseConnection}')>"
    
#     def insert(self,newContact: 'ContactFormModel') -> bool:
#         sql: str = "insert into contactForm (firstName,lastName,email,organization,phoneNumber,message) values (:firstName,:lastName,:email,:organization,:phoneNumber,:message)"

#         try:
#             self.databaseConnection.scopedSession.execute(sql,firstName = newContact.firstName, lastName = newContact.lastName, email = newContact.email, organization = newContact.organization,phoneNumber = newContact.phoneNumber, message = newContact.message)
#             return True
#         except Exception as e:
#             print(e)
#             return False

class ContactForm():
    def __init__(self):
        self.table = Table('contactform',metaData,
            Column('contactId',Integer, primary_key=True),
            Column('firstName',String(45)),
            Column('lastName',String(45)),
            Column('email',String(45)),
            Column('organization',String(45)),
            Column('phoneNumber',String(45)),
            Column('message',String(1000))
        )
        # self.table.create(databaseConnectionEngine)
        self.insertObject: 'ContactFormModel' = None
    
    def insert(self,newContact: 'ContactFormModel') -> bool:
        # sql: str = "insert into contactForm (firstName,lastName,email,organization,phoneNumber,message) values (:firstName,:lastName,:email,:organization,:phoneNumber,:message)"

        try:
            # self.databaseConnection.scopedSession.execute(sql,firstName = newContact.firstName, lastName = newContact.lastName, email = newContact.email, organization = newContact.organization,phoneNumber = newContact.phoneNumber, message = newContact.message)
            self.insertObject = self.table.insert.values(firstName = newContact.firstName, lastName = newContact.lastName, email = newContact.email, organization = newContact.organization,phoneNumber = newContact.phoneNumber, message = newContact.message)
            db.execute(self.insertObject)
            self.insertObject = None
            return True
        except Exception as e:
            print(e)
            return False

metaData.create_all(databaseConnectionEngine)