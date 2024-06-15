void main () {
  String takeFive() {
    return '';
  }
  takeTwo() {
    return '';
  }

  String takeSix(int number) {
    return '$number minus five equals ${number -5}';
  }

  takeSix(23);

  namedParams({required int a, int b =5 }) {
    return a - b;
  }

  namedParams(a: 23, b: 10);

  //arrow function 
  takeTen(int number) => '$number minus ten equals ${number - 10}';
  takeTen(23);

//Anonymous Function
callIt (called) {
  return called;
}

callIt (
    () => 'hola mundo!'
  );
}

