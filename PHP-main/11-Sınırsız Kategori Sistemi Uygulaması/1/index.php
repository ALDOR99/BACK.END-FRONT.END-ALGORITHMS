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
    try {
        $veriTabaniBaglantisi = new PDO("mysql:host=localhost;dbname=test8;charset=UTF8","root","");
    } catch (PDOException $hata) {
        echo "veri tabani baglanti hatasi: ".$hata->getMessage();
        die();
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
                
                echo str_repeat("&nbsp;",$BoslukDegeri);
                echo $MenuId ." | " . $MenuUstId . " | ". $MenuMenuAdi . "<br>";
                MenuYaz($MenuId,$BoslukDegeri+10);
            }
        }
    }
    MenuYaz();

    $veriTabaniBaglantisi = null;
    ?>
</body>
</html>
