//
//  IntCustomOperator.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/28.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class IntCustomOperator: NSObject {

}


extension Int {
    
    @discardableResult static postfix func ++(num: inout Int) -> Int {
        let temp = num
        num = num + 1
        return temp
    }
    
    @discardableResult static postfix func --(num: inout Int) -> Int {
        let temp = num
        num = num - 1
        return temp
    }
    
    @discardableResult static prefix func ++(num: inout Int) -> Int {
        num = num + 1
        return num
    }
    
    @discardableResult static prefix func --(num: inout Int) -> Int {
        num = num - 1
        return num
    }
}
