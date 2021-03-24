let venues = []
const venue_card = document.getElementById("venueCardContainer");
const vc_name = document.getElementById("venueCardName");
const vc_hours = document.getElementById("venueCardHours");
const vc_img = document.getElementById("venueCardImg");
const vc_link = document.getElementById("venueCardLinka");
const vc_description = document.getElementById("venueCardDescription");
let Venue = document.getElementsByClassName("venueName");

const VenueCardSB = document.getElementById("venueCardShadowbox");


document.getElementById("CloseWindowXVenue").addEventListener("click", function(){
    venue_card.style.display = "none";
    VenueCardSB.style.display = "none";
})
document.getElementById("venueCardShadowbox").addEventListener("click", function(){
    venue_card.style.display = "none";
    VenueCardSB.style.display = "none";
})

// generates the venue card using the venue object that i pass in the html.
for (var i = 0 ; i < Venue.length; i++) {
    Venue[i].addEventListener('click', function(){
        for (var j = 0 ; j < venues.length; j++) {
            console.log("iterated")
            if (venues[j]['venue'] == this.innerHTML) {
                console.log(Venue[j])
                vc_name.innerHTML = this.innerHTML
                vc_description.innerHTML = venues[j]['desc']
                vc_link.href = venues[j]['venueURL']
                venue_card.style.display = "grid";
                VenueCardSB.style.display = "block";
                vc_img.innerHTML = "<img src='" + venues[j]['venueIconAddress'] + "' />"
            }
        }
        
        console.log("clicked " + Venue[i]);
    })
}