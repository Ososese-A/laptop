<?php 
session_start();

session_destroy();
header('Location: /php_session_10.php');
?>