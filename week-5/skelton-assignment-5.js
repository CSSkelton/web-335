/**
 * Title: skelton-assignment-5.js
 * Description: WEB 335 Week 5 Assignment. Practice with MongoDB Shell queries
 * Author: Cody Skelton
 * Date: 02.11.2024
 * Code sourced from assignment requirements and derived from WEB 335 course repository examples
 */

// add new user to collection
// did this differently since ran this file as a script at first
// both script and shell commands worked for creating document
swift = {
    "firstName": "Taylor",
    "lastName": "Swift",
    "employeeId": "1013",
    "email": "tswift@me.com",
    "dateCreated": new Date()
}

db.users.insertOne(swift) 
/**
 * Mongosh command:
 * db.users.insertOne({"firstName": "Taylor", 
 *  "lastName": "Swift",
 *  "employeeId": "1013",
 *  "email": "tswift@me.com",
 *  "dateCreated": new Date()})
 */

// update email address
db.users.updateOne(
    { firstName : "Wolfgang" },
    { $set : { "email" : "mozart@me.com" }}
)

// check to make sure update was made
db.users.findOne({"lastName": "Mozart"})

// display entire collection
// only following fields: firstName, lastName, email
db.users.find( {}, { employeeId: 0, dateCreated : 0, _id : 0 } )