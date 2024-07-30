#!/usr/bin/node

const req = require('req');
const url = process.argv[2];

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
