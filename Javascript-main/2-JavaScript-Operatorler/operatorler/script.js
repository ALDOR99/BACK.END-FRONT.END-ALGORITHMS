//Operatörler

let val;
console.log(val);

const a =10;
console.log(a);

const b =5;
console.log(b);

const c=5;
console.log(c);

let d=3;
console.log(d);

// 1- Aritmetik Operatörler

val = a+b;
console.log(val);

val1 = a-b;
console.log(val1);

val2 = a*b;
console.log(val2);

val3 = a/b;
console.log(val3);

val4 = a%b;
console.log(val4);


val5 = d++;
console.log(val5);


val6 = ++d;
console.log(val6);

val7 = --d;
console.log(val7);


val8 = d--;
console.log(val8);


// 2- Atama Operatörleri

val = a;
console.log(val); 

val +=a;
console.log(val); // val = val + a;

val -=a;
console.log(val); // val = val - a;

val *=a;
console.log(val); // val = val * a;

val /=a; 
console.log(val); // val = val / a;

val %=a; // val = val % a;
console.log(val);

// 3- Karşılaştırma Operatörleri

val = a==b;
console.log(val);

val = b==c;
console.log(val);

val = b===c; // değer kontrolü & type
console.log(val);

val = 5 ==="5";
console.log(val);

val = a!=b;
console.log(val);

val = a!==b;
console.log(val);

val = a > b;
console.log(val);

val = b < a;
console.log(val);

val = a >= b;
console.log(val);

val = 5 >= 5;
console.log(val);

val = a <= b;
console.log(val);

// 4- Mantıksal Operatörler

// && (And)
// true  && true  => true
// true  && false => false
// false && false => false

val=  (a>b) && (a>c) 
console.log(val);

val = (a>b) || (a<c)
console.log(val);

val = !(a>b)
console.log(val);


// || (Or)
 
// true  && true  => true
// true  && false => true
// false && false => false


// ! (Not)

// !true  => false
// !false => true

console.log(val);
console.log(typeof val);


































