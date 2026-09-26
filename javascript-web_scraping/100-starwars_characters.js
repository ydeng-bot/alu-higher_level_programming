#!/usr/bin/node

const request = require('request');

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

function printCharacter (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      printCharacter(characters, index + 1);
    }
  });
}

request(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacter(characters, 0);
  }
});
