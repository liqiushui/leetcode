//
//  Solution119.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/30.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution119: NSObject {
    func getRow(_ rowIndex: Int) -> [Int] {

        var result: [Int] = []
        for i in 0...rowIndex {
            result.append(C_N_K(N: rowIndex, K: i))
        }
        return result
    }
    
    
    func C_N_K(N:Int, K:Int) -> Int {
        guard K != 0 && K != N else {
            return 1
        }
        
        guard K <= N - K else {
            return C_N_K(N: N, K: N - K)
        }
        
        var temp_top:Int = N
        var temp_down:Int = K
        var top:Double = 1
        var down:Double = 1
        for _ in 1...K {
            top = top * Double(temp_top)
            temp_top = temp_top - 1
            down = down * Double(temp_down)
            temp_down = temp_down - 1
        }

        
        print(top/down + 0.01)
        return Int(top/down)
    }
}
