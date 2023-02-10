#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
