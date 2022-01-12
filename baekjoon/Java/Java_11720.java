import java.io.*;
import java.util.*;

public class Java_11720{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String a = sc.next();
        sc.close();

        int sum = 0;

        for(int i=0;i<n;i++){
            sum += a.charAt(i)-'0';
        }
        System.out.println(sum);
    }
}