// Functions
function yasHesapla(dogumYili) {
    return 2021 - dogumYili;
}
let ageAlis = yasHesapla(2000);
document.write(yasHesapla(2000));
console.log(ageAlis);


function EmekligeKacYilKaldi(dogumYili, isim) {
    let yas = yasHesapla(dogumYili);
    let emeklilik = 65 - yas;

    if (emeklilik > 0) {
        console.log(`${isim} emekli olmana ${emeklilik} yıl kaldı`);
    } else {
        console.log("emeklisiniz");
    }
}

EmekligeKacYilKaldi(2012, "alis");
EmekligeKacYilKaldi(2000, "alis");
EmekligeKacYilKaldi(2002, "alis");