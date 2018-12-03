//
//  Solution54.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/21.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution54: NSObject {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        var result = [Int]()
        var tmpMat = matrix
        while tmpMat.count > 0 {
            result.append(contentsOf: tmpMat[0])
            tmpMat.remove(at: 0)
            tmpMat = zipMatrix(tmpMat).reversed()
        }
        return result
    }
    
    func zipMatrix(_ matrix: [[Int]]) -> [[Int]] {
        
        guard matrix.count > 0 else {
            return [[Int]]()
        }
        var result:[[Int]] = Array.init(repeating: [Int](), count: matrix[0].count)
        
        for col in 0..<matrix[0].count {
            for row in 0..<matrix.count {
                result[col].append(matrix[row][col])
            }
        }
        return result
    }
}
