#!/usr/bin/node
const myVar = 'C is fun';
const args = process.argv[2];
if (!args || isNaN(args)) {
  console.log('Missing number of ocurrences');
}
for (let x = 0; x < args; x++) {
  console.log(myVar);
}
