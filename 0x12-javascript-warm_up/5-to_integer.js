#!/usr/bin/node
const process = require('process');
let args = process.argv;
if(isNaN(args[2]) || args[2] === undefined){
    console.log('Not a number');
}
else{
    console.log('My Number: ' , parseInt(args[2]));
}
