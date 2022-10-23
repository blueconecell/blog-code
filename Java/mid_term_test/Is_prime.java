package mid_term_test;

public class Is_prime {
	public boolean is_prime_check_funtion(int n) {
		for(int i=2; i*i < n+1; i++) {
			if(n%i == 0) {
				return false;
			}
		}return true;
	}
}
