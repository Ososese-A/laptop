<?php 
class User {
    //properties are attributes that belong to a class
    //access modifiers public, private and protected
    public $name;
    public $email;
    public $password;

    function set_name ($name) {
        $this -> name = $name;
    }

    function get_name () {
        return $this -> name;
    }
}

//creating a class with a constructor 
class Player {
    public $userid;
    public $username; 

    public function __construct ($name, $uid) {
        $this->username = $name;
        $this ->userid = $uid;
    }

    function set_player_name ($name) {
        $this -> username = $name;
    }

    function get_player_name () {
        return $this-> username;
    }
}

//Instantiate a user object
$user1 = new User();
$user2 = new User();

$player1 = new Player('Player1','melony');
$player2 = new Player('player2', 'Anthrax');


// $user1 -> name = 'Brad';
$user1 -> set_name('Brad' . PHP_EOL);
$user2 -> set_name('John' . PHP_EOL);

// $player1 -> set_id('Meloney' . PHP_EOL);

echo $user1 -> get_name();
echo $user2 -> get_name();

// echo $player1 -> get_id();

// var_dump($user1);

echo $player1 ->username;
echo $player2 ->userid;



//Inheritance 

class Gamer extends Player {
    public $gamer_score;
    public $gamer_level;
    public function __construct($gamer_name, $gamer_id, $gamer_score, $gamer_level)
    {
        parent::__construct($gamer_name, $gamer_id);
        $this->gamer_score = $gamer_score;
    }

    public function get_score() {
        return $this -> gamer_score;
    }
}

$gamer1 = new Gamer('Bradly', 'Kunush', 22, 100);

echo $gamer1 -> get_score();
?>