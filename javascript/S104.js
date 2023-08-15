/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    function _depth(root, level, max_level) {
        if(root) {
            max_level.val = Math.max(max_level.val, level + 1);
            _depth(root.left, level + 1, max_level);
            _depth(root.right, level + 1, max_level);
        }
    }
    let max_level = {val: 0};
    _depth(root, 0, max_level);
    return max_level.val;
};