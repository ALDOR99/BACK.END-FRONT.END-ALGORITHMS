// Call,Apply & Bind


var welcome = function(a, b) {
    console.log('Welcome ' + this.name + '.Are you interested in ' + a + ' and ' + b);
}
var yigit = { name: "Yigit" };
var ada = { name: "Ada" };

welcome.call(yigit, 'asp.net', 'angular');
welcome.call(ada, 'asp.net', 'angular');
console.log("==================================")

welcome.apply(yigit, ['asp.net', 'angular']);
welcome.apply(ada, ['asp.net', 'angular']);
console.log("==================================")

var welcomeYigit = welcome.bind(yigit);
welcomeYigit('asp.net', 'ada');
console.log("==================================")

var welcomeAda = welcome.bind(ada);
welcomeAda('asp.net', 'angular');