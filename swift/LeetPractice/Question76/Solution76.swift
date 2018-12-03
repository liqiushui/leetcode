//
//  Solution76.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/28.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution76: NSObject {
    func minWindow(_ s: String, _ t: String) -> String {
        var result: String = ""
        var letterCount: [Character:Int] = [:]
        var left = 0, count = 0, minLength = Int.max
        
        for c in t {
            letterCount.registerValue(key: c, value: 0)
            letterCount[c]!++
        }
        
        for i in 0..<s.count {
            letterCount.registerValue(key: s[i], value: 0)
            if --letterCount[s[i]]! >= 0 {
                ++count
            }
            while count == t.count {
                if minLength > i - left {
                    minLength = i - left
                    result = String(s[left...i])
                }
                
                if ++letterCount[s[left]]! > 0 {
                    --count
                }
                ++left
            }
        }
        
        return result
    }
}
