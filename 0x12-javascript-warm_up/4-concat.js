#!/usr/bin/node
//scripts that prints two arguments passed to it
const process = require('process');
let args = process.argv;
console.log(args[2] + " is " + args[3]);
