#!/usr/bin/node

const request = require('request');
const end = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request({ url: end, methods: 'GET' }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
