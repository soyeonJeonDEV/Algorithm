import java.io.*;
import java.util.*;

public class Java_2588{
    public static void main(String args[]) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        String B = br.readLine();
        char[] b = B.toCharArray();

        System.out.println(a*(b[2]-'0'));
        System.out.println(a*(b[1]-'0'));
        System.out.println(a*(b[0]-'0'));
        System.out.println(a*Integer.parseInt(B));


    }
}