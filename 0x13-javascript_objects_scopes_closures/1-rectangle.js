#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    console.log(typeof (w), typeof (h));
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
