<?php 
$fruits = ['apple', 'orange', 'pear'];

echo count($fruits);

// to search an array 
var_dump(in_array('apple', $fruits));

//to add to an array
$fruits[] = 'grape';
array_push($fruits, 'blueberry', 'straberry');
array_unshift($fruits, 'mango');

// to remove from an array
array_pop($fruits);
array_shift($fruits);
// unset($fruits[2]);

//split into 2 chunks 
$chunked_array = array_chunk($fruits, 2);

print_r($fruits);

// spread operator and printing array items 

$arr1 = [1,2,3];
$arr2 = [4,5,6];

$arr3 = array_merge($arr1, $arr2);
$arr4 = [...$arr1, ...$arr2];

print_r($arr4);

$a = ['green', 'red', 'yellow'];
$b = ['avacado', 'apple', 'banana'];

$c = array_combine($a, $b);

$keys = array_keys($c);
print_r($keys);

$flipped = array_flip($c);
print_r($flipped);

$numbers = range(1, 20);
print_r($numbers);

$newNumbers = array_map(function($number) {
    return "Number $number";
}, $numbers);
print_r($newNumbers);

$lessThan10 = array_filter($numbers, fn($number) => $number <=10);
print_r($lessThan10);

$sum = array_reduce($numbers, fn($carry, $number) => 
$carry + $number);

var_dump($sum);