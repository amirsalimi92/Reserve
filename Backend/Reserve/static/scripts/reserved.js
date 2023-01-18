// Search part
searchButton = document.querySelectorAll(".postSearch > div > button")[0];
results = document.querySelectorAll(".result");

searchButton.addEventListener("click", (e) => {
  searchValue = document
    .querySelector(".postSearch > input")
    .value.toLowerCase();
  searchValueString = String(searchValue);
  for (const iterator of results) {
    if (String(iterator.innerHTML.toLowerCase()).includes(searchValueString)) {
      iterator.parentElement.classList = "finalResult";
    }
  }
  document.querySelectorAll(".postShowResult").forEach((n) => {
    n.remove();
  });
});

// refresh part
refreshButton = document.querySelectorAll(".postSearch > div > button")[1];

refreshButton.addEventListener("click", (e) => {
  setTimeout(function () {
    window.location.reload();
  }, 1);
});

// enter as default for Go button
// it has sometimes problem!
goButton = document.querySelectorAll(".postSearch button")[0];

document.querySelector("#postSearchInput").addEventListener("keyup", (e) => {
  e.preventDefault();
  if (e.key === "Enter") {
    goButton.click();
  }
});
