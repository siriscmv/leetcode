class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int a=0, b=0, c=matrix[0].size()-1, d=matrix.size()-1;
        int i=0, j=0;

        while (true) {
            if (j>c) break;
            while(j<=c) { ans.push_back(matrix[i][j]); j+=1; }
            j-=1; i+=1; b+=1;

            if (i>d) break;
            while(i<=d) { ans.push_back(matrix[i][j]); i+=1; }
            i-=1; j-=1; c-=1;

            if (j<a) break;
            while(j>=a) { ans.push_back(matrix[i][j]); j-=1; }
            j+=1; i-=1; d-=1;

            if (i<b) break;
            while(i>=b) { ans.push_back(matrix[i][j]); i-=1; }
            i+=1; j+=1; a+=1;
        }
        
        return ans;
    }
};
