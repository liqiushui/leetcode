//
//  Solution56.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/23.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa



 public class Interval {
   public var start: Int
   public var end: Int
   public init(_ start: Int, _ end: Int) {
     self.start = start
     self.end = end
   }
 }

class Solution56: NSObject {
    func merge(_ intervals: [Interval]) -> [Interval] {
        guard intervals.count > 1 else {
            return intervals
        }
        
        var result: [Interval] = intervals
        result.sort { (left:Interval, right:Interval) -> Bool in
            return left.start < right.start
        }
        
        var start = 0
        var length = result.count
        while start < length - 1 {
            
            if result[start].end >= result[start+1].start {
                result[start].end = max(result[start+1].end, result[start].end)
                result.remove(at: start+1)
                length = length - 1
            }
            else {
                start = start + 1
            }
        }
        return result
    }
}
