#!/usr/bin/node

/*
Update this script by adding a new function incr that increments the integer value.

You are not allowed to use var
*/
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);
myObject.incr = function () {
  this.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
