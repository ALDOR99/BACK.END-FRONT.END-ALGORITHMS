<?php
try {
    $veriTabaniBaglantisi = new PDO("mysql:host=localhost;dbname=test5;charset=UTF8","root","");
}catch(PDOException $hata){
    echo "veri tabani baglanti hatasi<br>";
    echo "baglanti hatasi: ".$hata->getMessage();
    die();
}
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
    <table width = "1000" align="center" border="0" cellpadding="0" cellspacing="0">
        <tr height="30" bgcolor="#00000">

            <td align="left" style="color:white">
                &nbsp;Urun Adi
            </td>

            <td align="right"style="color:white">
                Urun Fiyati&nbsp;
            </td>

        </tr>


        <?php
            $sorgu = $veriTabaniBaglantisi->prepare("SELECT * FROM urunler");
            $sorgu->execute();
            $sorguSayisi    = $sorgu->rowCount();    
            $sorguKayitlari = $sorgu->fetchAll(PDO::FETCH_ASSOC); 

            $BirinciRenk = "#dfdfdf";
            $IkinciRenk  = "#FFFFFF";
            $RenkIcinSayi = "0";


            foreach($sorguKayitlari as $satirlar){
                if($RenkIcinSayi % 2){
                    $ArkaPlanRengi = $BirinciRenk;
                }else{
                    $ArkaPlanRengi = $IkinciRenk;

                }

                ?>

        <tr height="30" bgcolor="<?php echo $ArkaPlanRengi;?>" onmouseover="this.bgColor='#c2cedb'" onmouseout="this.bgColor='<?php echo $ArkaPlanRengi;?>';" style="cursor:pointer;">
            <td align="left">&nbsp;<?php echo $satirlar["urunadi"];?></td>

            <td align="right">&nbsp;<?php echo $satirlar["urunfiyat"];?></td>
        </tr>
        <?php
            $RenkIcinSayi ++;

            }
        ?>

    </table>
</body>
</html>
<?php
    $veriTabaniBaglantisi = null;
?>