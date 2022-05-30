<?php 
require_once("baglan.php")
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
    <br><br>    <br><br>     <br><br>



    <form action="aramasonuc.php" method="POST">
        <table width="500" border="0" cellpadding="0" cellspacing="0" align="center">
            <tr>
                <td><input type="text" name="Kelime" style="width: 100%; height:30px; padding:0 20px; margin-bottom:20px;"></td>
            </tr>
            
            <tr>
                <td align="center"><input type="submit" value="Arama" style="padding:0 100px; height:30px;"></td>
            </tr>
            <tr>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td align="left">
                    <?php 
                    $GelenKelime    =   Filtre($_POST["Kelime"]);
                    $sorgu = $veriTabaniBaglanti->prepare("SELECT * FROM esyalar WHERE adi LIKE '%$GelenKelime%'");
                    $sorgu->execute();
                    $KayitSayisi     =  $sorgu->rowCount();
                    $Kayit     =  $sorgu->fetchAll(PDO::FETCH_ASSOC);

                    echo "Bulunan  Kayitlar<br>";

                    foreach($Kayit as $kayitlar){
                        echo $kayitlar["adi"]."<br>";
                    }
                    ?>
                </td>
            </tr>

        </table>
    </form>
   
   
</body>
</html>




