import java.io.*;
import java.util.*;

public class Java_1874{

    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Stack<Integer> stack = new Stack<>();

        int n = Integer.parseInt(bf.readLine());

        int start=0;

        while(n-- > 0){
            int value = Integer.parseInt(bf.readLine());

            if (value > start){
                for(int i = start+1; i<=value;i++){
                    stack.push(i);
                    sb.append('+').append('\n');
                }
                start = value;
            }else if(stack.peek() != value){
                System.out.println('NO');
                return;
            }
            stack.pop();
            sb.append('-').append('\n');
        }
        System.out.println(sb);
    }
    
}