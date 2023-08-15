/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var mergeTrees = function (root1, root2) {
    // 如果root1为空，不管root2是否为空，直接返回root2
    if (root1 == null) return root2;
    // 同理对于root2也一样
    if (root2 == null) return root1;
    // 走到这里，肯定root1和root2都不为空了，这里直接相加赋值root1就行
    root1.val = root1.val + root2.val;
    // 递归的对左子树和右子树进行同样操作
    root1.left = mergeTrees(root1.left, root2.left);
    root1.right = mergeTrees(root1.right, root2.right);
    return root1;
};