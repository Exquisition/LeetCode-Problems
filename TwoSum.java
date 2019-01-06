import java.util.Hashtable;

//Hashtable solution
public class Solution {

public int[] twoSum(int[] numbers, int target) {
    int[] solution = new int[2];
    Hashtable<Integer, Integer> table = new Hashtable<Integer, Integer>();
    
    for(int i = 0; i < numbers.length; i++){
        if(table.containsKey(numbers[i])){
            solution[0] = table.get(numbers[i]);
            solution[1] = i;
        }
        table.put(target - numbers[i], i);
    }
    return solution;
}
}
