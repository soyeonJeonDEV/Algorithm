// 완주하지 못한 선수

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hash = new HashMap<>();
        
        for(String str : participant){
            hash.put(str,hash.getOrDefault(str,0) + 1);
        }
        
        for(String str : completion){
            hash.put(str, hash.get(str)-1);
        }
        for(String key : hash.keySet()){
            if(hash.get(key) == 1) answer = key;
        }
        return answer;
    }
}