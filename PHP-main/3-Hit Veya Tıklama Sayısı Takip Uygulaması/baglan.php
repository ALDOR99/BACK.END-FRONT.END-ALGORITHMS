<?php

try{

    $veriTabaniBaglanti = new PDO("mysql:host=localhost;dbname=test;charset=UTF8;","root","");

}catch(PDOException $hata){
    
    echo "hata: ".$hata->getMessage();
    die();

}
function Filtre($deger){
    $Bir = trim($deger);
    $Iki = strip_tags($Bir);
    $Uc = htmlspecialchars($Iki,ENT_QUOTES);
    $Sonuc = $Uc;
    return $Sonuc;
}



?>