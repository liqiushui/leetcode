//
//  Solution96.swift
//  LeetPractice
//
//  Created by lunli on 2018/12/3.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution96: NSObject {
    func numTrees(_ n: Int) -> Int {
        var dp = Array.init(repeating: 0, count: n + 1)
        dp[0] = 1;
        dp[1] = 1;
        
        if n >= 2 {
            
            for i in 2...n {
                for j in 0..<i {
                    dp[i] = dp[j] * dp[i-j-1] + dp[i]
                }
            }
        }
        
        return dp[n]
    }
}
