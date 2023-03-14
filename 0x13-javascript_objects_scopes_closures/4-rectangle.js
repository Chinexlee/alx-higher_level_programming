#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }
   print () {
    let i = 0;
    while (i < this.height) {
        console.log('X'.repeat(this.width));
        i++;
    }
   }
    double () {
        this.width = this.width * 2;
        this.height = this.height * 2;
    }
    rotate () {
        let holder = this.width;
        this.width = this.height;
        this.height = holder;
    }
}
module.exports = Rectangle;
