void main() {
  //int age = null //error;

  int? age;

  print(age == null); //true

  //this removes if statement null checking
  if(age != null) {
    //do something
  }

  String? answer;
  String result = answer!;
}

//late initialization 
class Animal {
  late final String _size;

  void goBig() {
    _size = 'big';
    print(_size);
  }
}