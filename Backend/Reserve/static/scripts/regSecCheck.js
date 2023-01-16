let loginCheck = 0;
let finalCheckPass = 0;
let finalCheckCheckbox = 0;

const Signup = document.querySelector(".loginButtonSignup > button");
const loginCheckboxReg = document.querySelector(".loginCheckboxReg");
const passViewLog = document.querySelectorAll(".loginEye")[0];
const passViewReg = document.querySelectorAll(".loginEye")[1];
let passwordInputReg = document.querySelector("#id_password1");
let passwordInputReg2 = document.querySelector("#id_password2");
let form = document.querySelectorAll("form")[0];

// enable or disable the button
function buttonChecker() {
  if (finalCheckPass * finalCheckCheckbox * loginCheck === 1) {
    Signup.disabled = false;
  } else {
    Signup.disabled = true;
  }
}

// show/hide password
// passViewLog.addEventListener("mousedown", () => {
//   passwordInputReg.type = "text";
// });

// passViewLog.addEventListener("mouseup", () => {
//   passwordInputReg.type = "password";
// });

// passViewLog.addEventListener("touchstart", () => {
//   passwordInputReg.type = "text";
// });

// passViewLog.addEventListener("touchcancel", () => {
//   passwordInputReg.type = "password";
// });

// passViewReg.addEventListener("mousedown", () => {
//   passwordInputReg2.type = "text";
// });

// passViewReg.addEventListener("mouseup", () => {
//   passwordInputReg2.type = "password";
// });

// passViewReg.addEventListener("touchstart", () => {
//   passwordInputReg2.type = "text";
// });

// passViewReg.addEventListener("touchcancel", () => {
//   passwordInputReg2.type = "password";
// });

// check the password
form.id_password1.addEventListener("keyup", (e) => {
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
      loginCheck = 1;
    } else {
      passwordInputReg.style["border-color"] = "red";
      passwordInputReg.style["background-color"] = "#fdb7b7";
      loginCheck = 0;
    }
  }
});

passwordInputReg2.addEventListener("keyup", (e) => {
  if (passwordInputReg2.value == passwordInputReg.value) {
    passwordInputReg2.style["border-color"] = "green";
    passwordInputReg2.style["background-color"] = "#c0fdb7";
    finalCheckPass = 1;
    buttonChecker();
  } else if (passwordInputReg.value == passwordInputReg2.value) {
    passwordInputReg2.style["border-color"] = "green";
    passwordInputReg2.style["background-color"] = "#c0fdb7";
    finalCheckPass = 1;
    buttonChecker();
  } else {
    passwordInputReg2.style["border-color"] = "red";
    passwordInputReg2.style["background-color"] = "#fdb7b7";
    finalCheckPass = 0;
    buttonChecker();
  }
});

passwordInputReg.addEventListener("keyup", (e) => {
  if (passwordInputReg2.value == passwordInputReg.value) {
    passwordInputReg2.style["border-color"] = "green";
    passwordInputReg2.style["background-color"] = "#c0fdb7";
    finalCheckPass = 1;
    buttonChecker();
  } else if (passwordInputReg.value == passwordInputReg2.value) {
    passwordInputReg2.style["border-color"] = "green";
    passwordInputReg2.style["background-color"] = "#c0fdb7";
    finalCheckPass = 1;
    buttonChecker();
  } else {
    passwordInputReg2.style["border-color"] = "red";
    passwordInputReg2.style["background-color"] = "#fdb7b7";
    finalCheckPass = 0;
    buttonChecker();
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
