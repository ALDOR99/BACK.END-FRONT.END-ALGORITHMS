// object literals

let a = {
        name: "alis",
        yearOfBirth: 2010,
        job: "student"
    }
    //console.log(alis);

function Person(name, yearOfBirth, job) {
    this.name = name;
    this.yearOfBirth = yearOfBirth;
    this.job = job;
    this.calculateAge = function() {
        return 2021 - this.yearOfBirth;
    }
}

let alis = new Person('alis', 2000, 'student');
console.log(alis.name);
console.log(alis.job);
console.log(alis.yearOfBirth);
console.log(alis.calculateAge());
console.log("-----------------");

let deniz = new Person('deniz', 2000, 'student');
console.log(deniz.name);
console.log(deniz.job);
console.log(deniz.yearOfBirth);
console.log(deniz.calculateAge());