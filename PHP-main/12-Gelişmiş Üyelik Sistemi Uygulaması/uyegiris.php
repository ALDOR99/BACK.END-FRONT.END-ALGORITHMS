<?php 
require_once("baglan.php");


if (isset($_POST["kullaniciadi"])) {
    $GelenKullaniciAdi = Filtre($_POST["kullaniciadi"]);

}else{
    $GelenKullaniciAdi = "";
}

if (isset($_POST["sifre"])) {
    $GelenSifre = Filtre($_POST["sifre"]);

}else{
    $GelenSifre  = "";
}

$KontrolSorgu = $veriTabaniBaglantisi->prepare("SELECT  * FROM uyeler WHERE kullaniciadi = ? AND sifre=?");
$KontrolSorgu->execute([$GelenKullaniciAdi,$GelenSifre]);
$KontrolSayisi = $KontrolSorgu->rowCount();

if ($KontrolSayisi>0) {
    $_SESSION["Kullanici"] = $GelenKullaniciAdi;
    header("Location:index.php");
    exit();
}else{
    echo "Hata<br>";
    echo "girilen Bilgiler ile eşleşen kullanici kaydi bulunmamaktadir<br>";
    echo "Ana Sayfaya Donmek Icin Lutfen Buraya <a href = 'index.php'> Tıklayınız </a>";

}





?>