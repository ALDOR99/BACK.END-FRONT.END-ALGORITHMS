// Window Object

let val;
var a = 10;

function abc() {
    return 0;
};

val = window;
// alert
alert("merhaba")

//promot
//var val = prompt('bir sayı giriniz ');
// confirm
val = confirm('emin misiniz ?'); //onaylamak
if (val) {
    console.log("ok");
} else {
    console.log("no");
}


// scroll

val = window.location;
console.log(val);
val = window.location.href;
console.log(val);

val = window.location.hostname;
console.log(val);

val = window.location.host;
console.log(val);

val = window.location.protocol;
console.log(val);

val = window.location.search;
console.log(val);