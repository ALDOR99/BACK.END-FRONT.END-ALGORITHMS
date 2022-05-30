// Mouse Events
const btn = document.querySelector('#btnDeleteAll');
const ul = document.querySelector('#task-list');

// click
// btn.addEventListener('click', eventHandler);
// console.log(btn);
// ul.addEventListener('click', eventHandler);
// console.log(ul);

// double click

//btn.addEventListener("dblclick", eventHandler);

//mouse down
//btn.addEventListener("mousedown", eventHandler);
// //mouse up
//btn.addEventListener("mouseup", eventHandler);

// // mouseenter
//ul.addEventListener('mouseenter', eventHandler);
// // mouseleave
//ul.addEventListener('mouseleave', eventHandler);

// // mouseover
//ul.addEventListener('mouseover', eventHandler);

// // mouseout
//ul.addEventListener('mouseout', eventHandler);

// mouse move

const h5 = document.querySelector("h5");
console.log(h5);

ul.addEventListener("mousemove", eventHandler);
console.log(ul);


function eventHandler(event) {
    console.log(`event type : ${event.type}`);
    h5.textContent = `Mouse X : ${event.offsetX} Mouse Y : ${event.offsetY}`;
}