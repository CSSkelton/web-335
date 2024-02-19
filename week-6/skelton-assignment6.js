/**
 * Title: skelton-assignment-6.js
 * Description: WEB 335 Week 6 Assignment. Practice with MongoDB Shell queries
 * Author: Cody Skelton
 * Date: 02.18.2024
 * Code sourced from assignment requirements and derived from WEB 335 course examples and Query Guide
 */

//display entire house collection
db.houses.find()

//display entire students collection
db.students.find()

//add document to student's collection and verify creation
db.students.insertOne({
    "firstName": "Cody",
    "lastName": "Skelton",
    "studentId": "s1019",
    "houseId": "h1009"
})

db.students.find()

//delete created document and verify deletion
db.students.deleteOne( { "studentId" : "s1019" } )

db.students.find()

//show a list of students by house
db.students.aggregate( [
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house_docs"
      }
    },
  {
    $sort: {
      "houseId": 1
    }
  }
])

// display list of students for house Gryffindor
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house_docs"
      }
    },
    {
      $match: {
        "houseId": "h1007"
      }
    },
    {
      $addFields: {
        house_docs: {
          $arrayElemAt: ["$house_docs", 0]
        }
      }
    }
  ])

// display list of students for house with mascot "Eagle"
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house_docs"
      }
    },
    {
      $match: {
        "house_docs.mascot": "Eagle"
      }
    },
    {
      $addFields: {
        house_docs: {
          $arrayElemAt: ["$house_docs", 0]
        }
      }
    }
])