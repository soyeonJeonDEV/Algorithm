import java.io.*;
import java.util.*;

public class Java_9498{
    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());

        if(a<=100 && a>=90){
            System.out.println('A');
        }else if(a<=89 && a>=80){
            System.out.println('B');
        }else if(a<=79 && a>=70){
            System.out.println('C');
        }else if(a<=69 && a>=60){
            System.out.println('D');
        }else{
            System.out.println('F');
        }
    }
}