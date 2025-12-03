from collections import Counter

def minWindow(self, s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    # Count characters needed from t
    need = Counter(t)
    required = len(need)  # unique chars we need
    
    # Track what we have in current window
    have = 0  # unique chars with required count
    window = {}
    
    left = 0
    result = (float('inf'), 0, 0)  # (length, left, right)
    
    for right, char in enumerate(s):
        # Expand window
        window[char] = window.get(char, 0) + 1
        
        # Check if this char's count now satisfies requirement
        if char in need and window[char] == need[char]:
            have += 1
        
        # Contract window while valid
        while have == required:
            # Update result if smaller
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            # Remove leftmost char
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have -= 1
            left += 1
    
    return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]