fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const moviesList = document.getElementById('list_movies');
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      moviesList.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
