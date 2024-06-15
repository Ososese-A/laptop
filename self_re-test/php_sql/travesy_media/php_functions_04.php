<?php 
$y = 12;

// function me ($name) {
//     echo "Me is " . $name;
// }

// me("sese");

// function r() {
//     //to use a global variable within a function
//     global $y;
//     $x = 10;
//     echo "$x and $y";
// }

// r();

// function registerUser($email) {
//     echo $email . ' registered';
// }

// registerUser('Brad');


// function sum($n1, $n2) {
//     return $n1 + $n2;
// }

// function sum($n1 = 4, $n2 = 5) {
//     return $n1 + $n2;
// }

// $number = sum();
// echo $number;

// $numbers = sum(6,12);
// echo $numbers;



$subtract = function($n1, $n2) {
    return $n1 - $n2;
};

echo $subtract(10, 5);

$multiply = fn($n1, $n2) => $n1 * $n2;

echo $multiply(9,9);
?>