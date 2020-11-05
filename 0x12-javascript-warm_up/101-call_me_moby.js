#!/usr/bin/node

/*
Write a function that executes x times a function.

The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var
*/

exports.callMeMoby = function (x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
};
