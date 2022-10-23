package mid_term_test;


public class Gold {
	public static void main(String[] argss) {
		int n = 40;
		int gold_even_num = 30;
		
		boolean[] p = new boolean[n+1];
		for(int i=2;i<n;i++) {
			boolean pCheck = true;
			for(int j=2; j<i; j++) {
				if(i%j==0) {
					p[i] = false;
					pCheck = false;
					break;
				}
			}
			if(pCheck) {
				p[i] = true;
			}
		}
		
		for(int i=2; i<gold_even_num/2; i++) {
			if(p[i]) {
				for(int j=gold_even_num; j>gold_even_num/2;j--) {
					if(p[j] && i+j== gold_even_num) {
						System.out.println(i+" "+j);
					}
						
				}
			}
		}
	}

}
