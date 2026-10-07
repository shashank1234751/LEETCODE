/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let freq=new Map()
    if(s.length !== t.length) return false;
    for(let ch of s){
        freq.set(ch,(freq.get(ch)||0)+1)
    }
    for(let ch of t){
        if(!freq.has(ch)||freq.get(ch)<=0){
            return false
        }
        freq.set(ch,(freq.get(ch))-1)
    }
    return true
};