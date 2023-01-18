// enter as default for Go button
// it has sometimes problem!
goButton = document.querySelector(".reportButton button");

document.querySelector("#reportText").addEventListener("keyup", (e) => {
  e.preventDefault();
  if (e.key === "Enter") {
    goButton.click();
  }
});
