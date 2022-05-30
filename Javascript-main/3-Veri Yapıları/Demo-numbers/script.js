var num = 15.32456789;
console.log(num);

// toplamda 3 basamaklı sayı kullan
console.log(num.toPrecision(3))

// ondalık kısmı 3 basamakta sınırla
console.log(num.toFixed(4))

// en yakın sayıya yuvarla
console.log(Math.round(num));


// yukarı yuvarla
console.log(Math.ceil(num));

var num1 = 16.2;
console.log(Math.ceil(num1));


// 1,2,10,56,20 sayılarından en küçüğü ve en büyüğünü bul

var min = 50;
var max = 100;

console.log(Math.floor(min+Math.random()*(max-min)))

/* Bir personelin yaptığı mesai'ye göre aldığı maaşı hesaplayalım.
   ** Brüt maaş  : 3700 TL
   ** Brüt mesai : 10.3 TL
   Ağustos ayı mesai toplamı 42 saat ise toplam brüt maaş nedir ?
   Brüt maaş üzerinden toplam kesinti oranı %25 ise alınacak toplam net maaş nedir ?
*/

var brutMaas = 3700;
var mesaiUcreti = 10.3;
var mesaiSuresi = 42;

var toplamBrutMaas = brutMaas + (mesaiUcreti*mesaiSuresi);

var toplamNetMaas = toplamBrutMaas - toplamBrutMaas*0.25

console.log(toplamBrutMaas.toFixed(2),toplamNetMaas.toFixed(2));












































