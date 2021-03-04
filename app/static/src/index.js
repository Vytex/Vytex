// document.getElementById('searchinputid').addEventListener('submit', function(e) {
//     e.preventDefault();
// })

// function createVenue() {
//     console.log('mofo dene got clicked and created')
//     const data = {
//         "venue": "testVenue"
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

function getVenues() {
    // farms.school, farms.shchool/shoe-api
    console.log('mofo dene got clicked and searched')
    const data = {
        "venue": document.getElementById('si').value
    };
    return fetch("/home-api", 
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }
)
    .then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            window.location.href = "lineList";
            // location.assign("localhost:5000/lineList")
            console.log("got som mofo data bra \n", json);
        }
    )
}

const HamburgerMenu = document.getElementById("HamburgerMenu");

document.getElementById("CloseWindowX").addEventListener("click", function(){
    HamburgerMenu.style.display = "none";
    console.log("Clicked")
})
document.getElementById("HMOffscreen").addEventListener("click", function(){
    HamburgerMenu.style.display = "none";
    console.log("Clicked")
})

document.getElementById("hamburgerB").addEventListener("click", function(){
    HamburgerMenu.style.display = "flex";
    // console.log("Clicked")
    // used as a temp way to add some data to venues
    // createVenue()
})

// document.getElementById("searchInputB").addEventListener("click", createVenue());
