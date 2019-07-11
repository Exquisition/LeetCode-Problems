//28. Implement strStr()

class Solution {
  public int strStr(String haystack, String needle) {
    
    int h1 = 0, h2 = 0, n1 = 0;

    if (needle.length() == 0){
       return 0; 
    } 
    if (needle.length() > haystack.length()) {
        return -1;
    }
    
    while (h1 <= haystack.length() - needle.length()) {
        h2 = h1;
        while (n1 < needle.length()) {
            if (haystack.charAt(h2) != needle.charAt(n1) ) {
                n1 = 0;
                break;
            }
            h2 += 1;
            n1 += 1;
        }
        if (n1 == needle.length()) return h1;
        h1 += 1;
    }
