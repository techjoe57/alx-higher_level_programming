#!/usr/bin/node
const firstInt = Number(process.argv[2]);
const secondInt = Number(process.argv[3]);
function add (first, second) {
  if (isNaN(first) || isNaN(second)) {
    return NaN;
  } else {
    return first + second;
  }
}
console.log(add(firstInt, secondInt));
