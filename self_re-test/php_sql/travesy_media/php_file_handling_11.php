<?php 
$file = 'extras/users.txt';

if(file_exists($file)) {
    //non flexible way of reading the file
    echo readfile($file);
    //flexible way of reading files
    $handle = fopen($file, 'r');
    $contents = fread($handle, filesize($file));
    fclose($handle);
    echo $contents;
} else {
    $handle = fopen($file, 'w');
    $contents = 'Brad' . PHP_EOL . 'Sara' . PHP_EOL . 'Mike';
    fwrite($handle, $contents);
    fclose($handle);
    //PHP_EOL as a sort of line breaker
}
?>