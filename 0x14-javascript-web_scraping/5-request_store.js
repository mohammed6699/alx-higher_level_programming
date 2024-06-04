#!/usr/bin/node
/*
 * script that gets the contents of a webpage and stores it in a file.
 */

// import request module
const request = require('request');
// import fs module
const fs = require('fs');
// use request modue to perform http request and store the data by fs
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
