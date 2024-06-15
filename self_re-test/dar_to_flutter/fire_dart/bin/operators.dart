void main () {
  //logic 
  1 == 1;
  1 < 2;
  (1 >= 1) || ('a' == 'b');

  var x = 1;
  x++; // x = x + 1
  x--; // x = x -1

  //assignment 
  String? name;
  name ??= 'Guest';
  var z = name ?? 'Guest';


  //ternary 
  String color = 'blue';
  var isThisBlue = color == 'blue' ? 'Yep, blue it is' : 'Nah, it ain\'t blue';

  //cascade
  dynamic Paint;

  // var paint = Paint();
  // paint.color = 'black';
  // paint.strokeCap = 'round';
  // paint.strokeWidth = 5.0;

  var paint = Paint()
  ..color = 'black'
  ..strokeCap = 'round'
  ..strokeWidth = 5.0;



  //Typecast 
  var number = 23 as String;
  number is String; //true
}