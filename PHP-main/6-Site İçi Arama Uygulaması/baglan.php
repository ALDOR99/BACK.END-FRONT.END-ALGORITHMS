<?php
try{
    $veriTabaniBaglanti = new PDO("mysql:host=localhost;dbname=test4;charset=UTF8","root","");
}catch(PDOException $hata){
    echo "veri tabani baglanti hatasi<br>";
    echo "hata aciklamasi: ".$hata->getMessage();
    die();

    
}

function Filtre($deger){

    $bir = trim($deger);
    $iki = strip_tags($bir);
    $uc =  htmlspecialchars($iki);
    $sonuc = $uc;
    return $sonuc;
}
?>