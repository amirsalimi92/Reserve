pass1 = document.querySelector("#id_password1");
pass2 = document.querySelector("#id_password2");
loginFormReg = document.querySelectorAll(".loginFormReg label");
span0 = document.querySelectorAll(".loginFormReg > span")[0];
span1 = document.querySelectorAll(".loginFormReg > span")[1];
span2 = document.querySelectorAll(".loginFormReg > span")[2];

pass1.classList.add("loginPasswordInputReg");
pass2.classList.add("loginPasswordInputReg2");
span0.style["display"] = "none";
span1.style["display"] = "none";
span2.style["display"] = "none";

loginFormReg.forEach((e) => {
  e.style["color"] = "azure";
});
