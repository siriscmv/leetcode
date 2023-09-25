/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        return solve(root, 0);
    }

    int solve(TreeNode* root, int sum) {
        if (!root) return sum;

        int l = solve(root->left, sum + 1);
        int r = solve(root->right, sum + 1);

        if (l > r) return l;
        return r;
    }
};
