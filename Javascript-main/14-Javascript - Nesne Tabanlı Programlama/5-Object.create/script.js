//Object.create

let personProto = {
    calculateAge: function() {
        return 2018 - this.yearOfBirth;
    }
}

let alis = Object.create(personProto);
alis.name = "alis";
console.log(alis.name);
alis.yearOfBirth = 2000;
alis.job = "student";

console.log("================");

let emel = Object.create(personProto, {
    name: { value: "emel" },
    yearOfBirth: { value: 1989 },
    job: { value: "teacher" }
});

console.log(emel);
console.log(emel.calculateAge())