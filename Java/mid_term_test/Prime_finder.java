package mid_term_test;

public class Prime_finder {

	public static void main(String[] args) {
		int n = 40;
		
		for(int i=2; i<n; i++) {
//			if(i==2) {
//				System.out.print(i+" ");
//			}
			boolean can_be_prime = true;
			for(int j=2; j<i; j++) {
				if(i%j==0) {
					can_be_prime = false;
					break;
				}
			}
			if(can_be_prime) {
				System.out.print(i+" ");
			}
			
		}
	}
}