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

  // post
  document.querySelector(".postBase").classList.toggle("postBaseNight");
  document
    .querySelector(".postSearch label")
    .classList.toggle("postSearchLabelNight");
  document
    .querySelector(".postSearch input")
    .classList.toggle("postSearchInputNight");
  document
    .querySelector(".postAdd label")
    .classList.toggle("postSearchLabelNight");
  document
    .querySelector("#postAddInputName")
    .classList.toggle("postSearchInputNight");
  document
    .querySelector("#postAddInputWhere")
    .classList.toggle("postSearchInputNight");
  document.querySelectorAll("button").forEach((e) => {
    e.classList.toggle("postButtonNight");
  });

  document.querySelectorAll(".postShow tr:nth-child(odd)").forEach((e) => {
    e.classList.toggle("postTableNight");
  });

  document.querySelectorAll(".postShowHead td").forEach((e) => {
    e.classList.toggle("postTable");
  });

  // set the theme
  if (localStorage.getItem("themeModeReserve") == "night") {
    localStorage.setItem("themeModeReserve", "day");
  } else if (localStorage.getItem("themeModeReserve") == "day") {
    localStorage.setItem("themeModeReserve", "night");
  }
}
