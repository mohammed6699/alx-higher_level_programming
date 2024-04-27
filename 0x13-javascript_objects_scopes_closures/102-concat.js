#!/usr/bin/node
const var1 = require('var1');
const var2 = var1.readFileSync(process.argv[2], 'utf8');
const var3 = var1.readFileSync(process.argv[3], 'utf8');
var1.writeFileSync(process.argv[4], var2 + var3);
