public class binary {

  static StringBuilder binary;

  public static void formatting() {
    String text = "01010100 01101000 01101001 01110011 00100000 01110111 01101111 01110010 01101011 01110011 00100001";
    text = text.replaceAll("\\s", "");

    if (text.length() % 8 != 0) {
      System.out.println("Invalid binary string");
      System.exit(0);
    }

    binary = new StringBuilder(text);

    for (int i = 8; i < binary.length(); i += 9) {
      binary.insert(i, ' ');
    }
    
    System.out.println(binary);
  }

  public static void translation() {
    int index = 0;
    char current = binary.charAt(index);
    int ascii = 0;
    String translated = "";
    
    for (int i = 0; i < binary.length(); i+= 9) {
      ascii = 0;
      for (int x = 7; x >= 0; x--) {
        current = binary.charAt(index);
        if (current == '1') {
          ascii += Math.pow(2, x);
        }
        index++;
      }
      index++;
      translated += (char)ascii;
    }

    System.out.println(translated);
  }

  public static void main(String[] args) {
    formatting();
    translation();
  }
}