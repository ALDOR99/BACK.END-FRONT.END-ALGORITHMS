<?php 
    try {
        $veriTabaniBaglantisi = new PDO("mysql:host=localhost;dbname=test8;charset=UTF8","root","");
    } catch (PDOException $hata) {
        echo "veri tabani baglanti hatasi: ".$hata->getMessage();
        die();
    }
?>
