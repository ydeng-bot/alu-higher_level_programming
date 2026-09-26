#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const counts = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (counts[todo.userId] === undefined) {
          counts[todo.userId] = 0;
        }
        counts[todo.userId]++;
      }
    });

    console.log(counts);
  }
});
