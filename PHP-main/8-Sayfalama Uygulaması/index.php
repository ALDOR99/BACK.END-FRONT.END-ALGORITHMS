<?php

try {
    $veriTabaniBaglantisi = new PDO("mysql:host=localhost;dbname=test6;charset=UTF8;","root","");
} catch(PDOException $hata){
    echo "veri tabani baglanti hatasi: ".$hata->getMessage();
}

if(isset($_REQUEST["Sayfalama"])){
    $GelenSayfalama          =   $_REQUEST["Sayfalama"];
}else{
    $GelenSayfalama = 1;
}

$SayfalamaIcinSolVeSagButtonSayisi  = 3;

$SayfaBasinaGosterilecekKayitSayisi = 5;

$ToplamKayitSayisiSorgusu           =     $veriTabaniBaglantisi->prepare("SELECT * FROM urunler");
$ToplamKayitSayisiSorgusu->execute();
$ToplamKayitSayisi                  =     $ToplamKayitSayisiSorgusu->rowCount();
$SayfalamayaBaslanacakKayitSayisi   = ($GelenSayfalama*$SayfaBasinaGosterilecekKayitSayisi)-$SayfaBasinaGosterilecekKayitSayisi;

$BulunanSayfaSayisi                  = ceil($ToplamKayitSayisi/$SayfaBasinaGosterilecekKayitSayisi);

?>


<!doctype html>
<html lang="tr-TR">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="Content-Language" content="tr">
<meta charset="utf-8">
<title>Alis Egitim</title> 
<style>
    .sayfalamaAlaniKapsayicisi{
        display: block;
        width: 100%;
        height: auto;
        margin: 0;
        padding: 10px 0 10px 0;
        border: 0;
        outline: none;
        text-align: center;
        text-decoration: none;
    }
    .SayfalamaAlaniIcinMetinAlaniKapsayicisi{
        display: block;
        width: 100%;
        height: auto;
        margin: 0;
        padding: 5px 0 5px 0;
        border: 0;
        outline: none;
        text-align: center;
        text-decoration: none;

    }
    .SayfalamaAlaniIcinNumaralandirmaAlaniKapsayicisi{
        display: block;
        width: 100%;
        height: auto;
        margin: 0;
        padding: 5px 0 5px 0;
        border: 0;
        outline: none;
        text-align: center;
        text-decoration: none;

    }
    .pasif{
        display: inline-block;
        width: auto;
        height: 20px;
        margin: 0 0.5px;
        padding: 0;
        padding: 5px 7.5px;
        background: #FFFFFF;
        border: none;
        border: 1px solid #DADADA;
        outline: none;
        color: #646464;
        font-size: 14px;
        font-style: normal;
        font-variant: normal;
        font-weight: normal;
        line-height: 20px;
        text-align: center;
        text-decoration: none;
    }

    .pasif a:link,a:visited,a:hover,a:active{
        text-decoration: none;
        color: #646464;


    }

    .aktif{
        display: inline-block;
        width: auto;
        height: 20px;
        margin: 0 0.5px;
        padding: 0;
        padding: 5px 7.5px;
        background: #F6F6F6;
        border: none;
        border: 1px solid #DADADA;
        outline: none;
        color: red;
        font-size: 14px;
        font-style: normal;
        font-variant: normal;
        font-weight: bold;
        line-height: 20px;
        text-align: center;
        text-decoration: none;
    }


</style>
</head>
<body>
    <table align="center" width="500" border="0" cellpadding="0" cellspacing="0">
    <?php 

        $UrunSorgu            =    $veriTabaniBaglantisi->prepare("SELECT * FROM urunler ORDER BY id ASC LIMIT $SayfalamayaBaslanacakKayitSayisi,$SayfaBasinaGosterilecekKayitSayisi");
        $UrunSorgu->execute();
        $UrunSorguKayitSayisi = $UrunSorgu->rowCount();
        $UrunSorguKayitlari   =$UrunSorgu->fetchAll(PDO::FETCH_ASSOC);

        foreach ($UrunSorguKayitlari as $Kayitlar) {
            echo "<tr height='30'>";
            echo "<td width = '25' align='left'>" . $Kayitlar["id"] . "</td>";
            echo "<td width = '375' align='left'>" . $Kayitlar["urunadi"] . "</td>";
            echo "<td width = '100' align='right'>" . $Kayitlar["urunfiyat"] . " " . $Kayitlar["parabirimi"] . "</td>";
            echo "</tr>";
        }
    ?>

    </table>

    <div class="sayfalamaAlaniKapsayicisi">

        <div class="SayfalamaAlaniIcinMetinAlaniKapsayicisi">
            Toplam <?php echo $BulunanSayfaSayisi;?> Sayfada <?php echo $ToplamKayitSayisi;?> adet kayit bulunmaktadir
        </div>

        <div class="SayfalamaAlaniIcinNumaralandirmaAlaniKapsayicisi">
            <?php 

            if($GelenSayfalama>1){
                echo "<span class='pasif'><a href='index.php?Sayfalama=1'> << </a></span>";
                $SayfalamaIcinSayfaDegeriniBirGeriAl = $GelenSayfalama-1;
                echo "    <span class='pasif'><a href='index.php?Sayfalama=" . $SayfalamaIcinSayfaDegeriniBirGeriAl . "'> < </a></span>";
            }

            for ($SayfalamaIcınIndexDegeri =$GelenSayfalama-$SayfalamaIcinSolVeSagButtonSayisi;
                 $SayfalamaIcınIndexDegeri <=$GelenSayfalama+$SayfalamaIcinSolVeSagButtonSayisi; 
                 $SayfalamaIcınIndexDegeri ++) { 

                

                if(($SayfalamaIcınIndexDegeri>0) and ($SayfalamaIcınIndexDegeri<=$BulunanSayfaSayisi)){
                    if($GelenSayfalama==$SayfalamaIcınIndexDegeri){
                        echo " <span class='aktif'>" . $SayfalamaIcınIndexDegeri."</span>"; 

                    }else{
                        echo " <span class='pasif'><a href='index.php?Sayfalama=". $SayfalamaIcınIndexDegeri ."'>".$SayfalamaIcınIndexDegeri."</a></span>"; 
                    }   
                }
            }



            if($GelenSayfalama!=$BulunanSayfaSayisi){


                $SayfalamaIcinSayfaDegeriniBirIleriAl = $GelenSayfalama+1;
                echo "<span class='pasif'><a href='index.php?Sayfalama=" . $SayfalamaIcinSayfaDegeriniBirIleriAl . "'> > </a></span>";
                echo " <span class='pasif'><a href='index.php?Sayfalama= " . $BulunanSayfaSayisi . "'> >> </a></span>";
            }

            ?>
        </div>

    </div>

</body>
</html>
<?php 
$veriTabaniBaglantisi = null;
?>