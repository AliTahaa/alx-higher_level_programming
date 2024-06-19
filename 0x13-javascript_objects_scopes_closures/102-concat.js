#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
if (args.length < 3) {
  console.log('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}
const f1 = fs.readFileSync(args[0]);
const f2 = fs.readFileSync(args[1]);
fs.writeFileSync(args[2], f1 + f2);
