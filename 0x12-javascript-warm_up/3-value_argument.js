#!/usr/bin/node
//script that prints the first argument passed to it

const process = require('process');
let args = process.argv;
let first = args[2];
if(args.length > 2){
    console.log(first);}
else{
    console.log('No argument');
}
