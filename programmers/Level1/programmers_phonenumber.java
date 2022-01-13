//https://programmers.co.kr/learn/courses/30/lessons/12948?language=java
//핸드폰 번호 가리기

class Solution {
    public String solution(String phone_number) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        for(int i=0;i<phone_number.length();i++){
            if(i<phone_number.length()-4){
                sb.append("*");
            }
            else{
                char ch = phone_number.charAt(i);
                sb.append(ch);
            }
        }
        answer = sb.toString();
        return answer;
    }
}