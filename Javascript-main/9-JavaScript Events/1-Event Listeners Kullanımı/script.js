// Event Listeners

const btn = document.querySelector("#btnDeleteAll");
//console.log(btn);

const btn2 = document.querySelector("#btnAddNewTask");
console.log(btn2);

btn.addEventListener('click', function(e) {

    let val;

    val = e;

    val = e.target;
    val = e.target.id;
    val = e.target.classList;
    val = e.type;

    console.log(val);

    e.preventDefault();

});

btn.addEventListener('click', btnClick);
btn.addEventListener('click', btnClick2);
btn2.addEventListener('click', btnClick);

function btnClick() {
    console.log("btn clicked");

}

function btnClick2() {
    console.log("btn 2 clicked");
}