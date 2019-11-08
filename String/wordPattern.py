class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # 1
        
        str = str.split()
        return list(map(str.index, str)) == list(map(pattern.find, pattern))
    
        # 2
        
        str = str.split()
        a = zip(pattern, str)
        return len(str) == len(pattern) and len(set(a)) == len(set(str)) == len(set(pattern))