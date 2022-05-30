// Template  Literals

const fullName = "admin";
console.log(fullName);

const city = "none"
console.log(city);

const yearOfBirth = 2005;
console.log(yearOfBirth);


let val;

val = 'my name is '+fullName+
      ' I\'m '+(2018-yearOfBirth)+' years old '+
      ' and I live in '+city;

val = `my name is ${fullName} I'm ${(2018-yearOfBirth>=18)?'over 18':'under 18'} and I live in ${city}`;
console.log(val);















































































