const VenueCard = document.getElementById("venueCardContainer");
const VCName = document.getElementById("venueCardName");
const VCHours = document.getElementById("venueCardHours");
const VCIMG = document.getElementById("venueCardImg");
const VCLink = document.getElementById("venueCardLink");
const VCDescription = document.getElementById("venueCardDescription");
let Venue = document.getElementsByClassName("venueName");

const VenueCardSB = document.getElementById("venueCardShadowbox");


document.getElementById("CloseWindowXVenue").addEventListener("click", function(){
    VenueCard.style.display = "none";
    VenueCardSB.style.display = "none";
})
document.getElementById("venueCardShadowbox").addEventListener("click", function(){
    VenueCard.style.display = "none";
    VenueCardSB.style.display = "none";
})

for (var i = 0 ; i < Venue.length; i++) {
    Venue[i].addEventListener('click', function(){
        VenueCard.style.display = "grid";
        VenueCardSB.style.display = "block";
        console.log("clicked");
    })
}