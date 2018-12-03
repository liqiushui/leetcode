//
//  Solution94.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/30.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

/*
 public class TreeNode {
     public var val: Int
     public var left: TreeNode?
     public var right: TreeNode?
     public init(_ val: Int) {
         self.val = val
         self.left = nil
         self.right = nil
     }
 }
*/
class Solution94: NSObject {

    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        var r: [Int] = []
        inorderTraversal(root, &r)
        return r
    }

    func inorderTraversal(_ root: TreeNode?, _ record: inout [Int]) {
        if let left = root?.left {
            inorderTraversal(left, &record)
        }
        record.append(root!.val)
        if let right = root?.right{
            inorderTraversal(right, &record)
        } 
    } 

}
