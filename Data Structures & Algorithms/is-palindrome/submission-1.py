import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  
        left=0
        right=len(cleaned_text)-1

        while left<right:
            if cleaned_text[left]==cleaned_text[right]:
                left+=1
                right-=1
            else:    
                return False
        return True   