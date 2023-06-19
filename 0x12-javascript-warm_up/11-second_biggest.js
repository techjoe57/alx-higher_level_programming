#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const argsList = args.sort();
  const secondHighest = argsList[args.length - 2];
  console.log(secondHighest);
}
