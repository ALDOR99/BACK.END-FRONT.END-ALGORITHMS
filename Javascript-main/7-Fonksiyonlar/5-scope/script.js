// Scopes

// ** Global Scopes

var name = 'Çınar';
var age = 25;

function logName() {
    var name = 'Ada';
    var age = '12';
    console.log('function scope', name, age);
}
logName()

if (true) {
    var age = 30;
    console.log("block scope", name, age);

}
console.log(age);

// ** Local Scopes

// Fonksiyonlar kendi scope 'larını oluşturur.
// **Block'lar yeni scope oluşturmaz.
// ES6 ile gelen let ve const block scope oluşturur.
console.log("******************");

if (true) {
    var model = "opel";
    let year = 2016;
    const color = "white";
    console.log("block scope", model, year, color);

}
console.log(model);


var i = 1;

for (let i = 0; i < 10; i++) {
    console.log('i', i);
}

console.log(i);



function sinif(not) {

    if (not >= 0 && not < 50) return 'F';
    if (not >= 50 && not < 70) return 'D';
    if (not >= 70 && not < 80) return 'C';
    if (not >= 80 && not < 90) return 'B';
    if (not >= 90) return 'A';
}

var y = sinif(60);

alert(y);

function kare(x) {
    return x * x;
}
var y = kare(5);
alert("sonuc...." + y); // cıktı