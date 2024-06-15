LESSSON 2 DART BASICS VARIABLES
void main() {
  var name = "mario";
  
  print(name);
  
  const  age = 25;
  print(age);
  
 // + - * / % 
  
  print("my name is " + name);
  //print("my name is ${name}");
  print("my name is $name and my age is $age");
  /**/
}







LESSON 3 TYPE ANNOTATIONS
void main() {
  
  const String name = "mario";
  print(name);
  
  int age = 25;
  print(age);
  
  bool isOpen = true;
  print(isOpen);
  
  double averageRating = 7;
  averageRating = 7.6;
  print(averageRating);
  
  int? points;
  print(points);
}





LESSON 4 FUNCTIONS
Unamed parameters
Named parameters {}








LESSON 5
Lists and sets 
Non Static
Static <>








LESSON 6
control flow 
void main() {
  List<int> scores = [50, 75, 20, 99, 100, 30];
  
//   for (int i = 0; i < 5; i++) {
//     print("the current value of 1 is $i");
//   }
  
//   for (int score in scores) {
//     if (score > 50) {
//       print("th score is $score");
//     } else {
//       print("score not high enough");
//     }
//   }
  
    for (int score in scores.where((s) => s > 50)) {
      print("The score is $score");
  }
}







LESSON 7 
Maps 
void main() {
  
//   var planets = {
// //     "first" : "mecury",
//     1 : "mecury",
//   };
  
  Map<String, String> planets = {
    "first" : "mecury",
    "second" : "venus",
    "third" : "earth",
    "fourth" : "mars",
    "fifth" : "jupiter"
  };
  
  planets["sixth"] = "uranus";
  
  print(planets["fifth"]);
  print(planets);
  
  print(planets.containsKey("third"));
  print(planets.containsValue("third"));
  print(planets.remove("third"));
  
  
  
  print(planets);
}









LESSON 8
classes
void main() {
  
  var noodles = MenuItem("veg noodles", 9.99);
//   var pizza = MenuItem("volcano pizza", 12.99);
  var pizza = Pizza(["mushrooms", "peppers"], "veg volcano", 15.99);
  
  print(noodles.title);
  print(noodles.price);
  print(pizza.title);
  print(pizza.price);
  print(noodles.format());
  print(pizza.format());
}

class MenuItem {
  String title;
  double price;
  
  MenuItem(this.title, this.price);
  
  String format() {
    return "$title --> $price";
  }
}

//inheritance
class Pizza extends MenuItem {
  List<String> toppings;
  
  Pizza(this.toppings, String title, double price) : super(title, price);
  Pizza(this.toppings, super.title, super.price);
}








LESSON 9
method overriding
void main() {
  
  var noodles = MenuItem("veg noodles", 9.99);
//   var pizza = MenuItem("volcano pizza", 12.99);
  var pizza = Pizza(["mushrooms", "peppers"], "veg volcano", 15.99);
  
  print(noodles.title);
  print(noodles.price);
  print(pizza.title);
  print(pizza.price);
  print(noodles.format());
  print(pizza.format());
  print(noodles);
  print(pizza);
}

class MenuItem {
  String title;
  double price;
  
  MenuItem(this.title, this.price);
  
  String format() {
    return "$title --> $price";
  }
  
  @override
  String toString() {
    return format();
  }
}

//inheritance
class Pizza extends MenuItem {
  List<String> toppings;  
//   Pizza(this.toppings, String title, double price) :super(title, price);
  Pizza(this.toppings, super.title, super.price);
  
  @override
  String format() {
    var formattedToppings = 'Contains:';
    
    for (final t in toppings) {
      formattedToppings = '$formattedToppings $t';
    }
  
  return '$title -> NGN$price \n$formattedToppings';
  }
  
  @override 
  String toString () {
    return 'Instance of Pizza: $title, $price, $toppings';
  }
}









LESSON 10
Generics
void main() {
  
  var noodles = MenuItem("veg noodles", 9.99);
//   var pizza = MenuItem("volcano pizza", 12.99);
  var pizza = Pizza(["mushrooms", "peppers"], "veg volcano", 15.99);
  var roast = MenuItem('veggie roast dinner', 12.49);
  var kebab = MenuItem('plant kebab', 7.49);
  
  print("$noodles, $pizza, $roast, $kebab");
  
  var foods = Collection<MenuItem>(
    'Menu Items',
    [noodles, pizza, roast, kebab]
  );
  
  var random = foods.randomItem();
  print(random);
  
  print(noodles.title);
  print(noodles.price);
  print(pizza.title);
  print(pizza.price);
  print(noodles.format());
  print(pizza.format());
  print(noodles);
  print(pizza);
}

class MenuItem {
  String title;
  double price;
  
  MenuItem(this.title, this.price);
  
  String format() {
    return "$title --> $price";
  }
  
  @override
  String toString() {
    return format();
  }
}

//inheritance
class Pizza extends MenuItem {
  List<String> toppings;  
//   Pizza(this.toppings, String title, double price) :super(title, price);
  Pizza(this.toppings, super.title, super.price);
  
  @override
  String format() {
    var formattedToppings = 'Contains:';
    
    for (final t in toppings) {
      formattedToppings = '$formattedToppings $t';
    }
  
  return '$title -> NGN$price \n$formattedToppings';
  }
  
  @override 
  String toString () {
    return 'Instance of Pizza: $title, $price, $toppings';
  }
}

class Collection<T> {
  String name;
  List<T> data;
  
  Collection(this.name, this.data);
  
  randomItem() {
    data.shuffle();
    
    return data[0];
  }
}












LESSON 11
Async, Await and Futures
void main () async {
  
//   fetchPost().then((p) {
//     print(p.title);
//     print(p.userId);
//   });
  
  final post = await fetchPost();
  print(post.title);
  print(post.userId);
  
}

Future<Post> fetchPost() {
  const delay = Duration(seconds: 3);
  
  return Future.delayed(delay, (){
    return Post('my post', 123);
  });
}

class Post {
  String title;
  int userId;
  
  Post(this.title, this.userId);
}








LESSON 12
Fetching Data
import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

void main () async {
  final post = await fetchPost();
  
  print(post.title);
  print(post.userId);
}

Future<Post> fetchPost() async {
 var uri = Uri.https('jsonplaceholder.typicode.com', '/posts/2');
  
  final response = await http.get(uri);
  
  Map<String, dynamic> data = convert.jsonDecode(response.body);
  
  return Post(data["title"], data["userId"]);
}

class Post {
  String title;
  int userId;
  
  Post(this.title, this.userId);
}