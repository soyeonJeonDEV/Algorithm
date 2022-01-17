//예산

import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        for(int n : d){
            if(budget> 0){
                budget -= n;
                if(budget < 0) break;
                answer++;
            }
        }
       

        return answer;
    }
}