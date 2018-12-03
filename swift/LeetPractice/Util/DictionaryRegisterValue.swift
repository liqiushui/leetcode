//
//  DictionaryRegisterValue.swift
//  LeetPractice
//
//  Created by lunli on 2018/11/28.
//  Copyright © 2018年 lunli. All rights reserved.
//

import Cocoa

class DictionaryRegisterValue: NSObject {

}

extension Dictionary where Key: Hashable {
    
    @discardableResult public mutating func registerValue(key: Key, value: Value) -> Bool {
        
        if self.keys.contains(key) {
            return false
        }
        
        self.updateValue(value, forKey: key)
        
        return true
    }
}
