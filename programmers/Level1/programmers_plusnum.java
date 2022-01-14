import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        StringBuilder sb = new StringBuilder();
        String N = String.valueOf(n);
        for(int i=0; i< N.length();i++){
            char c = N.charAt(i);
            answer += c -'0';
        }
        
// 더 좋은 풀이        
//         while(true){
//             answer += n%10;
            
//             if(n < 10){
//                 break;
//             }
            
//             n = n/10;
//         }

        return answer;
    }
}