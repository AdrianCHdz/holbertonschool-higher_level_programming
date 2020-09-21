#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newlist = list.map(function (x, index) {
  return index * x;
});
console.log(newlist);
