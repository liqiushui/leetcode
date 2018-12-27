//
//  public.hpp
//  leetcode_solution
//
//  Created by lunli on 2018/12/3.
//  Copyright © 2018年 lunli. All rights reserved.
//

#ifndef public_hpp
#define public_hpp

#include <stdio.h>

#ifndef public_cplusplus
#define public_cplusplus

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

#endif

#endif /* public_hpp */
