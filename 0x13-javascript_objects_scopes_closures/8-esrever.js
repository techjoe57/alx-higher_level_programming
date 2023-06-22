#!/usr/bin/node
exports.esrever = function (list) {
  arr1 = [];
  list.forEach(element => {
    arr1.unshift(element);
  });
  console.log(arr1);
};
