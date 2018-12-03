//
//  Solution69.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/26.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution69: NSObject {
    func mySqrt(_ x: Int) -> Int {
        var res:Int = x
        while res * res > x {
            res = (res + x / res) / 2;
        }
        return res
    }
}
