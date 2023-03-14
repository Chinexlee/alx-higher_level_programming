#!/usr/bin/node
const process = require('process');
let args = process.argv;
let a = parseInt(args[2]);
let b = parseInt(args[3]);
function add(a, b){
    let result = a + b;
    console.log(result);
}
if(isNaN(a && b)){
    console.log('NaN');
} else{
    add(a, b);
}
