// Search part
searchButton = document.querySelectorAll(".postSearch > div > button")[0];
results = document.querySelectorAll(".result");

searchButton.addEventListener("click", (e) => {
  searchValue = document
    .querySelector(".postSearch > input")
    .value.toLowerCase();
  for (const iterator of results) {
    if (searchValue == iterator.innerHTML.toLowerCase()) {
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
