#!/usr/bin/node
//prints a square

const process = require('process');
let args = process.argv;
let letter = '';
if(isNaN(args[2])){
    console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
