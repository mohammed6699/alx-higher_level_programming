#!/usr/bin/node

/*
 * script that reads and prints the content of a file.
*/
//import fs module in node.js
const fs = require('fs');

fs.readFile(process.argv[2], "utf-8", function(error, content){

        if (error){
                //check the process if error happen in reading the file
                //console will print the error
                console.error("error reading the file:", error);
        }else{
                //the console will read the file if successed
                console.log(content);
        }
});
