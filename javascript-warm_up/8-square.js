#!/usr/bin/node
const { argv } = require('node:process');

if (parseInt(argv[2])) {
  let x = parseInt(argv[2]);
  let y; let x_str = '';
  while (x > 0) {
    y = parseInt(argv[2]);
    x_str = '';
    while (y > 0) {
      x_str += 'x';
      y--;
    }
    console.log(x_str);
    x--;
  }
} else {
  console.log('Missing size');
}
