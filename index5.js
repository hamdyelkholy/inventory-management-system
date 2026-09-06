// ==========================================
// Question 1
// ==========================================
function sayHello() {
    setTimeout(() => {
        console.log("Hello JavaScript");
    }, 3000);
}

sayHello();


// ==========================================
// Question 2
// ==========================================
function printWelcome() {
    let intervalId = setInterval(() => {
        console.log("Welcome");
    }, 2000);

    setTimeout(() => {
        clearInterval(intervalId);
    }, 10000);
}

printWelcome();


// ==========================================
// Question 3
// ==========================================
function displayMessage() {
    console.log("Task Completed");
}

function executeTask(callback) {
    callback();
}

executeTask(displayMessage);


// ==========================================
// Question 4
// ==========================================
function checkAge(age) {
    return new Promise((resolve, reject) => {
        if (age >= 18) {
            resolve("Access Granted");
        } else {
            reject("Access Denied");
        }
    });
}

checkAge(20)
    .then(result => console.log(result))
    .catch(error => console.log(error));


// ==========================================
// Question 5
// ==========================================
const downloadPromise = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Downloaded");
    }, 3000);
});

downloadPromise.then(result => console.log(result));


// ==========================================
// Question 6 
// ==========================================
function getUsers() {
    fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => response.json())
        .then(users => {
            users.forEach(user => console.log(user.name));
        })
        .catch(error => console.log("Something went wrong."));
}

getUsers();


// ==========================================
// Question 7
// ==========================================
async function getUsersWithHandling() {
    try {
        let response = await fetch('https://jsonplaceholder.typicode.com/users');
        let users = await response.json();
        console.log(users);
    } catch (error) {
        console.log("Something went wrong.");
    }
}

getUsersWithHandling();


// ==========================================
// Question 9
// ==========================================
let username = "";

try {
    if (!username) {
        throw new Error("Username is empty");
    }
} catch (error) {
    console.log(error.message);
}


// ==========================================
// Question 10
// ==========================================
async function displayUsersInfo() {
    try {
        let response = await fetch('https://jsonplaceholder.typicode.com/users');
        let users = await response.json();
        
        users.forEach(user => {
            console.log(`Name: ${user.name}`);
            console.log(`Email: ${user.email}`);
            console.log(`Company Name: ${user.company.name}`);
            console.log('-------------------');
        });
    } catch (error) {
        console.log("Something went wrong.");
    }
}

displayUsersInfo();