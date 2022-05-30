
<?php 
header("Content-Type: text/xmlns");
try {
    $veriTabaniBaglantisi = new PDO("mysql:host=localhost;dbname=test7;charset=UTF8","root","");

} catch (PDOException $hata) {
    echo "veri tabani baglanti hatasi :".$hata->getMessage();
    die();
}

echo "<?xml version='1.0' encoding='UTF8'?>
<rss xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' version='2.0'>
    <channel>
        <title>Alis Egitim</title>
        <description> Ileri Seviye Egitim Setleri</description>
        <link>https://www.youtube.com/watch?v=bq4LPGDs4MY</link>
        <language>tr</language>";


        $Sorgu = $veriTabaniBaglantisi->prepare("SELECT * FROM urunler");
        $Sorgu->execute();
        $SorguSayisi = $Sorgu->rowCount();
        $Sorgukayitlari = $Sorgu->fetchAll(PDO::FETCH_ASSOC);


        if($SorguSayisi>0){
            foreach($Sorgukayitlari as $Satirlar){

                $UrunAdi      = $Satirlar["urunadi"];
                $UrunFiyat    = $Satirlar["urunfiyat"];

                echo "<item>
                <title>$UrunAdi</title>
                <price>$UrunFiyat</price>
                </item>";
            }
        }
echo "
    </channel>
</rss>
";


$veriTabaniBaglantisi = null;
?>
