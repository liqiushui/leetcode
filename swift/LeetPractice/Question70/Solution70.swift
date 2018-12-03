//
//  Solution70.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/27.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution70: NSObject {
    var map:[Int:Int] = [:]
    func climbStairs(_ n: Int) -> Int {
        guard n > 3 else { return n}
        if let val = map[n] {
            return val
        }
        let x = climbStairs(n - 1) + climbStairs(n - 2)
        map[n] = x
        return x
    }
}
