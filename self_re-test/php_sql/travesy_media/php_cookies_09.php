<?php 
//this is to set 
setcookie('name', 'Brad', time() + 86400 * 30);

if(isset($_COOKIE['name'])) {
    echo $_COOKIE['name'];
}

//this is to unset
setcookie('name', '', time() - 86400);
?>