let cart = {
  items: [
    { name: "Laptop", price: 15000, quantity: 1 },
    { name: "Mouse", price: 300, quantity: 2 }
  ],
  calculateTotal: function() {
    let total = 0;
    for (let item of this.items) {
      total += item.price * item.quantity;
    }
    return total;
  }
};

console.log(cart.calculateTotal());
//*************************************** */
//task2
function analyzeGrades(grades) {
  let passedSubjects = 0;
  let failedSubjects = 0;

  const subjects = Object.keys(grades);

  subjects.forEach(subject => {
    if (grades[subject] >= 50) {
      passedSubjects++;
    } else {
      failedSubjects++;
    }
  });

  return {
    passedSubjects: passedSubjects,
    failedSubjects: failedSubjects
  };
}

console.log(analyzeGrades({ math: 85, english: 45, physics: 90 }));
//**************************************** */
//task3
const buildUserProfile = (username, email, ...skills) => {
  return {
    username: username,
    email: email,
    skills: skills,
    skillCount: skills.length
  };
};

console.log(buildUserProfile("Hamdy", "hamyelkholyy@icloud.com", "HTML", "C#", "JavaScript"));
//************************************** */
//task4
const originalConfig = {
  theme: "dark",
  notifications: {
    email: true,
    sms: false
  }
};

const clonedConfig = {
  ...originalConfig,
  notifications: { ...originalConfig.notifications }
};

clonedConfig.notifications.sms = true;

if (originalConfig.notifications.sms === false) {
  console.log("Deep copy successful!");
} else {
  console.log("Deep copy failed!");
}
//******************************************* */
//task5
const basicInfo = [
  { id: 101, name: "Sara" },
  { id: 102, name: "Kareem" }
];

const jobInfo = [
  { id: 101, title: "Developer" },
  { id: 102, title: "Designer" }
];

const mergedEmployees = [];

for (let i = 0; i < basicInfo.length; i++) {
  mergedEmployees.push({
    id: basicInfo[i].id,
    name: basicInfo[i].name,
    title: jobInfo[i].title
  });
}

console.log(mergedEmployees);
//*************************************//
//task6
let cartData = [
  { name: "Book", price: 150, quantity: 2 },
  { name: "Pen", price: 20, quantity: 5 },
  { name: "Bag", price: 600, quantity: 1 }
];

function calculateCart(cart) {
  let totalPrice = 0;

  for (let item of cart) {
    totalPrice += item.price * item.quantity;
  }

  let discount = totalPrice >= 1000 ? totalPrice * 0.1 : 0;
  let finalPrice = totalPrice - discount;

  return {
    total: totalPrice,
    discount: discount,
    finalPrice: finalPrice
  };
}

console.log(calculateCart(cartData));
//**************************************** */
//task7
function calculate(...numbers) {
  if (numbers.length === 0) return null;

  let sum = 0;
  for (let num of numbers) {
    sum += num;
  }

  let max = Math.max(...numbers);
  let min = Math.min(...numbers);
  let average = sum / numbers.length;

  return {
    sum: sum,
    max: max,
    min: min,
    average: average
  };
}

console.log(calculate(10, 20, 30, 40, 50));
 