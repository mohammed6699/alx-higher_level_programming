#!/usr/bin/node

const passedarg = process.argv[2];
const x = parseInt(passedarg);

if (isNaN(x)) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < x; i++){
	console.log ('C is fun');
	}
}
