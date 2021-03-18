let venues = []
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
        for (var i = 0 ; i < venues.length; i++) {
            console.log('in new loop')
            console.log(venues[i]['venue'])
            if (venues[i]['venue'] == Venue[i].innerHTML) {
                VCName.innerHTML = Venue[i].innerHTML
                VCDescription.innerHTML = venues[i]['desc']
            }
        }
        VenueCard.style.display = "grid";
        VenueCardSB.style.display = "block";
        console.log("clicked");
    })
}