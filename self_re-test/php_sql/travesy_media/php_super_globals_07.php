<?php 

// var_dump($_SERVER);
?>
<body>
    <ul>
        <li>Host: <?php echo $_SERVER['HTTP_HOST']; ?></li>
        <li>Document Root: <?php echo $_SERVER['DOCUMENT_ROOT']; ?></li>
        <li>Server Name: <?php echo $_SERVER['SERVER_NAME']; ?></li>
        <li>Server Port: <?php echo $_SERVER['SERVER_PORT']; ?></li>
        <li>Current file dir: <?php echo $_SERVER['PHP_SELF']; ?></li>
        <li>Request URI: <?php echo $_SERVER['REQUEST_URI']; ?></li>
        <li>Server Software: <?php echo $_SERVER['SERVER_SOFTWARE']; ?></li>
        <li>Client Info: <?php echo $_SERVER['HTTP_USER_AGENT']; ?></li>
        <li>Remote Address: <?php echo $_SERVER['REMOTE_ADDR']; ?></li>
        <li>Remote Port: <?php echo $_SERVER['REMOTE_PORT']; ?></li>
    </ul>
</body>



<a href="<?php echo $_SERVER['PHP_SELF']; ?>?name=john&age=30">MEME</a>

<!-- <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="GET"> -->
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
<div>
    <label for="name">Name: </label>
    <input type="text" name="name" id="name">
</div>
<div>
    <label for="age">Age: </label>
    <input type="text" name="age" id="age">
</div>
<input type="submit" value="Submit" name="submit">
</form>

<?php 
//for GET
// echo $_GET['name'];
// echo $_GET['age'];

if(isset($_POST['submit'])) {
    echo $_POST['name'];
    echo $_POST['age'];
}
?>