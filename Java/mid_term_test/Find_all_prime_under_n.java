package mid_term_test;

public class Find_all_prime_under_n extends Is_prime{
	public void find_all_prime_under_n_fuction(int n) {
		for(int i=2; i<n; i++) {
			if(is_prime_check_funtion(i)) {
				System.out.println(i+" ");
			}
		}
	}

}
