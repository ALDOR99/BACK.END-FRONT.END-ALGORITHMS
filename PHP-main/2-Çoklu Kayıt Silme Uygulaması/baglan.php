<?php
try{
    $veriTabaniBaglanti = new PDO("mysql:host=localhost;dbname=alisegitim;charset=UTF8","root","");
}catch(PDOException $hata){
    echo "baglantı hatasi<br>".$hata->getMessage();
    die();
}

function Filtrele($deger){
    $bir = trim($deger);
    $iki = strip_tags($bir);
    $uc = htmlspecialchars($iki ,ENT_QUOTES);
    $sonuc = $uc;
    return $sonuc;
}

?>