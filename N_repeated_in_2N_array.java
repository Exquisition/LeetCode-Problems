
class Solution {
    public int repeatedNTimes(int[] A) {
        int[] count = new int[10000];
        for (int a: A){
            count[a]++;
            if (count[a]>=2){
                return a;
            }
        }
        return -1;
}
}