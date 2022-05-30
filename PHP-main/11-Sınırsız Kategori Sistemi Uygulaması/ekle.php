
<?php
    require_once("baglan.php");    

function Filtrele($deger){

    $Bir = trim($deger);
    $Iki = strip_tags($Bir);
    $Uc  =  htmlspecialchars($Iki,ENT_QUOTES);
    $Sonuc = $Uc;
    return $Sonuc;
}

$GelenUstMenuSecimi     =   Filtrele($_POST["UstMenuSecimi"]);
$GelenMenuAdi           =  Filtrele($_POST["MenuAdi"]);

if (isset($GelenUstMenuSecimi) and isset($GelenMenuAdi)) {

    $Ekle = $veriTabaniBaglantisi->prepare("INSERT INTO menuler (Ustid,menuadi) values (?,?)");
    $Ekle->execute([$GelenUstMenuSecimi,$GelenMenuAdi]);
    $EkleKontrolSayisi = $Ekle->rowCount();
    
    if ($EkleKontrolSayisi>0) {

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
    echo "Ana Sayfa Geri Donmek İcin Lutfen Buraya <a href='index.php'>Tıklayınız</a>.";

}
    $veriTabaniBaglantisi = null;
    ?>
