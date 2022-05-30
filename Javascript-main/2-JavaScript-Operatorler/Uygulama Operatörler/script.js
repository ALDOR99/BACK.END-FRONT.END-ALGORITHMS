let IndexCan;
console.log(IndexCan);

let IndexAda;
console.log(IndexAda);


const kgCan = 60;
const kgAda = 40;


const heigtCan = 1.70;
const heigtAda = 1.50;

IndexAda = (kgAda) / (heigtAda*heigtAda);
console.log(IndexAda);

IndexCan = (kgCan) / (heigtCan*heigtCan);
console.log(IndexCan);

//

console.log(IndexAda.toFixed(2),IndexCan.toFixed(3));

//

let adaHigherIndex = IndexAda>IndexCan;
console.log(adaHigherIndex);

let canHigherIndex = IndexCan>IndexAda;
console.log(canHigherIndex);


console.log("Ada'nın kilo indeksi can'ın kilo indeksinden daha büyük : "+adaHigherIndex);


console.log("Can'ın kilo indeksi ada'nın kilo indeksinden daha büyük : "+canHigherIndex);

let AdaZayif = (IndexAda>=0) && (IndexAda<=18.4);
console.log(AdaZayif);
let AdaNormal = (IndexAda>=18.5) && (IndexAda<=24.9);
console.log(AdaZayif);
let AdaKilolu = (IndexAda>=25) && (IndexAda<=29.9);
console.log(AdaZayif);
let AdaSisman = (IndexAda>=30) && (IndexAda<=34.9);
console.log(AdaZayif);

console.log("Ada zayıf :"+AdaZayif);
console.log("Ada'nın kilosu normal : "+AdaNormal);
console.log("Ada kilolu mu : "+AdaKilolu);
console.log("Ada şişman mı : "+AdaSisman);






