// Define a global variable in NodeJS
global.myVariable = 'Hello World';

// Access the global variable
console.log(myVariable); // Output: Hello World

console.log("Press Enter to continue...");
process.stdin.resume();
process.stdin.on("data", () => {
    process.stdin.pause();
});

