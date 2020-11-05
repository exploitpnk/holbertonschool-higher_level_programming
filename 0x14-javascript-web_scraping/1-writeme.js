#!/usr/bin/node
/*
Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object
*/
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return (-1);
  }
});
