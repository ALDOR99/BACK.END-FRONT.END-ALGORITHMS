// Loops

// for loop

// for loop

for (let i = 1; i <= 10; i++) {

    if (i == 3) {
        console.log('en sevdiğim rakam :' + i);
        continue;
    }

    if (i == 6) {
        console.log('en sevmediğim rakam : 6');
        break;
    }

    console.log(i);
}

// while loop

for (let i = 0; i <= 10; i++) {
    console.log(i);
}

let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}

// do-While loop

//let i = 0;
//do {
//    console.log(i);
//    i++;
//} while (i < 10);

console.log("=== === === === ===")

let sonuc = 1;
for (let i = 10; i > 0; i--) {
    if (i % 2 == 1) {
        sonuc *= i;
    }
}
console.log(sonuc);
console.log("==================")


let val = "\n";
for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
        val += "* "
    }
    val += "\n";
}
console.log(val);
console.log("=============");

var kisi = { ad: "Murat", soyad: "Elicaliskan", yas: 30 };

var mesaj = "";
var x;
for (x in kisi) {
    mesaj += kisi[x];
}
console.log(mesaj);

// mesaj değişken "Murat Elicaliskan 30" olacaktır.

console.log("====================");


do {
    mesaj += "Benim sayım " + i + "<br />";
    i++;
}

while (i < 10);
//console.log(i);


var ileti = "";

for (i = 0; i <= 10; i++) {
    if (i == 3)
        continue;

    ileti += "Benim sayım " + i + "<br />";
}
console.log(ileti)
console.log("==============");



var araba = { marka: "Fiat", model: "500", renk: "beyaz" }

for (i in araba) {
    alert(i + " - " + araba[i]);
}

console.log("==============")


//var liste = ["Elma", "Armut", "Portakal", "Muz", "Kivi", "Karpuz", "Çilek"];
//var i = 0;

//for (; liste[i];) {

//   alert(liste[i]);
// i++;
//}