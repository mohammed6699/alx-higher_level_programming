#!/usr/bin/node

function add(a, b) {
	let result = a + b;
	return result;
}

const arg2 = parseInt(process.argv[2]);
const arg3 = parseInt(process.argv[3]);
const result = add(arg2, arg3);
console.log(result);
