import java.io.*;
import java.util.*;

public class Java_1152{
    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        System.out.print(st.countTokens());
    }
}