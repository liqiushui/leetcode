//
//  Solution66.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/26.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution66: NSObject {
    func plusOne(_ digits: [Int]) -> [Int] {
        
        guard digits.count > 0 else {
            return digits
        }
        
        var result = digits
        for i in (0..<result.count-1).reversed() {
            
            if result[i] < 9 {
                result[i] = result[i] + 1
                return result
            }
            
            result[i] = 0
        }
        
        result.insert(1, at: 0)
        return result
    }
}
