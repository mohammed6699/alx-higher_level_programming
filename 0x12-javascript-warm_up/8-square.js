#!/usr/bin/node

const squareSize = process.argv[2];
const square =  parseInt(squareSize);
const x = 'x';

if (isNaN(square)) {
	console.log('Missing size');
} else {
	for(let i = 0;i < square; i++) {
		console.log(x.repeat(square));
	}
}
