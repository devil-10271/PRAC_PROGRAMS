void main() {
  for (var i = 0; i < 5; i++) {
    if (i == 2) {
      break;
    }
    print("i = $i");
  }
  for (dynamic j = 0; j < 5; j++) {
    if (j == 1) {
      continue;
    }
    print('*'*(j+1));
  }
}
