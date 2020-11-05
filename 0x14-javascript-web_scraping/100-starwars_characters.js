#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module request
*/
const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(function (element) {
      request(element, function (err, response, body) {
        if (err) {
          return console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
