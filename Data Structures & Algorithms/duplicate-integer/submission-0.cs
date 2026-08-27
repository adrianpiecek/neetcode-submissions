public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> seen = new();
        foreach(int number in nums){
            if (!seen.Add(number)){
                return true;
            }
        }
        return false;
    }
}