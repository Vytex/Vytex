
const HamburgerMenu = document.getElementById("HamburgerMenu");
const HMContainer = document.getElementById("HMContainer");

document.getElementById("CloseWindowX").addEventListener("click", function(){
    HMContainer.classList.remove("HMAfter")
    HamburgerMenu.classList.remove("HamburgerAfter")
})

document.getElementById("HMOffscreen").addEventListener("click", function(){
    HMContainer.classList.remove("HMAfter")
    HamburgerMenu.classList.remove("HamburgerAfter")
})

document.getElementById("hamburgerB").addEventListener("click", function(){
    HamburgerMenu.classList.add("HamburgerAfter")
    HMContainer.classList.add("HMAfter")
})
