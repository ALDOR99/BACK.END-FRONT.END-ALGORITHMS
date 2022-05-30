// Loops in Array & Objects

let cars = ["Bmv", "Mercedes", "Toyota"];
console.log(cars);

let people = [
    { firstName: "Ada", lastName: "Bilgi" },
    { firstName: "Yiğit", lastName: "Işık" },
    { firstName: "Çınar", lastName: "Yıldırım" },
];

// Arrays
for (let i = 0; i < cars.length; i++) {
    console.log(cars[i]);
}

// Objects
for (let i = 0; i < people.length; i++) {
    console.log(people[i].firstName);
}

for (let i = 0; i < people.length; i++) {
    console.log(people[i].lastName);
}

// for-in
// Arrays

for (let i in cars) {
    console.log(`index: ${i} value : ${cars[i]}`);
}
console.log("=======================");
//Objects

for (let i in people) {
    console.log(`index:${i} value : ${people[i].firstName}`)
}
console.log("====================")

// foreach

cars.forEach(function(item) {
    console.log(item);
});

people.forEach(function(item) {
    console.log(item);
});
console.log("==========");

people.forEach(function(item) {
    console.log(item.firstName);
});

console.log("====================");

// map : returns an array

let val = people.map(function(item) {
    return item.firstName + ' ' + item.lastName;
});
console.log(val);

console.log("---------------")

let numbers = [1, 5, 6, 8, 10];
let num = numbers.map(function(n) {
    return n * n;
});

console.log(num);