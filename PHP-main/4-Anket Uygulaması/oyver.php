<?php
require_once("baglan.php");

$GelenCevap = Filtrele($_POST["cevap"]);
$KontrolSorgusu = $veriTabaniBaglantisi->prepare("SELECT * FROM oykullananlar WHERE ipadresi= ? AND tarih >= ?");
$KontrolSorgusu->execute([$IPAdresi,$ZamanGeriAl ]);
$KontrolSayisi = $KontrolSorgusu->rowCount();

if($KontrolSayisi>0){

    echo "HATA<br>";
    echo "Daha once oy kullanmisiniz.Lutfen en az 24 saat sonra tekrar deneyiniz<br>";
    echo "Ana sayfaya donmek icin <a href='index.php'> tiklaniyiniz</a>";
}else{

    if($GelenCevap == 1){
        $Guncelle = $veriTabaniBaglantisi->prepare("UPDATE anket SET oysayisibir = oysayisibir+1,toplamoysayisi=toplamoysayisi+1");
        $Guncelle->execute();
    }elseif($GelenCevap == 2){
        $Guncelle = $veriTabaniBaglantisi->prepare("UPDATE anket SET oysayisiiki = oysayisiiki+1,toplamoysayisi=toplamoysayisi+1");
        $Guncelle->execute();
    }elseif($GelenCevap == 3){
        $Guncelle = $veriTabaniBaglantisi->prepare("UPDATE anket SET oysayisiuc = oysayisiuc+1,toplamoysayisi=toplamoysayisi+1");
        $Guncelle->execute();
        
    }else{
        echo "HATA<br>";
        echo "Cevap Kaydi bulunamiyor<br>";
        echo "Ana sayfaya donmek icin <a href='index.php'> tiklaniyiniz</a>";
    }

    $Ekle = $veriTabaniBaglantisi->prepare("INSERT INTO oykullananlar (ipadresi,tarih) values (?,?)");
    $Ekle->execute([$IPAdresi,$ZamanDamgasi]);
    $EkleKontrol = $Ekle->rowCount();
    if($EkleKontrol>0){
        echo "tesekkurler<br>";
        echo "vermis oldugunuz oy sısteme kayıt edildi<br>";
        echo "Ana sayfaya donmek icin <a href='index.php'> tiklaniyiniz</a>";
    }else{
        echo "HATA<br>";
        echo "islem sirasinda bir hata olustu lutfen daha sonra tekrar deneyınız<br>";
        echo "Ana sayfaya donmek icin <a href='index.php'> tiklaniyiniz</a>";
    }

}
$veriTabaniBaglantisi =null;

?>