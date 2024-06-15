<?php 
if(isset($_POST['submit'])) {
    if(!empty($_FILES['upload']['name'])) {
        $allowed_ext = array('png', 'jpg', 'gif','jpeg');
        // print_r($_FILES);
        $file_name = $_FILES['upload']['name'];
        $file_size = $_FILES['upload']['size'];
        $file_tmp_name = $_FILES['upload']['tmp_name'];
        $file_type = $_FILES['upload']['type'];
        $file_error = $_FILES['upload']['error'];
        $file_full_path = $_FILES['upload']['full_path'];
        $target_dir = "uploads/$file_name";

        //Get file ext
        //the explode function creates an array from a string
        $file_ext = explode('.', $file_name);
        $file_ext = strtolower(end($file_ext));

        //validate file ext
        if (in_array($file_ext, $allowed_ext)) {
            if($file_size <= 1000000) {
                move_uploaded_file($file_tmp_name, $target_dir);

                $message = '<p style="color: green"> File Uploaded</p>';
            } else {
                $message = '<p style="color: red"> File is too large</p>';
            }
        } else {
            $message = '<p style="color: red;">Invalid file type </p>';
        }
    } else {
        $message = '<p style="color: red;">Please choose a file</p>';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php echo $message ?? null; ?>
    <!-- you need to add this if you want to upload files of any time and work with them in PHP -->
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" enctype="multipart/form-data">
    Select image to upload:
    <input type="file" name="upload">
    <input type="submit" value="Submit" name="submit">
    </form>
</body>
</html>