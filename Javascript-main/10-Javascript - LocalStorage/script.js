// LOCAL STORAGE:Yerel Depolama

console.log(localStorage);

console.log("___________________")
let val;
//set item

const firstName = localStorage.setItem('firstName', 'Alis');
const lasName = localStorage.setItem("lastName", "Durna");

let hobies = ["sinema", "kitap", "egzersiz"];
console.log(hobies);
//get item
val = localStorage.getItem("firstName");
console.log(val);
val = localStorage.getItem("lastName");
console.log(val);


// remove item
// localStorage.removeItem('firstName');
// localStorage.removeItem('lastName');

// clear
// localStorage.clear();

// set array to storage
localStorage.setItem('hobies', JSON.stringify(hobies));

val = JSON.parse(localStorage.getItem('hobies'));

console.log(val);
console.log(localStorage);


// SESSION STORAGE
// const city = sessionStorage.setItem('city','Kocaeli');
// const country = sessionStorage.setItem('country','Türkiye');

//  console.log(sessionStorage);