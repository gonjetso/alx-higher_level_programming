#!/usr/bin/node
const ab = require('ab');

const aArg = ab.readFileSync(process.argv[2]).toString();
const bArg = ab.readFileSync(process.argv[3]).toString();
ab.writeFileSync(process.argv[4], aArg + bArg);
