#!/usr/bin/node
/*
 * script that prints the title of a Star Wars movie 
 * the episode number matches a given integer.
 */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function(error, response, body) {
	if (error)
	{
		console.error(error)
	}
	else{
		const movie = JSON.parse(body);
		console.log(movie.title);
	}
});
