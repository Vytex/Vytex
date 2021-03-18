const ResetMenu = document.getElementById("ResetMenu");

document.getElementById("CloseWindowX2").addEventListener("click", function () {
    ResetMenu.style.display = "none";
    console.log("ClickedClose")
})
document.getElementById("ResetOffscreen").addEventListener("click", function () {
    ResetMenu.style.display = "none";
    console.log("ClickedOff")
})

document.getElementById("forgot").addEventListener("click", function () {
    ResetMenu.style.display = "flex";
    console.log("ClickedTest")
})