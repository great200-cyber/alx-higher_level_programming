#!/usr/bin/node
const args = parseInt(process.argv[2]);
let i = 0;
if (!args) console.log('Missing number of ocurrences');
while (i < args) {
  console.log('C is fun');
  i++;
}
