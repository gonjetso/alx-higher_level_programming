#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destFile = process.argv[4];

const file1Contents = fs.readFileSync(sourceFile1);
const file2Contents = fs.readFileSync(sourceFile2);

const result = Buffer.concat([file1Contents, file2Contents]);

fs.writeFileSync(destFile, result);
console.log(`Successfully concatenated ${sourceFile1} and ${sourceFile2} to ${destFile}.`);
