/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s=s.trim()
    s = s.toLowerCase().replace(/[^a-z0-9]/g, "");
    let left=0
    let right=s.length-1
    while(right>left){
        if(s[right]!==s[left]){
            return false
        }
        right-=1
        left+=1
    }
    return true 
};