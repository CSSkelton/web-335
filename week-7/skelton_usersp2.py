#
# Title: skelton_usersp2.py
# Author: Cody Skelton
# Date: 02.25.2024
# Purpose: DB connection w/ python 
# Requirements from WEB 335 Exercise 7.3
# Code sources from Python Guide, courtesy of Professor Krasso
#

#import MongoClient
from pymongo import MongoClient
import datetime

# build connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.ifz0to0.mongodb.net/web335DBretryWrites=true&w=majority")

# configure variable to access web335DB
db = client['web335DB']

# create a user document
new_user = { "firstName": "Connor", "lastName": "Price", "employeeId": "1014", "email": "connorprice@me.com" }

db.users.insert_one(new_user)

# display the new user document
print(db.users.find_one({"employeeId": "1014"}))
print("\n")

# update new user's email address
query = { "email": "connorprice@me.com" }
new_value = { "$set": {"email": "cprice@me.com" }}

db.users.update_one(query, new_value)

# display updated document
print(db.users.find_one({"employeeId": "1014"}))
print("\n")

# delete the document
query = { "employeeId": "1014" }
db.users.delete_one(query)

# prove document was deleted
for user in db.users.find():
    print(user)
print("\n")