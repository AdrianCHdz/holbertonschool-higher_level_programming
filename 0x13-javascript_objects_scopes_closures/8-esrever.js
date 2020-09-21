#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [...list];
  for (let x = 0, y = list.length - 1; list[x]; x++, y--) {
    newlist[x] = list[y];
  }
  return newlist;
};
