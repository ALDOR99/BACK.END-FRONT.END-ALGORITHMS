<?php


try{
    $veriTabaniBaglanti = new PDO("mysql:host=localhost;dbname=test3;charset=UTF8","root","");
}catch(PDOException $hata){
    echo "veri Tabani baglanti hatasi";
    echo "hata aciklamasi: ".$hata->getMessage();
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

    <?php

    $reklamSorgusu  = $veriTabaniBaglanti->prepare("SELECT * FROM bannerlar ORDER BY gosterimsayisi ASC LIMIT 1");
    $reklamSorgusu->execute();
    $reklamSayisi   = $reklamSorgusu->rowCount();
    $reklamKaydi    = $reklamSorgusu->fetch(PDO::FETCH_ASSOC);


    ?>


    <table width="1000" align="center" border="0" cellpadding="0" cellspacing="0">
        <tr height="400">
            <td><img src="dosyalar/<?php echo $reklamKaydi["bannerdosyasi"]; ?>" border = "0"></td>
        </tr>

    </table>
</body>
</html>
<?php

$reklamGuncele  =   $veriTabaniBaglanti->prepare("UPDATE bannerlar SET gosterimsayisi = gosterimsayisi+1 WHERE id=? LIMIT 1");
$reklamGuncele->execute([$reklamKaydi["id"]]);
$veriTabaniBaglanti = null;

?> 