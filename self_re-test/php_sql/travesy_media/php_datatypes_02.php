<?php
    $name ="Brad";
    $age = 40;
    $has_kids = false;
    $cash_on_hand = 20.75;

    echo $name;
    echo $age;
    echo $has_kids;
    echo $cash_on_hand;
    //concatenation
    echo $name . " is " . $age . " years old";
    
    //constants
    define("Host", "abc");
    define("DB_Name", "dev_db");

    echo Host;
    echo DB_Name;

    //arrays 
    $numbers = [1, 44, 55, 22];
    $nos = [1, 'meme', 55, 22];
    $fruits = array('apple', 'orange', 'pear');

    echo $fruits[0];

    //associative array 
    $color = [
        1 => 'green',
        2 => 'red'
    ];

    echo $color[1];

    $people = [
        [
            'first_name' => 'Brad',
            'last_name' => 'Wewe'
        ],
        [
            'first' => 'Brad',
            'last' => 'Wewe'
        ]
        ];

var_dump(json_encode($people));
?>