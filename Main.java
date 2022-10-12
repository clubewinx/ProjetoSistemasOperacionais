import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;
import java.io.FileNotFoundException;






class Main {
  public static void main(String[] args) throws FileNotFoundException{
    File file = new File("txt.txt");
    String  Items;
    Scanner scan = new Scanner(file);

    while (scan.hasNextLine()) {
      //Items = scan.nextLine();
      System.out.println(scan.nextLine());
    }
      
  }
}