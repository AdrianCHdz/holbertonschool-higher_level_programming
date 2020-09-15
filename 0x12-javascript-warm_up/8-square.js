#!/usr/bin/node
const size = process.argv[2];
if (!size || isNaN(size)) {
  console.log('Missing size');
}
for (let x = 0; x < size; x++) {
  console.log('X'.repeat(size));
  /*
  for (let y = 0; y < size; y++) {
    process.stdout.write('X');
  }
  console.log();
  */
}
