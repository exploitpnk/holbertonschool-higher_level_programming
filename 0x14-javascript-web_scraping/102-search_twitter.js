#!/usr/bin/node
/*
Write a Javascript script that takes in 3 strings and sends a search request to the Twitter API

Use the Twitter API search endpoint
Use the Application-only authentication flow to do a search request
Create an Twitter application here
The first argument must be the Consumer Key (API Key)
The second argument must be the Consumer Secret (API Secret)
The third argument must be the search string
Display only 5 results in the following format: [<Tweet ID>] <Tweet text> by <Tweet owner name> (see example below)
Only these modules are allowed: request, base-64 and utf8
You don’t need to check arguments passed to the script (number or type)
*/
const base64 = require('base-64');
const request = require('request');
const utf8 = require('utf8');

const promise = new Promise(function (resolve, reject) {
  const token = utf8.decode(base64.encode(`${process.argv[2]}:${process.argv[3]}`));
  const options = {
    url: 'https://api.twitter.com/oauth2/token',
    headers: {
      Authorization: `Basic ${token}`,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    },
    form: {
      grant_type: 'client_credentials'
    }
  };
  request.post(options, function (error, response, body) {
    if (!error) {
      resolve(JSON.parse(body).access_token);
    }
  });
});

promise.then(
  result => search(result),
  error => console.log(error)
);

function search (bearer) {
  const options = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: {
      Authorization: `Bearer ${bearer}`
    },
    qs: {
      q: process.argv[4],
      count: '5'
    }
  };
  request.get(options, function (error, response, body) {
    if (!error) {
      const tweets = JSON.parse(body).statuses;
      tweets.forEach((t) => console.log(`[${t.id}] ${t.text} by ${t.user.name}`));
    }
  });
}
