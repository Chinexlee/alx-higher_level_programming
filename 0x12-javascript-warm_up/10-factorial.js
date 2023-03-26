#!/usr/bin/node
const process = require('process');
const args = process.argv;
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const n = parseInt(args[2]);

if (isNaN(args[2])) {
  console.log(1);
} else {
  console.log(factorial(n));
}
