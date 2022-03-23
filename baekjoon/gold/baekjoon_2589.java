import java.io.*;
import java.util.*;

public class baekjoon_2589{

    static int n,m;
    static int answer, cnt;
    static char[][] graph;
    static int[][] dist;
    static boolean[][] visited;
    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,1,0,-1};
    static ArrayList<Integer> result = new ArrayList<Integer>();

    public static void main(String[] args) throws IOException{
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            String[] str = bf.readLine().split(" ");

            n = Integer.parseInt(str[0]);
            m = Integer.parseInt(str[1]);

            graph = new char[n][m];
            visited = new boolean[n][m];
            dist = new int[n][m];

            answer = 0;

            for(int i=0; i<n; i++){
                char[] ch = bf.readLine().toCharArray();
                for (int j=0; j<m; j++){
                    graph[i][j] = ch[j];
                }
            }

            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    if (graph[i][j] == 'L'){
                        bfs(i,j);
                    }
                    for(int k=0; k<n;k++){
                        Arrays.fill(visited[k],false);
                        Arrays.fill(dist[k],0);
                    }
                    
                }
            }

            System.out.println(Collections.max(result));
        
    }

    public static void bfs(int a,int b){

        cnt = 0;

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{a,b});
        visited[a][b] = true;

        while(!q.isEmpty()){
            int x = q.poll()[0];
            int y = q.poll()[1];
            
            for(int i=0; i<4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0<=nx && 0<=ny && nx<m && ny<n){
                    if(!visited[nx][ny] && graph[nx][ny] == 'L'){
                        dist[nx][ny] = dist[x][y] + 1;
                        visited[nx][ny] = true;
                        q.add(new int[] {nx,ny});

                    }
                }
            }
        }
        

    }
    
}
