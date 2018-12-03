//
//  Solution75.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/27.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution75: NSObject {
    func sortColors(_ nums: inout [Int]) {
        if nums.count > 1 {
            var left = 0
            var right = nums.count - 1
            for i in 0...right {
                
                while nums[i] == 2 && right > i {
                    nums.swapAt(i, right)
                    right = right - 1
                }
                
                while nums[i] == 0 && left < i {
                    nums.swapAt(i, left)
                    left = left + 1
                }
            }
        }
    }
}
