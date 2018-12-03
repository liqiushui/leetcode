//
//  Solution100.swift
//  LeetPractice
//
//  Created by lunli on 2018/12/3.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Solution100: NSObject {
    func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        
        if p == nil && q == nil {
            return true
        }
        
        if p == nil || q == nil {
            return false
        }
        
        return p!.val == q!.val && isSameTree(p!.left, q!.left) && isSameTree(p!.right, q!.right)
    }
}
