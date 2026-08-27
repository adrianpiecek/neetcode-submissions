public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length){return false;}

        Dictionary<char, int> map = new Dictionary<char, int>();

        for(int i=0; i<s.Length; i++){
            if(map.ContainsKey(s[i])){map[s[i]]++;continue;}
            map.Add(s[i],1);
        }
        for(int i=0; i<t.Length; i++){
            if(!map.ContainsKey(t[i])){return false;}
            map[t[i]]--;
        }
        foreach(int x in map.Values){
            if(x!=0){return false;}
        }
        return true;
    }
}
