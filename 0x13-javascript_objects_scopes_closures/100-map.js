#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
//print a list in data file
console.log(list.map((item, index) => item * index));
