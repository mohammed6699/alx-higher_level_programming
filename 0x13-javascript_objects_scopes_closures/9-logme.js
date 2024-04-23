#!/usr/bin/node
let nom = 0;
exports.logMe = function (item) {
	console.log(`${nom++}: ${item}`);
};

