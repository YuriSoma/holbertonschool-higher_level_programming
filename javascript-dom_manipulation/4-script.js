#!/usr/bin/node
let unList = document.querySelector("ul.my_list");
let addItem = document.querySelector("div#add_item");

addItem.addEventListener("click", () =>{
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  unList.appendChild(newItem);
})
