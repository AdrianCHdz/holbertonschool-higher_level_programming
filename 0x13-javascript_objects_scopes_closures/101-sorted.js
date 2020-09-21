#!/usr/bin/node
const myObject = require('./101-data').dict;
const newdict = {};
let values = [];
for (const key in myObject) {
  values.push(myObject[key]);
}
values = [...new Set(values)];
for (const item of values) {
  const newvalues = [];
  for (const key in myObject) {
    if (parseInt(item) === myObject[key]) {
      newvalues.push(key);
    }
  }
  newdict[item] = newvalues;
}
console.log(newdict);
