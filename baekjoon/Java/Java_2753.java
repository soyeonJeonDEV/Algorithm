import java.io.*;
import java.util.*;

public class Java_2753{
    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int year = Integer.parseInt(bf.readLine());

        if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
            System.out.println(1);
        }else{
            System.out.println(0);
        }

    }
}