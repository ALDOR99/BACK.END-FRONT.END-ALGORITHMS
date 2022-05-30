<?php

require_once("baglan.php");



// $GelenSecimDegerleri = $_POST["secim"];
// $IDlerBirlestir      = implode(",",$GelenSecimDegerleri); 
// $IDler = Filtrele($IDlerBirlestir);

// $Sil = $veriTabaniBaglanti ->prepare("DELETE FROM kisiler WHERE id IN ($IDler)");
// $Sil->execute();

// header("Location:index.php");
// exit();

//------------------------------------------------------


$GelenSecimDegerleri  = $_POST["secim"];


foreach($GelenSecimDegerleri as $SilinecekDeger){
    $SilinecekID = Filtrele($SilinecekDeger);

    $sil = $veriTabaniBaglanti->prepare("DELETE FROM kisiler WHERE id=$SilinecekID LIMIT 1");
    $sil->execute();
}
header("Location:index.php");
exit();




?>