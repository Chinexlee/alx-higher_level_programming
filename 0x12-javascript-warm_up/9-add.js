#!/usr/bin/node
const process = require('process');
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
function add (a, b) {
  const result = a + b;
  console.log(result);
}
if (isNaN(a && b)) {
  console.log('NaN');
} else {
  add(a, b);
}
