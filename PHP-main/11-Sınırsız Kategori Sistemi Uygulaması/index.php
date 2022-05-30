<?php
require_once("baglan.php");
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


    function AcilirListeIcinMenuYaz($MenuUstIdDegeri=0 ,$BoslukDegeri = 0){
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

                echo "<option value='".$MenuId."'>" . str_repeat("&nbsp;",$BoslukDegeri) . $MenuMenuAdi . "</option>";
                AcilirListeIcinMenuYaz($MenuId,$BoslukDegeri+5);
            }
        }
    }



    function MenuYaz($MenuUstIdDegeri=0 ,$BoslukDegeri = 0){
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
                echo str_repeat("&nbsp;",$BoslukDegeri).$MenuMenuAdi ."<a href='guncelle.php?id=".$MenuId ."'>[Guncele]</a>  <a href='sil.php?id=" . $MenuId . "'>[Sil]</a> <br>";
                MenuYaz($MenuId,$BoslukDegeri+10);
            }
        }
    }

    //yeni menu ekleme
    ?> 
    Menü Ekleme Formu<br>
    
    <form action="ekle.php" method="POST">
        Üst Menü:<select name="UstMenuSecimi">
            <option value="0">Ana Menü Yap</option>
        <?php AcilirListeIcinMenuYaz();?>
    </select><br>
    Menu Adi: <input type="text" name="MenuAdi"><br>
        <input type="submit" value="Menü Ekle">
    </form><br><br><br>
    




    <?php
    //menulerı listeleme
    MenuYaz();

    $veriTabaniBaglantisi = null;
    ?>
</body>
</html>
