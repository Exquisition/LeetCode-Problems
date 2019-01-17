class Solution {
    public int trap(int[] height) {
        if(height.length <= 2) {
            return 0;
        }
        int total = 0;
        int[] forward = new int[height.length];
        int[] backward = new int[height.length];
        forward[0] = height[0];
        backward[height.length-1] =  height[height.length-1];

        for(int i = 1; i<height.length; i++) {
            if(height[i] > forward[i-1]) {
                forward[i] = height[i];
            } else {
                forward[i] = forward[i-1];
            }
        }

        for(int i = height.length-2; i>= 0; i--) {
            if(height[i] > backward[i+1]) {
                backward[i] = height[i];
            } else {
                backward[i] = backward[i+1];
            }
        }

        for(int i = 0; i<height.length; i++) {
            total += Math.min(forward[i], backward[i]) - height[i];
        }
        return total;


    }
}