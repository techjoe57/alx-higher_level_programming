#!/usr/bin/node

const rq = require('request');

const apiUrl = process.argv[2];

rq(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId;
        if (!completedTasks[userId]) {
          completedTasks[userId] = 0;
        }

        completedTasks[userId]++;
      }
    }

    console.log(completedTasks);
  }
});
