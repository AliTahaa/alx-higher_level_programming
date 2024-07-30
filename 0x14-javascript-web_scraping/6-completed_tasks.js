#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const Dict = {};

request(url, function (error, data, body) {
  if (error) {
    console.log(error);
  } else {
    const response = JSON.parse(body);

    for (let i = 0; i < response.length; i++) {
      if (response[i].completed === true) {
        if (Dict[response[i].userId] === undefined) {
          Dict[response[i].userId] = 1;
        } else {
          Dict[response[i].userId] += 1;
        }
      }
    }
  }
  console.log(Dict);
});
