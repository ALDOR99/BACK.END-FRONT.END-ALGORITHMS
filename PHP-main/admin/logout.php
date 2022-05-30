<?php 

session_start();              
unset($_SESSION['admins']);      //session silme
header("Location:login.php");   //silinme isleminden sonra login'e yönlendirdim
exit;                           //kapatiyorum

?>