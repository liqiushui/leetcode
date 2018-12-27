//
//  S297.hpp
//  leetcode_solution
//
//  Created by lunli on 2018/12/3.
//  Copyright © 2018年 lunli. All rights reserved.
//

#ifndef S297_hpp
#define S297_hpp

#include "public.hpp"
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

class Codec {
public:
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        
        vector<int> s = vector<int>();
        this->serialize(root, s);
        //
        return "";
    }
    
    void serialize(TreeNode* root, vector<int> &levelRecord) {
        if(root) {
            levelRecord.push_back(root->val);
            this->serialize(root->left, levelRecord);
            this->serialize(root->right, levelRecord);
        }
    }
    
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        
        return NULL;
    }
};

#endif /* S297_hpp */
