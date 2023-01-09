let loginTime = document.querySelector(".loginTime");

setInterval(() => {
  let now = new Date();
  let min = now.getMinutes();
  if (min < 10) {
    min = "0" + min;
  }

  let sec = now.getSeconds();
  if (sec < 10) {
    sec = "0" + sec;
  }

  let time = now.getHours() + ":" + min + ":" + sec;
  loginTime.innerHTML = time;
}, 1000);
