#!/usr/bin/node
let headerEl = document.querySelector("header");
let toggleClass = document.querySelector("div#toggle_header");

toggleClass.addEventListener("click", () =>{
  if (headerEl.classList == "green") {
    headerEl.classList.toggle("red");
  }
  else headerEl.classList.toggle("green");
})
