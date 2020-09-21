#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let x = 0; list[x]; x++) {
    if (list[x] === searchElement) {
      count++;
    }
  }
  return count;
};
