#
# Title: skelton_usersp1.py
# Author: Cody Skelton
# Date: 02.18.2024
# Purpose: DB connection w/ python 
# Requirements from WEB 335 Exercise 6.3
# Code sources from Python Guide, courtesy of Professor Krasso
#

#import MongoClient
from pymongo import MongoClient
import datetime

# build connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.ifz0to0.mongodb.net/web335DBretryWrites=true&w=majority")

# configure variable to access web335DB
db = client['web335DB']

#display all documents in user collection
for user in db.users.find():
    print(user)
print("\n")

#display employeeId = 1011 document
print(db.users.find_one({"employeeId": "1011"}))
print("\n")

#display lastName = Mozart document
print(db.users.find_one({"lastName": "Mozart"}))
