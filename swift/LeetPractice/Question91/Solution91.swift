//
//  Solution91.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/30.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution91: NSObject {
    func numDecodings(_ s: String) -> Int {
        return numDecodings("", s)
    }
    
    func numDecodings(_ head: String, _ tail: String) -> Int {
        
        let last = (Int(head) ?? 0)
        let one = tail.count >= 1 ? numDecodings(String(tail[0...0]), String(tail[1...])) : 0
        let two = tail.count >= 2 ? numDecodings(String(tail[0...1]), String(tail[2...])) : 0

        return ((last >= 1 && last <= 26) ? 1: 0) + one + two
    }
}
