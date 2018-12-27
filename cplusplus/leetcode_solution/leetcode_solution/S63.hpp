//
//  S63.hpp
//  leetcode_solution
//
//  Created by lunli on 2018/12/13.
//  Copyright © 2018年 lunli. All rights reserved.
//

#ifndef S63_hpp
#define S63_hpp

#include "public.hpp"
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

class Solution63 {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int> > dp(m + 1, vector<int> (n + 1, 0));
        dp[0][1] = 1;
        for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
        if (!obstacleGrid[i - 1][j - 1])
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        return dp[m][n];
    }
};

#endif /* S63_hpp */
