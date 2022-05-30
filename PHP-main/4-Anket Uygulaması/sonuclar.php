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
    <?php
    $anketSorgu = $veriTabaniBaglantisi->prepare("SELECT * FROM anket LIMIT 1");
    $anketSorgu->execute();
    $kayitSayisi = $anketSorgu->rowCount();
    $kayit = $anketSorgu->fetch(PDO::FETCH_ASSOC);

    $AnketinBirinciSikkiIcinOySayisi    = $kayit["oysayisibir"];
    $AnketinIkinciSikkiIcinOySayisi     = $kayit["oysayisiiki"];
    $AnketinUcuncuSikkiIcinOySayisi     = $kayit["oysayisiuc"];
    $AnketinToplamOySayisi              = $kayit["toplamoysayisi"];

    $BirinciSecenekIcinYuzdeHesaplama   =   ($AnketinBirinciSikkiIcinOySayisi /$AnketinToplamOySayisi)*100;
    $BirinciSecenekYuzde         =   number_format($BirinciSecenekIcinYuzdeHesaplama, 2 , "," , "");

    $IkinciSecenekIcinYuzdeHesaplama   =   ($AnketinIkinciSikkiIcinOySayisi /$AnketinToplamOySayisi)*100;
    $IkinciSecenekYuzde         =   number_format($IkinciSecenekIcinYuzdeHesaplama, 2 , "," , "");

    $UcuncuSecenekIcinYuzdeHesaplama   =   ($AnketinUcuncuSikkiIcinOySayisi /$AnketinToplamOySayisi)*100;
    $UcuncuSecenekYuzde         =   number_format($UcuncuSecenekIcinYuzdeHesaplama, 2 , "," , "");



    
    if($kayitSayisi>0){
    ?>
    <table width="300" align="center" border="0" cellpadding="0" cellspacing="0">
        <tr height="30">
            <td colspan="2"><?php echo $kayit["soru"];?></td>
        </tr>
        <tr height="30">
            <td width="75">%<?php echo $BirinciSecenekYuzde;?></td>
            <td width="225"><?php echo $kayit["cevapbir"];?></td>
        </tr>
        <tr height="30">
            <td width="75">%<?php echo $IkinciSecenekYuzde;?></td>
            <td width="225"><?php echo $kayit["cevapiki"];?></td>
        </tr>
        <tr height="30">
            <td width="75">%<?php echo $UcuncuSecenekYuzde;?></td>
            <td width="225"><?php echo $kayit["cevapuc"];?></td>
        </tr>

        <tr height="30">
            <td colspan="2" align="right"><a href="index.php" style="color:blue; text-decoration:none">Ana sayfaya Don/a></td>
        </tr>
    </table>
    <?php
    }else{
        header("Location:index.php");
        exit();
    }
    ?>
</body>
</html>
<?php
$veriTabaniBaglantisi = null;

?>