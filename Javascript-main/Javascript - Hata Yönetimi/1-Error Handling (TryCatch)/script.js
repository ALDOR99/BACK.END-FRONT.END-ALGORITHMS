// Reference Error
// Type Error
// Syntax Error
// URI Error

// Error

var user = {
    name: "Alis Durna"
}
try {
    //console.log(myFunction());
    console.log(user.name);

    if (!user.email) {
        throw new Error("User has no email");
    }
} catch (e) {
    console.log(e);
    console.log(e.message);
    console.log(e.name);
    console.log(e instanceof ReferenceError);
    console.log(e instanceof TypeError);
    console.log(typeof e);
} finally {
    console.log("finally block");
}