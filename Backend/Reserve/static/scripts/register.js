username = document.querySelector("#id_username");
pass1 = document.querySelector("#id_password1");
pass2 = document.querySelector("#id_password2");
loginFormReg = document.querySelectorAll(".loginFormReg label");
spans = document.querySelectorAll(".loginFormReg > span");
labels = document.querySelectorAll(".loginFormReg > label");
inputs = document.querySelectorAll(".loginFormReg > input");

username.classList.add("loginUsenameInputReg");
pass1.classList.add("loginPasswordInputReg");
pass2.classList.add("loginPasswordInputReg2");

spans.forEach((e) => {
  e.remove();
});

labels.forEach((e) => {
  e.classList.add("loginUsenameLabelReg");
});

loginFormReg.forEach((e) => {
  e.style["color"] = "azure";
});

brs = document.querySelectorAll(".loginFormReg > br");
brs.forEach((e) => {
  e.remove();
});

inputs[0].setAttribute("placeholder", "Please insert a username");
inputs[1].setAttribute("placeholder", "Please insert a password");
inputs[2].setAttribute("placeholder", "Please repeat your password");
