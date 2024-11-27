const btn = document.querySelector("button");
const body = document.body;
// const black = document.querySelector(".dark");
const wel = document.getElementById("welcome")

btn.addEventListener("click", function() {
    console.log("hello")
  if (body.style.backgroundColor === "white"){
    body.style.backgroundColor = "black"
    wel.style.color = "white"
  }else{
    body.style.backgroundColor = "white"
    wel.style.color = "black"
  }

});
