//
//  Solution_8.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/19.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution_8: NSObject {
    
    func myAtoi(_ str: String) -> Int {
        var trimstr = str.trimmingCharacters(in: .whitespaces)
        let sign:Int64 = (trimstr.count > 0 && trimstr[0] == "-") ? -1 : 1;
        trimstr = trimstr.trimmingCharacters(in: ["-"])
        guard trimstr.count > 0 else {
            return 0
        }
        let limit = 1 << 31
        var result:Int64 = 0
        for i in 0...trimstr.count-1 {
            if trimstr[i] >= "0" && trimstr[i] <= "9" {
                let off:Int64 = Int64(trimstr[i].unicodeScalars.first!.value - Unicode.Scalar("0")!.value)
                result = result*10 + off
                if result < limit * -1 {
                    return -2147483648
                }
                if result > (limit - 1) {
                    return limit - 1
                }
            }
            else {
                return Int(result)
            }
        }
        result = result * sign
        if result < limit * -1 {
            return -2147483648
        }
        if result > (limit - 1) {
            return limit - 1
        }
        return Int(result)
    }
}
