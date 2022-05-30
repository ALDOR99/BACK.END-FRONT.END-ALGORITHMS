// Numbers

let val;

val = Number("10");
console.log(val)
console.log(typeof(val));

val = parseInt("10");
console.log(val);

val = parseFloat("10.5");
console.log(val);
console.log(typeof(val));

val = parseInt('a10a');
console.log(val);
console.log(val);

val = isNaN('10');
console.log(val);

val = isNaN('a10');
console.log(val);

var num = 10.12456789;
console.log(num);

val = num.toPrecision(6);
console.log(val);

val = num.toFixed(2);
console.log(val);
//


val = Math.PI;
console.log(val);
//
val = Math.round(2.4);
console.log(val);
//
val = Math.round(2.7);
console.log(val);
//
val = Math.ceil(2.4);
console.log(val);
//
val = Math.ceil(2.6);
console.log(val);
//
val = Math.floor(2.4);
console.log(val);
//
val = Math.floor(2.7);
console.log(val);
//
val = Math.sqrt(64);
console.log(val);
//
val = Math.pow(2,4);//
console.log(val);
//
val = Math.abs(-100);
console.log(val);
//
val = Math.min(1,2,3,2,4,9);
console.log(val);
//
val = Math.max(4,5,6,4,98,7);
console.log(val);
//
val = Math.floor(Math.random()*100+1);
console.log(val);
console.log(typeof val);

//İnanılmaz örneğim
let a ="10";
let b = 10;

if(a===b)
{
    console.log("Eşittir.");
}
else{
console.log("Eşit değildir.");
}

// const değiştirilemez.

const firstName='Sena';
const age = 19;
const isStudent = false;
const school = 'university';

if(firstName === "Sena")
{
    console.log()
}

// if(firstName === 'Sena'){
//     console.log('Merhaba Sena');
// }

// if (age === 19){
//     console.log('yaşınız 19');
// }

// if (isStudent){
//     console.log('Merhaba öğrenci');
// }else{
//     console.log('Merhaba işler nasıl');
// }
























