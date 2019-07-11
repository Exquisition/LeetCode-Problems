import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    //SuperReducedString function below.
    
    static String superReducedString(String s) {
                StringBuffer returnedString = new StringBuffer(s);
        for(int i = 1; i < returnedString.length(); i++) {
            if(returnedString.charAt(i) == returnedString.charAt(i-1)) {
                

                returnedString.delete(i-1, i+1);
                i = 0;
            }
        }

        if(returnedString.length() == 0){
            return("Empty String");
        }
        else{
            System.out.println(returnedString);
            String thing = returnedString.toString();
            return thing;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = superReducedString(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
