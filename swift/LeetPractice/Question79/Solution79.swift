//
//  Solution79.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/28.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution79: NSObject {
    func exist(_ board: [[Character]], _ word: String) -> Bool {
        
        var mark: [[Int]] = Array.init(repeating: Array.init(repeating: 0, count: board[0].count), count: board.count)
        
        for row in 0..<board.count {
            for col in 0..<board[0].count {
                if board[row][col] == word[0] {
                    if search(board, word, &mark, row, col) {
                        return true
                    }
                }
            }
        }
        
        return false
    }
    
    func search(_ board: [[Character]], _ word: String,
                _ mark: inout [[Int]], _ posX: Int, _ posY: Int) -> Bool {
        
        
        guard word.count > 0 else {
            return true
        }
        
        guard posX >= 0 && posX < board.count && posY >= 0 && posY < board[0].count else {
            return false
        }
        
        let suffix = String(word.suffix(word.count-1))

        if board[posX][posY] == word[0] && mark[posX][posY] == 0 {
            
            mark[posX][posY] = 1
            
            if ( search(board, suffix, &mark, posX+1, posY) ||
                 search(board, suffix, &mark, posX-1, posY) ||
                 search(board, suffix, &mark, posX, posY+1) ||
                 search(board, suffix, &mark, posX, posY-1) ) {
                return true
            }
            mark[posX][posY] = 0
        }

        
        return false
    }
}
