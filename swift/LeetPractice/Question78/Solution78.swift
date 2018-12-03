//
//  Solution78.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/28.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution78: NSObject {
    func subsets(_ nums: [Int]) -> [[Int]] {
        
        let len = nums.count
        var result: [[Int]] = []
        for cur in 1...(1<<len) {
            var temp: [Int] = []
            for i in 0..<len {
                if cur&(1<<i) != 0 {
                    temp.append(nums[i])
                }
            }
            result.append(temp)
        }
        result.append([])
        return result
    }
}

/*
func subsets(_ nums: [Int]) -> [[Int]] {
    var res = [[Int]()]
    subset(&res, nums)
    return res
}

private func subset(_ res: inout [[Int]], _ nums: [Int]) {
    guard let n = nums.first else { return }
    res += res.map { $0 + [n] }
    subset(&res, Array(nums[1..<nums.count]))
}
*/
