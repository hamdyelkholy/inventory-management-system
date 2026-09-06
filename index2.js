// Task 1
function sayHello(name) {
  console.log("Hello " + hamdy + " to JavaScript");
}

// Task 2
function printNumbers(limit) {
  for (let i = 1; i <= limit; i++) {
    console.log(i);
  }
}

// Task 3
function sumArray(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}

// Task 4
const findLargest = function(numbers) {
  let largest = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      largest = numbers[i];
    }
  }
  return largest;
};

// Task 5
const sum = (a, b) => a + b;
const subtract = (a, b) => a - b;
const multiply = (a, b) => a * b;

function calculator(a, b, operationCallback) {
  return operationCallback(a, b);
}

// Task 6
const squareExpression = function(number) {
  return number * number;
};

const squareArrow = (number) => number * number;

// Task 7
var company = "Tech Corp";

function showDepartment() {
  let manager = "Ahmed";
  console.log(company);
  console.log(manager);
}

showDepartment();


// Task 8
(function() {
  let user = "Ahmed";
  console.log("Welcome " + user);
})();

// Task 9
let fruits = ["Apple", "Banana"];

fruits.push("Orange");
fruits.unshift("Mango");
fruits.pop();
fruits.shift();

console.log(fruits);

// Task 10
let names = ["Ahmed", "Ali", "Sara", "Mona"];

names.splice(1, 2);
console.log(names);

names.splice(1, 0, "Omar");
console.log(names);

let newArray = [names[1].toLowerCase(), names[0].toLowerCase()];
console.log(newArray);

console.log(names.indexOf("Ahmed"));

// Task 11
let skills = ["HTML", "CSS", "JavaScript"];

if (skills.includes("JavaScript")) {
  console.log("Skill Found");
}

console.log(skills.join(" | "));