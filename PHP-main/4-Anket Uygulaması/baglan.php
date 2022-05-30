<?php


try{
    $veriTabaniBaglantisi = new PDO("mysql:host=localhost;dbname=test1;charset=UTF8","root","");
}catch(PDOException $hata){
    echo "veri tabani baglanti hatasi";
    echo "hata acıklaması".$hata->getMessage();
    die();
}

$IPAdresi = $_SERVER["REMOTE_ADDR"];
$ZamanDamgasi = time();
$OyKullanmaSiniri = 86400;//saniye cınsınden
$ZamanGeriAl = $ZamanDamgasi-$OyKullanmaSiniri;

function Filtrele($deger){
    $bir = trim($deger);
    $iki = strip_tags($bir);
    $uc =  htmlspecialchars($iki, ENT_QUOTES);
    $sonuc = $uc;
    return $sonuc;
}




?>