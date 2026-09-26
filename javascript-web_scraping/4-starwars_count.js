#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter((film) => {
      return film.characters.some((character) => {
        return character.endsWith('/people/18/');
      });
    }).length;
    console.log(count);
  }
});
