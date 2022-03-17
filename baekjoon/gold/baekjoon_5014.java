import java.io.*;
import java.util.*;

public class baekjoon_5014 {


    static int F, S, G, U, D;
    static int[] visit;
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        F = Integer.parseInt(str[0]);
        S = Integer.parseInt(str[1]);
        G = Integer.parseInt(str[2]);
        U = Integer.parseInt(str[3]);
        D = Integer.parseInt(str[4]);
        visit = new int[F+1];
        System.out.println(bfs(F,S,G,U,D,visit));
        
    }
    public static String bfs(int Floor, int start, int end, int up, int down, int[] visit){
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(start);
        visit[start] = 1;

        while(!q.isEmpty()){
            int x = q.poll();

            if (x == end) return String.valueOf(visit[x] - 1);

            if (x + up <= end && visit[x + up] == 0){
                q.add(x + up);
                visit[x + up] = visit[x] + 1;
            } 

            if(x - down > 0 && visit[x - down] == 0){
                q.add(x - down);
                visit[x - down] = visit[x] + 1;
            }
        

        }
        
        return "use the stairs";

    }
}
