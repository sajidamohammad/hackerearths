import java.util.*;
import java.io.*;
class deepu{
	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String array=br.readLine();
		int count=Integer.parseInt(array);
		int numbers[]=new int[count];
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		for (int i=0; i<count;i++){
			numbers[i]=Integer.parseInt(st.nextToken());
		}
		int M=Integer.parseInt(br.readLine());
		for (int j=0;j<M;j++){
			hit(numbers, Integer.parseInt(br.readLine()));
		}
		for (int k=0;k<numbers.length;k++){
			System.out.print(numbers[k]+" ");
		}
	}

	private static void hit(int[] numbers, int x){
		for (int i=0;i<numbers.length;i++) {
			if (numbers[i]>x)
				numbers[i]=numbers[i]-1;
		}
	}
}

