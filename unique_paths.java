class Solution {
    public int uniquePaths(int m, int n) {
		
		\\ initialize dp matrix
		
		int [][] dp = new int[m][n]
		\\ first column is all ones
		for (int i = 0; i < dp.length; i++){
			dp[i][0] = 1
		}
		\\ first row is all ones
		for (int j = 0; j < dp[j].length; j++){
			dp[0][j] = 1
		} 
		
		\\ build the matrix to get dp[m-1][n-1]
		
		for (int i = 1; i < dp.length; i++){
			for (int j = 1; j < dp[i].length; j++){
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
		
		return dp[m-1][n-1]
        
       
    }
}