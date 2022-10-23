package mid_term_test;

public class Prime_factor {
	public static void main(String[] argss) {
		int n = 40;
		
		int[] p = new int[n];
		int idx = 0;
		int prime = 2;
		
		while(n>1) {
			if(n%prime == 0) {
				p[idx] = prime;
				n = n/prime;
				idx+=1;
			}else {
				prime+=1;
			}
		}
		System.out.print("n의 소인수분해 = ");
		int while_idx = 0;
		while(while_idx < idx-1) {
			System.out.print(p[while_idx]+"*");
			while_idx+=1;
		}
		System.out.print(p[while_idx]);
	}

}
