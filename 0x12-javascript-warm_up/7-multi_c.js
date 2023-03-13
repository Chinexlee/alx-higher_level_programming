#!/usr/bin/node
//prints stings no of time argument passed
const process = require('process');
let args = process.argv;
if(isNaN(args[2])){
    console.log("Missing number of occurrences");
}
else{
    for(let i = 0; i < parseInt(args[2]); i++){
        console.log("C is fun");
 }
}
