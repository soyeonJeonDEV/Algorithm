import java.io.*;
import java.util.*;

public class Java_1157{
    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[26];

        String str = bf.readLine();
        str = str.toUpperCase();
        for(int i=0;i<str.length();i++){
            char ch = str.charAt(i);
            arr[ch-'A']++;
        }
        int max = -1;
        char c = '?';
        for(int i=0;i<26;i++){
            if(max < arr[i]){
                max = arr[i];
                c = (char)('A' + i);
            }else if(max == arr[i]){
                c='?';
            }
        }
        System.out.print(c);
    }
}