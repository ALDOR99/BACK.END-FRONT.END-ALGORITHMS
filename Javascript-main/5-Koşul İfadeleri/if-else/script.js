// if/else statements

const firstName = "alis";
const age = 21;

const isStudent = false;
const school = "university";

if (firstName === "alis") {
    console.log("hello alis");
}

if (age === 21) {
    console.log("your age is 21");
}

if (isStudent) {
    console.log("hello student");
} else {
    console.log("How are things going");
}

if (age >= 18) {
    if ((school == "university") || (school == "high school")) {
        console.log("You can get a driver's license")
    }
} else {
    console.log("You cannot receive a driver's license")
}


if (age > 0 && age < 25) {
    console.log(`${firstName} is an adult`);
}


//undefined

if (typeof id !== "undefined") {
    console.log("id: " + id);
} else {
    console.log("no id");
}