import java.io.*;
import java.util.*;

public class Java_2739{
    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(bf.readLine());

        for(int i = 1; i<10; i++){
            System.out.println(num + " * " + i + " = " + num*i);
        }
    }
}