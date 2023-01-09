themeSelector = document.querySelector(".theme");

//get the saved theme
let themeModeFirst = localStorage.getItem("themeModeReserve");
//set the saved theme
if (themeModeFirst === "night") {
  nightTheme();
} else if (themeModeFirst == null || themeModeFirst === "day") {
  localStorage.setItem("themeModeReserve", "day");
}

// run the function

themeSelector.addEventListener("click", () => {
  nightTheme();
});

// night theme function
function nightTheme() {
  // navbar
  document.querySelector(".navbar").classList.toggle("nightNavbar");
  document.querySelector(".navMenu").classList.toggle("navMenuNight");
  document.querySelectorAll(".dropdown").forEach((e) => {
    e.classList.toggle("nightDropdown");
  });

  // floors contents
}
