#!/usr/bin/node
const { argv } = require('node:process');

if (Object.keys(argv).length == 2) {
  console.log('No argument');
} else if (Object.keys(argv).length == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
