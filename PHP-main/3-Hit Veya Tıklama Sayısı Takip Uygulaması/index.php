<?php require_once("baglan.php");?>

<!doctype html>
<html lang="tr-TR">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="Content-Language" content="tr">
<meta charset="utf-8">
<title>Alis Egitim</title> 
</head>
<body>
    <table width="1000" border="0" cellpadding="0" cellspacing="0" align="center">
        
        <tr height = "30">
            <td align="left"><b>Goruntuleme ve Hit Uygulamasi</b></td>
            <td align="rigth"><a href="index.php" style="text-decoration: none; color:black">Anasayfa</a></td>
        </tr>

        <tr height="30">
            <td colspan="2"></td>
        </tr>
    
        <tr height="30" bgcolor="#990000">    
            <td align="left" style="color: white;">Makale Başlığı</td>
            <td align="right" style="color: white;">Gosterim Sayisi&nbsp;</td>    
        </tr>


        <?php
        
        $sorgu = $veriTabaniBaglanti->prepare("SELECT * FROM makalaler");
        $sorgu->execute();
        $kayitSayisi = $sorgu->rowCount();
        $kayitlar = $sorgu->fetchAll(PDO::FETCH_ASSOC);
        if($kayitSayisi>0){
            foreach($kayitlar as $Satirlar){
        ?>

        <tr height="30">    
            <td align="left"><a href="oku.php?id=<?php echo $Satirlar["id"];?>" style="color: black; text-decoration:none;">&nbsp;<?php echo $Satirlar["makalebasligi"];?></a></td>
            <td align="right"><?php echo $Satirlar["gosterimsayisi"];?>&nbsp;</td>    
        </tr>

        <?php
            }
        }
        ?>

    </table>
</body>
</html>

<?php
$veriTabaniBaglanti = null;
?>
