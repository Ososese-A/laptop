void main () {
  const String quest = "A car in 1986 was 1500 naira. If the global economy has being going up by 9% since then, what is the price of that same car in the current year?";

  // test one for calculating 9% of 1500 and getting the new rpincipal amount
  // const double calc = (1500 * 9)/100;
  // const double principal = 1500 + calc;
  // print(calc);
  // print(principal);

  //to get the number of times the loop should run from the date
  const int current_date = 2024;
  const int old_date = 1986;
  const int loop_no = current_date - old_date;
  print(loop_no);

  int i = 0;
  var principal = 1500.0;
  while (i < (loop_no + 1)) {
    var new_principal = principal;
    var increase = (new_principal * 9)/100;
    principal = increase + new_principal;
    i++;
    print(i);
    print(new_principal);
  }


  print(quest);
}