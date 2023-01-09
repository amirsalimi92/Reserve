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

function nightTheme() {
  // navbar
  document.querySelector(".navbar").classList.toggle("nightNavbar");
  document.querySelector(".navMenu").classList.toggle("navMenuNight");
  document.querySelectorAll(".dropdown").forEach((e) => {
    e.classList.toggle("nightDropdown");
  });

  // report
  document.querySelector(".reportBase").classList.toggle("reportBaseNight");
  document
    .querySelector(".reportButton > button")
    .classList.toggle("reportButtonNight");
  document
    .querySelector(".reportSender > select")
    .classList.toggle("reportSenderNight");
  document
    .querySelector(".reportSender > textarea")
    .classList.toggle("reportSenderNight");

  // set the theme
  if (localStorage.getItem("themeModeReserve") == "night") {
    localStorage.setItem("themeModeReserve", "day");
  } else if (localStorage.getItem("themeModeReserve") == "day") {
    localStorage.setItem("themeModeReserve", "night");
  }
}
