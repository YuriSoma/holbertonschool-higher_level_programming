#!/usr/bin/node
let headerEl = document.querySelector("header");
let addClass = document.querySelector("div#red_header");
addClass.addEventListener("click", () =>{
    headerEl.classList.add("red");
})
