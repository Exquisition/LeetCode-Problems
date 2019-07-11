/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        // inorder is left, root, right
        // implement iteratively using stack
            
            
        List < Integer > res = new ArrayList <> ();
        Stack < TreeNode > stack = new Stack <> ();
        
        TreeNode curr = root;
        
        while(!stack.isEmpty() || curr != null){
            // if either stack is nonempty or current node isn't null, we need to add the value 
            // of the current node and move to the right
            
            
            //left
            while(curr != null){
                stack.push(curr);
                curr = curr.left;
            }
            
            //root
            curr = stack.pop();
            res.add(curr.val);
            //right 
            curr = curr.right;
        }
        
        return res;
        
    }
}