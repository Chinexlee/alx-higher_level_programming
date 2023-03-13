#!/usr/bin/node
//computes and print a factorial
const process = require('process');
let args = process.argv;

//creating a function for factorial
function factorial(n){
    if(n === 0 || n === 1){
        return 1;
    } else{
        return n * factorial(n - 1);
    }
}

let n = parseInt(args[2]);

if(isNaN(args[2])){
    console.log(1);
} else{
    console.log(factorial(n));
}
