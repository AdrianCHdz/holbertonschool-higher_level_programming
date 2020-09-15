#!/usr/bin/node
const args = parseInt(process.argv[2]);

function factorial (a) {
  if (a < 0) {
    return -1;
  }
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
if (!args) {
  console.log(1);
} else {
  console.log(factorial(args));
}
