<?php

$age = 17;

if ($age >= 18) {
    echo 'You are too old';
} else {
    echo 'You are not old enough';
}

$t = date('H');

if($t < 12) {
    echo 'Good Morning';
} elseif($t < 17){
    echo 'Good Afternoon';
} else {
    echo 'Good Evening';
}

if (true) {
    echo 123;
}

$posts = ['First Post'];

if (!empty($posts)) {
    echo $posts[0];
} else {
    echo 'No Posts';
}

//ternary operation
echo !empty($posts) ? $posts[0] : 'No Posts';

//ternary operations
$firstPostA = !empty($posts) ? $posts[0] : 'No Posts';

//ternary with the coelesent operator 
$firstPostB = $posts[0] ?? null;

echo $firstPostA;
echo $firstPostB;

$favcolor = 'yellow';

switch ($favcolor) {
    case 'red':
        echo 'Your favorite color is red';
        break;
    case 'blue':
        echo 'Your favorite color is blue';
        break;
    case 'green':
        echo 'Your favorite color is green';
        break;
    default:
        echo 'Your favorite color is yellow';
}


// then loops 
for($x = 0; $x <= 10; $x++) {
    echo $x . '<br>';
}


$x = 1;
while($x <=15) {
    echo 'Number' . $x . '<br>';
    $x = $x + 1;
}


do {
    echo 'Letter Number' . $x . '<br>';
    $x++;
    echo 'Letter Number' . $x . '<br>';
} while ($x <= 5);


//the for each loop for PHP 

$posts = ['First Post', 'Second Post', 'Third Post'];

for($x = 0; $x < count($posts); $x++) {
    echo $posts[$x];
}

foreach($posts as $index => $post) {
    echo $index + 1 . '_' . $post . '<br>';
}

$person = [
    'first_name' => 'Brad',
    'last_name' => 'Travesy',
    'email' => 'brad@gmail.com'
];

foreach($person as $key => $value) {
    echo "$key - $value <br>";
    //echo '$key - $value <br>';
}
?>
