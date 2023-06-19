#!/usr/bin/node
const value = Number(process.argv[2]);
function factorial (value) {
  if (isNaN(value) || value === 0) {
    return 1;
  } else {
    return value * factorial(value - 1);
  }
}
console.log(factorial(value));
