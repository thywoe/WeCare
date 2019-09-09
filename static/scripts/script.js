let reg1 =document.querySelector(".reg1")
 reg1.addEventListener("click", ()=> {
 document.querySelector(".register-form").style.display = "block";
 document.querySelector(".login-form").style.display = "none";
    })

let log1 =document.querySelector(".log1")
log1.addEventListener("click", ()=> {
document.querySelector(".login-form").style.display = "block";
document.querySelector(".register-form").style.display = "none";
    })

let reg =document.querySelector(".reg")
reg.addEventListener("click", ()=> {
document.querySelector(".register-form").style.display = "block";
document.querySelector(".login-form").style.display = "none";
    })

let log =document.querySelector(".log")
log.addEventListener("click", ()=> {
document.querySelector(".login-form").style.display = "block";
document.querySelector(".register-form").style.display = "none";
    })