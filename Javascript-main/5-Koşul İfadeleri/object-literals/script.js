// Object Literals


let val;

let person = {
    firstName: 'Alis',
    lastName: 'Space',
    age: 21,
    hobbies: ['music', 'game'],
    address: {
        city: 'Space',
        country: 'Space'
    },
    getBirthYear: function() {
        return 2021 - this.age;
    }
};

val = person;
console.log(val)
val = person.firstName;
console.log(val)
val = person.lastName;
console.log(val)
val = person['firstName'];
console.log(val)
val = person.age;
console.log(val)
val = person.hobbies;
console.log(val)
val = person.hobbies[1];
console.log(val)
val = person.hobbies.length;
console.log(val)
val = person.address;
console.log(val)
val = person.address.city;
console.log(val)
val = person.address['city'];
console.log(val)
val = person.getBirthYear();
console.log(val)


let people = [
    { firstName: 'Alis', lastName: 'Space' },
    { firstName: 'Denis', lastName: 'Space' },
    { firstName: 'Kaptan', lastName: 'Spock' }
];

val = people[2];
console.log(val);
val = people[2].firstName;
console.log(val);

for (let i = 0; i < people.length; i++) {
    console.log(people[i].firstName);
}
console.log(val);
console.log(typeof people)