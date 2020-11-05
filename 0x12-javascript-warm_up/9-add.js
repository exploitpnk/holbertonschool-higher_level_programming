#!/usr/bin/node
/*
Write a script that prints the addition of 2 integers

The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var
*/

const numberOne = parseInt(process.argv[2]);
const numbertwo = parseInt(process.argv[3]);

if (isNaN(numberOne) || isNaN(numbertwo)) {
  console.log('NaN');
} else {
  console.log(add(numberOne, numbertwo));
}

function add (a, b) {
  return a + b;
}
