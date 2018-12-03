//
//  Solution62.swift
//  LeetPractice
  //  Created by lunli on 2018/11/23.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution62: NSObject {
    
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        guard m >= 1 && n >= 1 else {
            return 0
        }
        
        if m == 1 || n == 1 {
            return 1
        }
        return uniquePaths( m - 1, n ) + uniquePaths( m , n - 1)
    }
    
    //优化版本
    func uniquePaths2(_ m: Int, _ n: Int) -> Int {
        guard m >= 1 && n >= 1 else {
            return 0
        }
        if m == 1 || n == 1 {
            return 1
        }
        var dp: [[Int]] = Array.init(repeating: Array.init(repeating: 1, count: m), count: n)
        for row in 1..<n {
            for col in 1..<m {
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
            }
        }
        return dp[n-1][m-1]
    }
}
