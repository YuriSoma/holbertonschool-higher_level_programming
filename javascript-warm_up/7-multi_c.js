#!/usr/bin/node
const { argv } = require('node:process');

if (parseInt(argv[2])) {
  let times = parseInt(argv[2]);
  while (times > 0) {
    console.log('C is fun');
    times--;
  }
} else {
  console.log('Missing number of occurrences');
}
