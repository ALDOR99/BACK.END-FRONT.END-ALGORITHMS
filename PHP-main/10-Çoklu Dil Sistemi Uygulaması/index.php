<?php
session_start();

if(empty($_SESSION["SiteDili"])){
    include("diltr.php");
}else{
    if($_SESSION["SiteDili"]=="Turkish"){
        include("diltr.php");
    }   else{
        include("dilen.php");
    } 
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

<table width ="1000" align="center" border="0">

    <tr height="40">
        <td width="130"><?php echo ANASAYFA; ?></td>    
        <td width="155"><?php echo HAKKIMIZDA; ?></td>    
        <td width="130"><?php echo ILETİSİM; ?></td>    
        <td width="373"><?php echo URUNLER; ?></td>       
        <td width="190"><a href="secim.php?DilSecimi=Turkish" style="color: #000000; text-decoration:none;">TR</a> | <a href="secim.php?DilSecimi=English" style="color: #000000; text-decoration:none;">EN</a></td>   
    <tr>

</table>


</body>
</html>