#!/usr/bin/node

/*
* script that display the status code of a GET request.
*/

//import request module
const request = require('request');
//import hhtp request
request.get(process.argv[2])
//http request import
        .on ('response', function (response) {
        console.log('code: ${ response.statuscode}');
});
