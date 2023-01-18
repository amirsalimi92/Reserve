// enter as default for Go button
// it has sometimes problem!
reserveButton = document.querySelectorAll(".ffSelectorButton button")[0];

document
  .querySelector(".ffSelectorOffice select")
  .addEventListener("keyup", (e) => {
    e.preventDefault();
    if (e.key === "Enter") {
      reserveButton.click();
    }
  });
