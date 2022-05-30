
<?php
require_once("baglan.php");    
$GelenId     =   Filtrele($_GET["id"]);

function Filtrele($deger){

    $Bir = trim($deger);
    $Iki = strip_tags($Bir);
    $Uc  =  htmlspecialchars($Iki,ENT_QUOTES);
    $Sonuc = $Uc;
    return $Sonuc;
}






$MenuHiyerarsiniBulDizisi = [$GelenId];

function MenuHiyerarsiniBul($MenuIdDegeri){
    global $veriTabaniBaglantisi;
    global $MenuHiyerarsiniBulDizisi;
    


    $MenuSorgusu = $veriTabaniBaglantisi->prepare("SELECT * FROM menuler WHERE ustid = ?");
    $MenuSorgusu->execute([$MenuIdDegeri]);
    $MenuSorguSayisi = $MenuSorgusu->rowCount();
    $MenuSorgusuKayitlari = $MenuSorgusu->fetchAll(PDO::FETCH_ASSOC);

    if ($MenuSorguSayisi>0) {
    
        foreach($MenuSorgusuKayitlari as $Kayitlar){
            $MenuId = $Kayitlar["id"];
            $MenuUstİd = $Kayitlar["Ustid"];
            $MenuMenuAdi = $Kayitlar["menuadi"];
            echo $MenuMenuAdi."<br>";
            $MenuHiyerarsiniBulDizisi[] = $MenuId;
            MenuHiyerarsiniBul($MenuId);
        }
    }
    return $MenuHiyerarsiniBulDizisi;
}




if (isset($GelenId)) {
    $SilinecekMenuler = MenuHiyerarsiniBul($GelenId);
    foreach ($SilinecekMenuler as $SilinecekId) {
        $Sil = $veriTabaniBaglantisi->prepare("DELETE FROM menuler WHERE id = ? LIMIT 1");
        $Sil->execute([$SilinecekId]);
        $SilKontrolSayisi = $Sil->rowCount();
        if ($SilKontrolSayisi<1) {
            echo "Hata<br>";
            echo "Lütfen Bos Alan Bırakmayınız<br>";
            echo "Ana Sayfa Geri Donmek İcin Lutfen Buraya <a href='index.php'>Tıklayınız</a>.";
        } else {
            echo "Hata<br>";
            echo "Ana Sayfa Geri Donmek İcin Lutfen Buraya <a href='index.php'>Tıklayınız</a>.";
        }
    }

    header("Location:index.php");
    exit();

}else{
    echo "Hata<br>";
    echo "Lütfen Bos Alan Bırakmayınız<br>";
    echo "Ana Sayfa Geri Donmek İcin Lutfen Buraya <a href='index.php'>Tıklayınız</a>.";

}
$veriTabaniBaglantisi = null;
?>
