class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size();
        int i = 0;
        int j = 0;

        int sum = 0;

        while (i<n) {
            sum += mat[i][j];

            i += 1;
            j += 1;
        }

        i = 0;
        j = n-1;

        while (i<n) {
            sum += mat[i][j];

            i += 1;
            j -= 1;
        }

        if (n%2 == 0) return sum;
        int mid = n/2;
        return sum - mat[mid][mid];
    }
};
