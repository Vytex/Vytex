
const HamburgerMenu = document.getElementById("hamburger-menu");

document.getElementById("close-window-x").addEventListener("click", function(){
    HamburgerMenu.style.display = "none";
    console.log("Clicked")
})
document.getElementById("hm-offscreen").addEventListener("click", function(){
    HamburgerMenu.style.display = "none";
    console.log("Clicked")
})

document.getElementById("hamburger-b").addEventListener("click", function(){
    HamburgerMenu.style.display = "flex";
})
