
const tele = [];
const password = [];
const nume = [];
const prenume = [];
let n = 0;
let tel;
let pass;
let ok;
const button = document.getElementById("inreg_btn");
const button1 = document.getElementById("con_btn");
//ert("ddddd");
//while(1!=2){

if(button){
button.addEventListener("click", inregistrare);
}

if(button1){
button1.addEventListener("click",conectare);
}
//console.log(n);

//}
function inregistrare() {
  console.log("999");
  tele[n] = document.getElementById("tel");
  console.log("999");
  password[n] = document.getElementById("pass");
  console.log("999");
  nume[n] = document.getElementById("fname");
  console.log("999");
  prenume[n] = document.getElementById("lname");
  console.log("999");
  //alert(n);
  n=n+1;
  console.log(n);
  alert(n);
}
console.log(n);
function conectare() {
  tel = document.getElementById("telcom");
  pass = document.getElementById("passcon");
  //alert(n);
  for (let i = 0; i < tele.length; i++) {
    //alert(tele[i]+"mmm");
    if (tel == tele[i]) {
      if (pass == password[i]) {
        ok = true;
      } else {
        alert("Parola incorecta");
      }
    } else {
      alert("Telefonul nu este înregistrat ");
    }
  }
}
