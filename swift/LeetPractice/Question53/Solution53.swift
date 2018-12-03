//
//  Solution53.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/22.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution53: NSObject {
    
    func maxSubArray(_ nums: [Int]) -> Int {
        var max_record:[Int] = Array.init(repeating: 0, count: nums.count)
        var max_sub = Int.min
        for i in 0..<nums.count{
            max_record[i] = (i>0) ? max(nums[i], nums[i] + max_record[i-1]) : nums[i]
            max_sub = max(max_record[i], max_sub)
        }
        return max_sub
    }
}
