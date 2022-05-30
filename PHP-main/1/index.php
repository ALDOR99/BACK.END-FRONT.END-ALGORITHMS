<!doctype html>
<html lang="tr-TR">


<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="Content-Language" content="tr">
<meta charset="utf-8">
<title>Alis Egitim</title>


<style>


    .InputAlani{

        width: 100%;
        height: 15;
        margin: 0;
        padding: 5px 10px 5px 10px;

    }

    .TextareaAlani{
        width: 100%;
        height: 50px;
        margin: 0;
        padding: 5px 10px 5px 10px;
}
    .GonderButtonu{
        height: 30px;
        margin: 0;
        padding: 5px 50px 5px 50px;
        border: 1px solid #00FF00;
        background: #009900;
        color: #FFFFFF;
    }
    .GonderButtonu:hover{
        
        border: 1px solid #000000;
        background: #00FF00;
        color: #000000;
        cursor: pointer;
    }

</style>

</head>
<body>

    <form action="sonuc.php" method="post">
        <table width="500" border="0" align="center" cellpadding="0" cellspacing="0">

            <tr>
                <td width="150">Adınız Soyadınız</td>
                <td width="20">:</td>
                <td width="330"><input type="text" name="adisoyadi" class="InputAlani"></td>
            </tr>

            <tr>
                <td width="150">Telefon Numaraniz</td>
                <td width="20">:</td>
                <td width="330"><input type="text" name="telefon" class="InputAlani"></td>
            </tr>

            <tr>
                <td width="150">E-Mail Adresiniz</td>
                <td width="20">:</td>
                <td width="330"><input type="email" name="emailadresi" class="InputAlani"></td>
            </tr>

            <tr>
                <td width="150">Konu</td>
                <td width="20">:</td>
                <td width="330"><input type="text" name="konusu" class="InputAlani"></td>
            </tr>
            <tr>
                <td width="150" valing="top">Mesaj</td>
                <td width="20"  valing="top">:</td>
                <td width="330"><textarea name="mesaji" class="TextareaAlani"></textarea></td>
            </tr> 
            <tr>
                <td width="150" height="30">&nbsp;</td>
                <td width="20" height="30">&nbsp;</td>
                <td width="330"><input type="submit" value="Gonder" class="GonderButtonu"></td>
            </tr> 

        </table>



</body>
</html>