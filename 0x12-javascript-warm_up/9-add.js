#!/usr/bin/node
//prints addition of 2 integers

const process = require('process');
let args = process.argv;
let a = parseInt(args[2]);
let b = parseInt(args[3]);

//defining function
function add(a, b){
    let result = a + b;
    console.log(result);
}

if(isNaN(a && b)){
    console.log('NaN');
} else{
    add(a, b);
}
