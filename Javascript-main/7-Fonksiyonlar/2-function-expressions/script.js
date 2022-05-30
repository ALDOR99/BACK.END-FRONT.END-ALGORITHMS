// Function Declarations

function sum(a, b) {
    var c = a + b;
    return c;
}

console.log(sum(10, 20));

// Function Expressions

const sum1 = function(a, b) {

    if (typeof a === 'undefined') { a = 0; }
    if (typeof b === 'undefined') { b = 0; }

    var c = a + b;
    return c;
}

document.writeln(sum1(10, 10));
console.log(sum1(15, 40));

// ES6 Default Parameters

const sum3 = function(a = 0, b = 0) {
    var c = a + b;
    return c;
}
document.writeln(sum3(100, 10));
document.writeln(sum3(10, 10));
console.log(sum3(115, 40));

function sunAll() {
    var total = 0;
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}

console.log(sunAll(10, 10, 10, 40));