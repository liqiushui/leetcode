/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    let dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    for(let i = 1; i <= amount; i++) {
        for(let coin of coins) {
            if(i - coin >= 0 ) {
                //dp[i - coin]： 当前面额i减当前硬币价值所需要的最少硬币
                //dp[i] 可由 dp[i - coin] + 1 转换而来
                dp[i] = Math.min(dp[i - coin] + 1, dp[i]);
            }
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
};