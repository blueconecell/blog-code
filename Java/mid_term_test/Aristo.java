package mid_term_test;

public class Aristo {
	public static void main(String[] argss) {
		int n = 40;
		
		boolean[] prime_check_arr = new boolean[n+1];
		
		for(int i=2; i<n; i++) {
//			if(i==2) {
//				prime_check_arr[i] = true;
//			}
			boolean can_prime = true;
			for(int j=2; j<i; j++) {
				if(i%j==0) {
					can_prime = false;
					prime_check_arr[i] = false;
					break;
				}
			}
			if(can_prime) {
				prime_check_arr[i] = true;
			}
		}
		for(int i=2; i<n; i++) {
			if (prime_check_arr[i]) {
				System.out.print(i+" ");
			}
		}
	}

}
