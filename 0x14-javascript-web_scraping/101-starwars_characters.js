#!/usr/bin/node

const request = require('request');
const end = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(end, function (error, response, body) {
  if (error) {
    throw error;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const l = [];
    characters.forEach(character => {
      l.push(new Promise((resolve, reject) => {
        request.get(character, function (error, response, body) {
          if (error) {
            reject(error);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        });
      }));
    });
    Promise.all(l).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
