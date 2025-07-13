#!/usr/bin/node
const { argv } = require('node:process');

if (parseInt(argv[2])) {
  let x = parseInt(argv[2]);
  let y; let xStr = '';
  while (x > 0) {
    y = parseInt(argv[2]);
    xStr = '';
    while (y > 0) {
      xStr += 'X';
      y--;
    }
    console.log(xStr);
    x--;
  }
} else {
  console.log('Missing size');
}
