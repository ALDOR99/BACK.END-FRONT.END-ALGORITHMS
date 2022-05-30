// Arrays

let names = ['çınar','sena','ada','yiğit'];
console.log(names);

let years = [2017,1970,1990,1998];
console.log(years);

let mix = ['sadık','turan',1983,null,undefined,['sinema','kitap']];
console.log(mix);

// // get array item
console.log(names[0]);
console.log(names[1]);
console.log(names[2]);
console.log(names[3]);
// // set array item

names[names.length]='emel';
console.log(names);




// // add item
years.push(1986);
console.log(years);
years.unshift(1986);
console.log(years);


// // remove item

years.pop();
console.log(years);
years.shift();
console.log(years);

// //indexof

let index = names.indexOf("ada");
console.log(index)

console.log("index : " +index);

// // reverse
names.reverse();
console.log(names);


// // sort
years.sort();
console.log(years);

// //concat
let  val = years.concat(names);
console.log(val);

// splice
console.log(names);
console.log(names.splice(0,1));

function over18(year){
    let age = 2018 - year;
    return age>=18;
}
console.log(over18(2000));
console.log(over18(2006));
console.log(over18(2009));
console.log(over18(2010));

// filter
//let val = years.filter(over18);

console.log(val);
console.log(names);
console.log(names.length);
console.log(typeof names);

console.log(years);
console.log(mix);




































