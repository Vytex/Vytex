// function createVenue() {
//     console.log('mofo dene got clicked and created')
//     const data = {
//         "venue": "venueName"
//     };
//     // farms.school, farms.shchool/shoe-api
//     return fetch("/home-api", 
//         {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(data)
//         }
//     )
//     .then(
//         (response) => {
//             return response.json();
//         }
//     ).then(
//         (json) => {
//             console.log("YOU GOT MAIL MOTHER FUCKER: \n", json);
//         }
//     )
// }

// function getVenues() {
//     console.log("getting venues")
//     // farms.school, farms.shchool/shoe-api
//     return fetch("/admin-api")
//         .then(
//             (response) => {
//                 return response.json();
//             }
//         ).then(
//             (json) => {
//                 console.log("YOU GOT MAIL MOTHER FUCKER: \n", json);
//             }
//         )
// }

// function deleteVenue() {
//     console.log('mofo dene got clicked and deleted')
//     const data = {
//         "venueID": document.getElementById("venueID").innerHTML
//     };
//     // farms.school, farms.shchool/shoe-api
//     return fetch("/home-api", 
//         {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(data)
//         }
//     )
//     .then(
//         (response) => {
//             return response.json();
//         }
//     ).then(
//         (json) => {
//             console.log("YOU GOT MAIL MOTHER FUCKER: \n", json);
//         }
//     )
// }

// document.getElementById('deleteVenue').addEventListener('submit', function(e) {
//     e.preventDefault();
//     deleteVenue();
// })

