#!/usr/bin/node
const argList = process.argv.slice(2);
const numbers = argList.map(arg => parseInt(arg));

if (numbers.length < 2) {
	console.log(0);
} else {
	const sortedNo = numbers.sort((a, b) => b - a);
	console.log(sortedNo[1]);
}
