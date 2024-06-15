<?php 
//headers can be sued so that we don't hvae to use the session start every time
session_start();

if(isset($_SESSION['username'])) {
    echo '<h1> Welcome ' . $_SESSION['username'] . '</h1>';
    echo '<a href="logout.php">Logout</a>';
} else {
    echo '<h1> Welcome Guest </h1>';
    echo '<a href="/php_session_10.php">Home</a>';
}

?>