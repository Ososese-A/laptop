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
    // $name = htmlspecialchars($_POST['name']);
    // $age = htmlspecialchars($_POST['age']);

    // $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_SPECIAL_CHARS);
    $name = filter_var($_POST['name'], FILTER_SANITIZE_SPECIAL_CHARS);
    $age = htmlspecialchars($_POST['age']);
    echo $name;
    echo $age;
}
?>