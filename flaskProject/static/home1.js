function myFunction(x) {
  x.classList.toggle("change");}

 function openNav(x) {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  x.classList.toggle("change");

}

function closeNav(x) {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
  x.classList.toggle("changeclose");
}