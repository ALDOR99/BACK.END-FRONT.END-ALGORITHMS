<?php
require_once("baglan.php");



function Filtrele($deger){

    $Bir = trim($deger);
    $Iki = strip_tags($Bir);
    $Uc  =  htmlspecialchars($Iki,ENT_QUOTES);
    $Sonuc = $Uc;
    return $Sonuc;
}
$GelenId     =   Filtrele($_GET["id"]);

?>
<!doctype html>
<html lang="tr-TR">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="Content-Language" content="tr">
<meta charset="utf-8">
<title>Alis Egitim</title> 
</head>
<body>

    <?php 


    function AcilirListeIcinMenuYaz($GuncellenecekMenuID,$GuncellenecekMenuUstID ,$MenuUstIdDegeri=0 ,$BoslukDegeri = 0){
        global $veriTabaniBaglantisi;

        $MenuSorgu = $veriTabaniBaglantisi->prepare("SELECT * FROM menuler WHERE Ustid = ?");
        $MenuSorgu->execute([$MenuUstIdDegeri]);
        $MenuSorgusuSayi = $MenuSorgu->rowCount();
        $MenuSorgusuKayitlari = $MenuSorgu->fetchAll(PDO::FETCH_ASSOC);

        if($MenuSorgusuSayi>0){
            foreach($MenuSorgusuKayitlari as $kayitlar){
                $MenuId     =   $kayitlar["id"];
                $MenuUstId  =   $kayitlar["Ustid"];
                $MenuMenuAdi=   $kayitlar["menuadi"];

                if ($GuncellenecekMenuID != $MenuId) {
                    if ($GuncellenecekMenuUstID==$MenuId) {
                        echo "<option value='".$MenuId."' selected='selected'>" . str_repeat("&nbsp;",$BoslukDegeri) . $MenuMenuAdi . "</option>";
    
                    }else{
                        echo "<option value='".$MenuId."'>" . str_repeat("&nbsp;",$BoslukDegeri) . $MenuMenuAdi . "</option>";
                        AcilirListeIcinMenuYaz($GuncellenecekMenuID, $GuncellenecekMenuUstID, $MenuId, $BoslukDegeri+5);
                    }
                }

            }
        }
    }

    $Sorgu = $veriTabaniBaglantisi->prepare("SELECT * FROM menuler WHERE id = ? LIMIT 1");
    $Sorgu->execute([$GelenId]);
    $SorgusuSayi = $Sorgu->rowCount();
    $SorgusuKaydi = $Sorgu->fetch(PDO::FETCH_ASSOC);
    ?> 

    Menü Günceleme Formu<br>
    
    <form action="guncellesonuc.php?id=<?php echo $SorgusuKaydi["id"]; ?>" method="POST">
        Üst Menü:<select name="UstMenuSecimi">
            <option value="0" <?php if ($SorgusuKaydi["Ustid"]==0) {?> selected="selected" <?php } ?>>Ana Menü Yap</option>
            <?php AcilirListeIcinMenuYaz($SorgusuKaydi["id"],$SorgusuKaydi["Ustid"]);?>
    </select><br>
    Menu Adi: <input type="text" name="MenuAdi" value="<?php echo $SorgusuKaydi["menuadi"]; ?>"><br>
        <input type="submit" value="Menü Guncelle">
    </form><br><br><br>

    <?php

    $veriTabaniBaglantisi = null;
    ?>
</body>
</html>
