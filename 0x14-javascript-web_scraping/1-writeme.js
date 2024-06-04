#!/usr/bin/node

/*
 * script that writes a string to a file.
 */

// import fs module for node.js
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', error=> {
        // process.argv[2] the file to write in
        // process.argv[3] the sentence to write in the file
        if (error){
                console.error(error);
        }
});
