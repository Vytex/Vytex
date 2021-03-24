let venues = []
const venue_card = document.getElementById("venue-card-container");
const vc_name = document.getElementById("venue-card-name");
const vc_hours = document.getElementById("venue-card-hours");
const vc_img = document.getElementById("venue-card-img");
const vc_link = document.getElementById("venue-card-link-a");
const vc_description = document.getElementById("venue-card-description");
let Venue = document.getElementsByClassName("venue-name");

const VenueCardSB = document.getElementById("venue-card-shadow-box");


document.getElementById("close-window-x-venue").addEventListener("click", function(){
    venue_card.style.display = "none";
    VenueCardSB.style.display = "none";
})
document.getElementById("venue-card-shadow-box").addEventListener("click", function(){
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
                vc_link.href = venues[j]['venue-url']
                venue_card.style.display = "grid";
                VenueCardSB.style.display = "block";
                vc_img.innerHTML = "<img src='" + venues[j]['venue-icon-address'] + "' />"
            }
        }
        
        console.log("clicked " + Venue[i]);
    })
}