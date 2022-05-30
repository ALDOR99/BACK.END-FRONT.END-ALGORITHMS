<?php
require_once("baglan.php");
function Filtrele($deger){

    $Bir = trim($deger);
    $Iki = strip_tags($Bir);
    $Uc  =  htmlspecialchars($Iki,ENT_QUOTES);
    $Sonuc = $Uc;
    return $Sonuc;
}
$GelenId = Filtre($_GET["id"]);
$GelenUstMenuSecimi = Filtre($_POST["UstMenuSecimi"]);
$GelenMenuAdi = Filtre($_POST["MenuAdi"]);

if (isset($GelenId) and isset($GelenUstMenuSecimi) and isset($GelenMenuAdi)) {





    $Gunceleme = $veriTabaniBaglantisi->prepare("UPDATE menuler SET Ustid = ?,menuadi = ? WHERE id= ? LIMIT 1");
    $Gunceleme->execute([$GelenUstMenuSecimi,$GelenMenuAdi,$GelenId]);
    $GuncelemeKontrolSayisi = $Gunceleme->rowCount();
    
    if ($GuncelemeKontrolSayisi>0) {
        header("Location:index.php");
        exit();
    }else{
        echo "Hata<br>";
        echo "İşlem Sırasında Beklenmeyen Bir Sorun Olustu. Daha Sonra Tekrar Deneyiniz.<br>";
        echo "Ana Sayfa Geri Donmek İcin Lutfen Buraya <a href='index.php'>Tıklayınız</a>.";
    }
}else{
    echo "Hata<br>";
    echo "Lütfen Bos Alan Bırakmayınız<br>";
    echo "Guncelleme Sayfaasına Geri Donmek İcin Lutfen Buraya <a href='guncelle.php?id=". $GelenId ."'>Tıklayınız</a>.";
}
$veriTabaniBaglantisi = null;
?>