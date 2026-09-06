let num1 = 10;
let num2 = 25;
let num3 = 18;

let largest = Math.max(num1, num2, num3);
console.log(largest);
//********************************//
// task2//
let year = 2024;

if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log("Leap Year");
} else {
    console.log("Not a Leap Year");
}
//***************************** */
//task3//
let units = 180;
let bill = 0;

switch (true) {
    case (units <= 50):
        bill = units * 0.50;
        break;
    case (units <= 150):
        bill = (50 * 0.50) + ((units - 50) * 0.75);
        break;
    case (units <= 250):
        bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20);
        break;
    default:
        bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50);
        break;
}

console.log(bill);
//****************************** */
//task4//
let count = 20;

while (count >= 1) {
    if (count === 13) {
        break;
    }
    
    if (count % 5 === 0) {
        count--;
        continue;
    }
    
    console.log(count);
    count--;
}
//************************************* */
//task5//
for (let i = 1; i <= 5; i++) {
    let row = "";
    for (let j = 1; j <= i; j++) {
        row += j;
    }
    console.log(row);
}
//******************************* */
//task6//
let password = "JavaScript123";

if (password === "JavaScript123") {
    console.log("Access Granted");
} else {
    console.log("Access Denied");
}
//*******************************************/ */
//task7//
{
  let num1 = 10;
  let num2 = 5;
  let operator = "+";

  switch (operator) {
    case "+":
      console.log(num1 + num2);
      break;
    case "-":
      console.log(num1 - num2);
      break;
    case "*":
      console.log(num1 * num2);
      break;
    case "/":
      console.log(num1 / num2);
      break;
    case "%":
      console.log(num1 % num2);
      break;
    default:
      console.log("Invalid Operator");
      break;
  }
}