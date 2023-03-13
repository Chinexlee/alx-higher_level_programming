#!/usr/bin/node
//prints a message depending on the no of args

const process = require('process');
let args = process.argv;
if(args.length === 2){
    console.log("No argument");
}
else if(args.length === 3){
    console.log("Argument found");
}
else{
    console.log("Arguments found");
}
