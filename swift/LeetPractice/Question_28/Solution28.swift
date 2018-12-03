//
//  Solution28.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/20.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution28: NSObject {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        guard needle.count > 0 else {return 0}
        guard haystack.count > 0 else {return -1}
        
        var i = 0;
        while i < haystack.count - needle.count  {
            var j = i;
            var k = 0
            while j < haystack.count && k < needle.count && haystack[j] == needle[k] {
                j = j + 1
                k = k + 1
            }
            
            guard k == needle.count else { i = i + 1; continue }
            return i
        }
        return -1
    }
}
