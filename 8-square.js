#!/usr/bin/node
const args = parseInt(process.argv[2]);
if (!args) console.log('Missing size');
for (let i = 0; i < args; i++) {
  console.log('X'.repeat(args));
}
