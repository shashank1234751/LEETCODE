/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let mini=Infinity;
    let diff=0;
    let curr;
    for(let n of prices){
        mini=Math.min(mini,n)
        curr=n-mini
        diff=Math.max(diff,curr)
    }
    return diff
};