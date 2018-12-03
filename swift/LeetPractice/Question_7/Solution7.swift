//
//  Solution7.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/19.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution7: NSObject {
    func reverse(_ x: Int) -> Int {
        var temp = (x > 0 ? x : (-1 * x))
        var stack = [Int]()
        while temp > 0 {
            stack.append(temp%10)
            temp = temp/10
        }
        
        var result = 0
        for e in stack {
            result = result*10 + e
        }
        
        let limit:Int64 = Int64(1 << 31)
        result = (x > 0 ? result : (-1 * result))
        if(result > 0) {
            return (result > limit-1 ? 0 : result)
        }
        else {
            return (result < limit * -1 ? 0 : result)
        }
    }
}

/*
 
 
 let s = Solution7()
 
 for i in 0...31
 {
 print(2 << i)
 }
 print(s.reverse(123))
 print(s.reverse(1230))
 print(s.reverse(-1230))
 
 */
