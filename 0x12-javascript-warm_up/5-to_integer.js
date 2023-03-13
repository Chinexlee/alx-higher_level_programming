#!/usr/bin/node
//prints script if first argument can be converted to int
const process = require('process');
let args = process.argv;
if(isNaN(args[2])){
    console.log('Not a number');
}
else{
    console.log('My Number: ' + parseInt(args[2]));
}
