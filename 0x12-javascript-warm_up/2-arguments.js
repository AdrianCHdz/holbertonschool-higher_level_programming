#!/usr/bin/node
const args = process.argv.slice(2).length;
if (!args) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
