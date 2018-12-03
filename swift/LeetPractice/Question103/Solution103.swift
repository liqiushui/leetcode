//
//  Solution103.swift
//  LeetPractice
//
//  Created by lunli on 2018/12/3.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Solution103: NSObject {
    func zigzagLevelOrder(_ root: TreeNode?) -> [[Int]] {
        
        var record: [[Int]] = []
        zigzagLevelOrder(root, levelRecord: &record, curLevel: 0)
        return record
    }
    
    
    func zigzagLevelOrder(_ root: TreeNode?, levelRecord: inout [[Int]], curLevel:Int) {
        
        if let node = root {
            levelRecord[curLevel].append(node.val)
            if levelRecord.count <= (curLevel + 1) {  levelRecord.append([]) }
            if(curLevel % 2 == 0) {
                zigzagLevelOrder(node.left, levelRecord: &levelRecord, curLevel: curLevel+1)
                zigzagLevelOrder(node.right, levelRecord: &levelRecord, curLevel: curLevel+1)
            }
            else {
                zigzagLevelOrder(node.right, levelRecord: &levelRecord, curLevel: curLevel+1)
                zigzagLevelOrder(node.left, levelRecord: &levelRecord, curLevel: curLevel+1)
            }
        }
    }
        
}

