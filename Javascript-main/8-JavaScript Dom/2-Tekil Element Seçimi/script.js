// Selecting Elements
// *** Single Elements

// document.getElementById()

let val;

val = document.getElementById("header");
console.log(val);
//id ile secmek

val = document.getElementById("header").id;
console.log(val);

val = document.getElementById("header").className;
console.log(val);

val = document.getElementById('header');
val.style.fontSize = "50px";
val.style.color = "red";
val.style.fontWeight = "bold";
val.style.display = "none";

console.log("============");

document.getElementById("header").innerText = "Lord Alis";
//document.getElementById("header").innerText = "<b>my ToDo App</b>";
document.getElementById("header").innerText = "<b>Lord Alis</b>";

document.getElementById('header').innerHTML = '<b>my ToDo App</b>';
console.log(val);

// document.querySelector()

document.querySelector("li").style.color = "red";
document.querySelector("li:last-child").style.color = "blue";
document.querySelector("li:nth-child(2").style.color = "yellow";
document.querySelector("li:nth-child(3").textContent = "task item";
document.querySelector('li:nth-child(4)').textContent = 'task item';

document.querySelector('li').className = 'list-group-item list-group-item-primary';

document.querySelector('li').classList.add('active');

// *** Multiple Elements