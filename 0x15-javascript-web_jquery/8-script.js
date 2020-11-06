$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (response) {
  response.results.forEach(function (film) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});
