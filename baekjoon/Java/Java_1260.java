import java.io.*;
import java.util.*;

public class Java_1260{
    static int[][] graph;
    static boolean[] visited = new boolean[1001];
    static int n,m;

    static Queue<Integer> q = new LinkedList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
     
        String[] token = bf.readLine().split(" ");

        n = Integer.parseInt(token[0]);
        m = Integer.parseInt(token[1]);
        int v = Integer.parseInt(token[2]);

        graph = new int[n+1][n+1];

        for(int i=0;i<m;i++){
            token = bf.readLine().split(" ");
            int node1 = Integer.parseInt(token[0]);
            int node2 = Integer.parseInt(token[1]);

            graph[node1][node2] = 1;
            graph[node2][node1] = 1;
        }

        dfs(v);
        sb.append("\n");
        Arrays.fill(visited,false);
        
        bfs(v);
        System.out.println(sb);
        sb.setLength(0);
        Arrays.fill(visited,false);
    }
    
    private static void dfs(int v){
        visited[v] = true;
        sb.append(v).append(" ");
        for(int i=1; i<=n;i++){
            if(graph[v][i] == 1 && !visited[i]){
                dfs(i);
            }
        }
    }
    static void bfs(int v){
        q.add(v);
        visited[v] = true;

        while(!q.isEmpty()){
            v = q.poll();
            sb.append(v).append(" ");

            for(int i=1;i<=n;i++){
                if(graph[v][i] == 1 && !visited[i]){
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
        q.clear();
    }

}