#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())          // parse the JSON from the response
  .then(data => {
    const characterDiv = document.getElementById('character');
    characterDiv.textContent = data.name;     // set the text content to the character's name
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
