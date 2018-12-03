//
//  Solution118.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/30.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution118: NSObject {
    func generate(_ numRows: Int) -> [[Int]] {
        
        var result: [[Int]] = []
        guard numRows > 0 else {
            return result
        }
        for i in 0...(numRows-1) {
            if i == 0 {
                result.append([1])
            }
            else {
                let last = result[i-1]
                var tmp: [Int] = []
                for i in 0..<(last.count + 1) {
                    if i == 0 || i == last.count {
                        tmp.append(1)
                    }
                    else {
                        tmp.append(last[i-1] + last[i])
                    }
                }
                result.append(tmp)
            }
        }
        return result
    }
    
}
