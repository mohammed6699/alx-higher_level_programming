#!/usr/bin/node

const argNumber = process.argv[2];
const passedNumber = parseInt(argNumber);

if (isNaN(passedNumber)) {
	console.log('Not a number');
} else {
	console.log (`My number:${passedNumber}`);
}
