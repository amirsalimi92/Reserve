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

  // profile
  document.querySelector(".content").classList.toggle("night");
  document.querySelector(".profileName").classList.toggle("profileLeftNight");
  document.querySelector(".profileFamily").classList.toggle("profileLeftNight");
  document
    .querySelector(".profilePhoto")
    .classList.toggle("profileTopLeftNight");
  document.querySelectorAll("input").forEach((e) => {
    e.classList.toggle("profileInputNight");
  });
  document.querySelectorAll("select").forEach((e) => {
    e.classList.toggle("profileSelectNight");
  });
  document
    .querySelector(".profileButton > button")
    .classList.toggle("profileButtonNight");

  // set the theme
  if (localStorage.getItem("themeModeReserve") == "night") {
    localStorage.setItem("themeModeReserve", "day");
  } else if (localStorage.getItem("themeModeReserve") == "day") {
    localStorage.setItem("themeModeReserve", "night");
  }
}
