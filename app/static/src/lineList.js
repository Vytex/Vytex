let venues = []
const VenueCard = document.getElementById("venueCardContainer");
const VCName = document.getElementById("venueCardName");
const VCHours = document.getElementById("venueCardHours");
const VCIMG = document.getElementById("venueCardImg");
const VCLink = document.getElementById("venueCardLinka");
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

// generates the venue card using the venue object that i pass in the html.
for (var i = 0 ; i < Venue.length; i++) {
    Venue[i].addEventListener('click', function(){
        for (var j = 0 ; j < venues.length; j++) {
            console.log("iterated")
            if (venues[j]['venue'] == this.innerHTML) {
                console.log(Venue[j])
                VCName.innerHTML = this.innerHTML
                VCDescription.innerHTML = venues[j]['desc']
                VCLink.href = venues[j]['venueURL']
                VenueCard.style.display = "grid";
                VenueCardSB.style.display = "block";
                VCIMG.innerHTML = "<img src='" + venues[j]['venueIconAddress'] + "' />"
            }
        }
        
        console.log("clicked " + Venue[i]);
    })
}