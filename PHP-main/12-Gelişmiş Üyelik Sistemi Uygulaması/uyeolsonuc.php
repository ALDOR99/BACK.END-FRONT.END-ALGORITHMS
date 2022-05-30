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

if (isset($_POST["adsoyad"])) {
    $GelenIsimSoyisim = Filtre($_POST["adsoyad"]);

}else{
    $GelenIsimSoyisim  = "";
}

if (isset($_POST["emailadresi"])) {
    $GelenEmailAdresi = Filtre($_POST["emailadresi"]);

}else{
    $GelenEmailAdresi  = "";
}
$KontrolSorgu = $veriTabaniBaglantisi->prepare("SELECT  * FROM uyeler WHERE kullaniciadi = ? OR emailadresi=?");
$KontrolSorgu->execute([$GelenKullaniciAdi,$GelenEmailAdresi]);
$KontrolSayisi = $KontrolSorgu->rowCount();

if ($KontrolSayisi>0) {
    echo "Hata<br>";
    echo "girilen Bilgiler ile eşleşen kullanici adi veya email adresi baska bir uye tarafindan  kullanilmaktadir<br>";
    echo "Ana Sayfaya Donmek Icin Lutfen Buraya <a href = 'index.php'> Tıklayınız </a>";
}else{
    $KayitEkle = $veriTabaniBaglantisi->prepare("INSERT INTO uyeler (kullaniciadi,sifre,adisoyadi,emailadresi,kayittarihi) values (?,?,?,?,?)");
    $KayitEkle->execute([$GelenKullaniciAdi,$GelenSifre,$GelenIsimSoyisim,$GelenEmailAdresi,$ZamaDamgasi]);
    $KayitKontrol = $KayitEkle->rowCount();

    if ($KayitKontrol>0) {
        echo "Tebrikler<br>";
        echo "Kullanıcı kaydi basariyla tamamlandi<br>";
        echo "Ana Sayfaya Donmek Icin Lutfen Buraya <a href = 'index.php'> Tıklayınız </a>";
    }else{
        echo "Hata<br>";
        echo "Kullanici kaydi islemi sirasinda hata olustu<br>";
        echo "Lutfen daha sonra tekrar deneyiniz<br>";
        echo "Ana Sayfaya Donmek Icin Lutfen Buraya <a href = 'index.php'> Tıklayınız </a>";
    }
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
    echo "Ana Sayfaya Donmek Icin Lutfen Buraya <a href = 'index.php'> Tıklayınız </a>.<br>";

}

?>