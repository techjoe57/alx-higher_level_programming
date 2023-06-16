#!/usr/bin/node
const value = Number(process.argv[2]);
let pattern = '';
if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    for (let j = 0; j < value; j++) {
      pattern += 'X';
    }
    pattern += '\n';
  }
  console.log(pattern);
}
