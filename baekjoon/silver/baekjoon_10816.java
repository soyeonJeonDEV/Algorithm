import java.util.*;

public class baekjoon_10816{
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();

        for(int i =0; i<m;i++){
            int key = Integer.parseInt(st.nextToken());

            sb.append(upperBound(arr,key) - lowerBound(arr,key)).append(" ");
        }

    }
    private static int lowerBound(int[] arr, int key){
        int st = 0;
        int ed = arr.length;

        while(st < ed){
            int mid = (st+ed)/2;

            if(key <= arr[mid]){
                ed = mid;
            }else{
                st = mid+1;
            }
        }
        return st;
    }

    private static int upperBound(int[] arr, int key){
        int st = 0;
        int ed = arr.length;

        while (st < ed){
            int mid = (st + ed)/2;

            if(key < arr[mid]){
                ed = mid;
            }else{
                st = mid+1;
            }
        }
        return st;
    }
}