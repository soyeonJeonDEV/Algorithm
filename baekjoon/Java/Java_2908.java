import java.io.*;
import java.util.*;

public class Java_2908{
    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringBuffer sb = new StringBuffer(bf.readLine());
        String reverse = sb.reverse().toString();
        StringTokenizer st = new StringTokenizer(reverse, " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        if(a>b){
            System.out.print(a);
        }else{
            System.out.print(b);
        }

    }
}