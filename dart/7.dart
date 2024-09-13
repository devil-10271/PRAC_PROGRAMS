void main(){

  var a=10; // it can give value an int form && it can store only int value
  a=12;
  print(a.runtimeType);

  var b;  // here a value assign into a dynamic variable form
  b=true;
  b=1.33;
  print(b.runtimeType);

  dynamic ab=12;
  print(ab.runtimeType);
  ab='sahil';
  print(ab.runtimeType);
}