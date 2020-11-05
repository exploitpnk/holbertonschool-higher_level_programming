#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request
*/
const request = require('request');
const uri = process.argv[2];

request.get(uri, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = {};

    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.userId in result) {
          result[task.userId]++;
        } else {
          result[task.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
