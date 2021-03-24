
const LineHMenu = document.getElementById("LineHistory");

document.getElementById("CloseWindowX2").addEventListener("click", function(){
    LineHMenu.style.display = "none";
    console.log("ClickedClose")
})
document.getElementById("LHOffscreen").addEventListener("click", function(){
    LineHMenu.style.display = "none";
    console.log("ClickedOff")
})

document.getElementById("lineHist").addEventListener("click", function(){
    LineHMenu.style.display = "flex";
    console.log("ClickedTest")
})