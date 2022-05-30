// Demo : Functions

// var bakiye = 2000;
// var adsoyad = "alis durna";

var hesapA = {
    ad: "alis durna",
    hesapNo: "123456",
    bakiye: 99999999999,
    ekHesap: 99999999999999
}

var hesapB = {
    ad: "miray durna",
    hesapNo: "1234567",
    bakiye: 99999999999,
    ekHesap: 99999999999999
}

function paraCek(hesap, miktar) {
    console.log(`Merhaba ${hesap.ad}`);

    if (hesap.bakiye >= miktar) {
        hesap.bakiye = hesap.bakiye - miktar;
        console.log(`paranızı alabilirsiniz Kalan paranız : ${hesap.bakiye}`);

    } else {
        var toplam = hesap.bakiye + hesap.ekHesap;

        if (toplam >= miktar) {
            if (confirm('ek hesabınızı kullanmak istermisiniz')) {
                console.log('paranızı alabilirsiniz');
                var bakiye = hesap.bakiye;
                var ekhesap = miktar - bakiye;
                hesap.bakiye = 0;
                hesap.ekhesap = hesap.ekhesap - ekhesap;
            } else {
                console.log(`${hesap.hesapNo} nolu hesabınızda ${miktar} TL bulunmamaktadır.`);
            }
        } else {
            console.log('üzgünüz bakiye yetersiz');
        }
    }

}
paraCek(hesapA, 2000)
console.log(paraCek(hesapA, 2000))
    // console.log(paraCek(hesapA))