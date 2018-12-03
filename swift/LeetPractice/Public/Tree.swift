//
//  Tree.swift
//  LeetPractice
//
//  Created by lunli on 2018/12/3.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class Tree: NSObject {

}

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
