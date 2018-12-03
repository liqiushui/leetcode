//
//  Solution55.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/23.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution55: NSObject {
    func canJump(_ nums: [Int]) -> Bool {
        guard nums.count > 0 else {
            return false
        }
        
        var reach = 0
        var i = 0
        while i < nums.count && (i == 0 || i <= reach) && reach < nums.count - 1{
            reach = max(i + nums[i], reach)
            guard reach < nums.count - 1 else {return true}
            i = i + 1
        }
        return reach >= nums.count - 1
    }
}
