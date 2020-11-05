#!/usr/bin/node
/*
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

Your script must import dict from the file 101-data.js
In the new dictionary:
A key is a number of occurrences
A value is the list of user ids
Print the new dictionary at the end
*/
const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  if (typeof (newDict[dict[key]]) === 'undefined') {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}
console.log(newDict);
