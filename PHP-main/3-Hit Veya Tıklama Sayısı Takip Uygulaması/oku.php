<?php 
require_once("baglan.php");
$GelenID = Filtre($_GET["id"]);

$HitGuncele = $veriTabaniBaglanti->prepare("UPDATE makalaler SET gosterimsayisi=gosterimsayisi+1 WHERE id = ?");

$HitGuncele->execute([$GelenID]);

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
    <table width="1000" border="0" cellpadding="0" cellspacing="0" align="center">
        
        <tr height = "30">
            <td align="left"><b>Goruntuleme ve Hit Uygulamasi</b></td>
            <td align="rigth"><a href="index.php" style="text-decoration: none; color:black">Anasayfa</a></td>
        </tr>

    <?php
        $sorgu = $veriTabaniBaglanti->prepare("SELECT * FROM makalaler WHERE id = ?");
        $sorgu->execute([$GelenID]);
        $kayitSayisi = $sorgu->rowCount();
        $kayitlar = $sorgu->fetch(PDO::FETCH_ASSOC);
        if($kayitSayisi>0){
    ?>
        <tr height = "30">
            <td colspan="2" align="left"><h3> <?php echo $kayitlar["makalebasligi"]?> </h3></td>
        </tr>
        <tr height = "30">
            <td colspan="2" align="left"><h4> <?php echo $kayitlar["makaleicerigi"]?> </h4></td>
        </tr>
        <tr height = "30">
            <td colspan="2" align="center">Bu makale <?php echo $kayitlar["gosterimsayisi"]?> defa görüntülendi</td>
        </tr>
    <?php
        }else{
            header("Location:index.php");
        }
    ?>
    </table>
</body>
</html>

<?php
$veriTabaniBaglanti = null;
?>
