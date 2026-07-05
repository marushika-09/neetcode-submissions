import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  
        if cleaned_text==cleaned_text[::-1]:
            return True
        return False    