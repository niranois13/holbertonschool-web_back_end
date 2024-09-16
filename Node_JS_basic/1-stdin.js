const readline = require('readline');

const lineRead = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Welcome to Holberton School, what s your name?');

lineRead.question('', (name) => {
  console.log(`Your name is: ${name}`);

  lineRead.on('close', () => {
    console.log('This important software is now closing');
  });

});
