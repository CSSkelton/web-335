/**
 * Title: skelton-exercise-4.js
 * Description: WEB 335 Week 4 Exercise. Practice with MongoDB Shell queries
 * Author: Cody Skelton
 * Date: 02.04.2024
 * Code sourced from assignment requirements and derived from WEB 335 course repository examples
 */

//load script after navigating to directory where file exists and connecting to db
load("users.js")

//display entire collection
db.users.find()

//find user with email jbach@me.com
db.users.findOne({"email": "jbach@me.com"})

//find user with last name Mozart
db.users.findOne({"lastName": "Mozart"})

//find user with first name Richard
db.users.findOne({"firstName": "Richard"})

//find user with employeeId 1010
db.users.findOne({"employeeId": "1010"})