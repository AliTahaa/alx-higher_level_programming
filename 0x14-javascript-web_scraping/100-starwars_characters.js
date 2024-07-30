#!/usr/bin/node

const request = require('request');
const end = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(end, function (error, response, body) {
  if (error) {
    throw error;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request.get(character, function (error, response, body) {
        if (error) {
          throw error;
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
