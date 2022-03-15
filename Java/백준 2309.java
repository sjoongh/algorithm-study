import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Solution {
    public static int[] dwarf;
    public static int sum;

    public static void main(String[] args) throws  Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        dwarf = new int[9];
        for(int i = 0 ; i<9; i++){
        	dwarf[i] = Integer.parseInt(br.readLine());
        	sum += dwarf[i];
        }
        find();
    }

    public static void find(){
        Arrays.sort(dwarf);
        for(int i = 0; i < 9 ; i++){
            for(int j = i+1; j < 9 ; j++){
                int result = sum - dwarf[i] - dwarf[j];
                if(result == 100){
                    for(int k = 0 ; k < 9; k ++){
                        if(k != i && k != j) System.out.println(dwarf[k]);
                    }
                    return; // return이 존재하지 않으면 result == 100일 때 다시 출력되므로 error
                }

            }
        }
    }


}