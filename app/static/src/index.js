
const HamburgerMenu = document.getElementById("HamburgerMenu");

document.getElementById("CloseWindowX").addEventListener("click", function(){
    HamburgerMenu.style.display = "none";
})
document.getElementById("HMOffscreen").addEventListener("click", function(){
    HamburgerMenu.style.display = "none";
})

document.getElementById("hamburgerB").addEventListener("click", function(){
    HamburgerMenu.style.display = "flex";
})
