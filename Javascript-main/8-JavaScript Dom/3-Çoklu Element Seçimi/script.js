// Selecting Elements

// *** Single Elements
//    *** document.getElementById()
//    *** document.querySelector()

// *** Multiple Elements
// class name
// document.getElementsByClassName()

let val;

val = document.getElementsByClassName("list-group-item");
console.log(val);

val = document.getElementsByClassName("list-group-item")[0];
console.log(val);

val = document.getElementsByClassName('list-group-item')[2];
console.log(val);

val = val[2];
console.log(val);



val = document.getElementsByClassName("list-group-item");
val[1].style.color = 'blue';
val[1].style.fontSize = '40px';
val[2].textContent = 'Lord alis';

for (let i = 0; i < val.length; i++) {
    console.log(val[i].style.color = "red");
    console.log(val[i].textContent = "new item");
}

//document.getElementsByTagName()

val = document.getElementsByTagName("li");

val = document.getElementById('task-list').getElementsByTagName('a');
console.log(val);


// document.querySelectorAll()

val = document.querySelectorAll("li");
console.log(val);

val.forEach(function(item) {
    item.style.background = "#8599ad";
});
console.log(val);