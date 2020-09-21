#!/usr/bin/node
const Sqr = require('./5-square');
class Square extends Sqr {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
