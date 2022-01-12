import java.io.*;
import java.util.*;

public class Java_10773{

    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<Integer>();
        
        int k = Integer.parseInt(bf.readLine());

        for(int i = 0; i<k; i++){
            int number = Integer.parseInt(bf.readLine());

            if(number == 0){
                stack.pop();
            }
            else{
                stack.push(number);
            }

        }
        int sum = 0;
        for (int o : stack){
            sum += o;
        }
        System.out.println(sum);
    }
    
}