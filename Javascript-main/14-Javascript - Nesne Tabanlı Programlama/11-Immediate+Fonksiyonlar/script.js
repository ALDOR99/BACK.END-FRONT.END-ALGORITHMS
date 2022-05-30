// Immediate Functions

// (function(){

// })();

// (function(){

// }());


(function(name, name2) {
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var today = new Date();
    var msg = 'Welcome ' + name + ' Today is ' + days[today.getDay()];
    var msg2 = 'Welcome ' + name2 + ' Today is ' + days[today.getDay()];

    console.log(msg);
    console.log(msg2);

}("Çınar", "deniz"));