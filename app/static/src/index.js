
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
})
