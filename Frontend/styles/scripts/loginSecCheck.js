let finalCheckPass = 0;
let finalCheckCheckbox = 0;

const Signup = document.querySelector(".loginButtonSignup > button");
const loginCheckboxReg = document.querySelector(".loginCheckboxReg");
const passViewLog = document.querySelectorAll(".loginEye")[0];
const passViewReg = document.querySelectorAll(".loginEye")[1];
let passwordInput = document.querySelector(".loginPasswordInput");
let passwordInputReg = document.querySelector(".loginPasswordInputReg");
let form = document.querySelectorAll("form")[1];

// enable or disable the button
function buttonChecker() {
  if (finalCheckPass * finalCheckCheckbox === 1) {
    Signup.disabled = false;
  } else {
    Signup.disabled = true;
  }
}

// show/hide password
passViewLog.addEventListener("mousedown", () => {
  passwordInput.type = "text";
});

passViewLog.addEventListener("mouseup", () => {
  passwordInput.type = "password";
});

passViewLog.addEventListener("touchstart", () => {
  passwordInput.type = "text";
});

passViewLog.addEventListener("touchcancel", () => {
  passwordInput.type = "password";
});

passViewReg.addEventListener("mousedown", () => {
  passwordInputReg.type = "text";
});

passViewReg.addEventListener("mouseup", () => {
  passwordInputReg.type = "password";
});

passViewReg.addEventListener("touchstart", () => {
  passwordInputReg.type = "text";
});

passViewReg.addEventListener("touchcancel", () => {
  passwordInputReg.type = "password";
});

// check the password
form.passwordReg.addEventListener("keyup", (e) => {
  if (e.target.value) {
    let ep = 0;
    ep += /[a-z]/.test(e.target.value) ? 1 : 0;
    ep += /[A-Z]/.test(e.target.value) ? 1 : 0;
    ep += /[0-9]/.test(e.target.value) ? 1 : 0;
    ep += /[\W]/.test(e.target.value) ? 1 : 0;
    ep += e.target.value.length >= 8 ? 1 : 0;

    if (ep === 5) {
      passwordInputReg.style["border-color"] = "green";
      passwordInputReg.style["background-color"] = "#c0fdb7";
      finalCheckPass = 1;
      buttonChecker();
    } else {
      passwordInputReg.style["border-color"] = "red";
      passwordInputReg.style["background-color"] = "#fdb7b7";
      finalCheckPass = 0;
      buttonChecker();
    }
  }
});

// checkbox
loginCheckboxReg.addEventListener("click", (e) => {
  if (document.querySelector(".loginCheckboxReg:checked") !== null) {
    finalCheckCheckbox = 1;
    buttonChecker();
  }
  if (document.querySelector(".loginCheckboxReg:checked") == null) {
    finalCheckCheckbox = 0;
    buttonChecker();
  }
});
