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
    public List<Integer> rightSideView(TreeNode root) {
        
        List <Integer> res = new ArrayList<>();
        
        if (root == null){
            return res;
        }
        
        Queue<TreeNode> Q = new LinkedList<>();
        Q.add(root);
            
        while(!Q.isEmpty()){
            int level_size = Q.size();
            for (int i = 0; i < level_size; i++){
                TreeNode curr = Q.remove();
                if (i == level_size - 1){
                    res.add(curr.val);
                }
                
                // add left child first
                if (curr.left != null){
                    Q.add(curr.left);
                }
                
                // then right child
                if (curr.right != null){
                    Q.add(curr.right);
                }
                
            }
           
            
        
        }
        
        return res;
    }
}