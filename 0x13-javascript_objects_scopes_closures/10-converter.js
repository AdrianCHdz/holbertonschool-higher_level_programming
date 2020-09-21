#!/usr/bin/node
exports.converter = function (base) {
  function num (namber) {
    return namber.toString(base);
  }
  return num;
};
