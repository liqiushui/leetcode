//
//  Solution36.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/21.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

extension Character {
    var integerValue:Int {
        return Int(String(self)) ?? 0
    }
}

class Solution36: NSObject {
    
    func isValidSudoku(_ board: [[Character]]) -> Bool {
        var row_mark:[[Int]] = Array.init(repeating: Array.init(repeating: 0, count: 9), count: 9)
        var col_mark:[[Int]] = Array.init(repeating: Array.init(repeating: 0, count: 9), count: 9)
        var box_mark:[[Int]] = Array.init(repeating: Array.init(repeating: 0, count: 9), count: 9)
        
        for row in 0..<board.count {
            for col in 0..<board[row].count {
                if(board[row][col] != Character.init(".")){
                    let num = board[row][col].integerValue - 1
                    let box_index = (row/3)*3 + col/3
                    if row_mark[row][num] == 1 ||
                       col_mark[col][num] == 1 ||
                       box_mark[box_index][num] == 1 {
                        return false
                    }
                    
                    row_mark[row][num] = 1
                    col_mark[col][num] = 1
                    box_mark[box_index][num] = 1
                }
            }
        }
        
        return true
    }
}
