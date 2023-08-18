#!/usr/bin/node
/*
    Print a square with the character #
    
    The size of the square must be the first argument 
    of the program.
*/


if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1)
}

/*
   ParseInt was failing when the number was 10 or greater
   Fix: converting string using Number object in Javascript.
*/
const size = Number.parseInt(process.argv[2])
console.log(size)
let i, j;

for (i = 0 ; i < size ; i++) {
    for (j = 0 ; j < size ; j++) {
       process.stdout.write("#");
    }
    process.stdout.write("\n");
}
process.exit(0)
