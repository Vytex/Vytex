
const InfoMenu = document.getElementById("InfoMenu");

document.getElementById("CloseWindowX1").addEventListener("click", function(){
    InfoMenu.style.display = "none";
    console.log("ClickedClose")
})
document.getElementById("IMOffscreen").addEventListener("click", function(){
    InfoMenu.style.display = "none";
    console.log("ClickedOff")
})

document.getElementById("info").addEventListener("click", function(){
    InfoMenu.style.display = "flex";
    console.log("ClickedTest")
})

