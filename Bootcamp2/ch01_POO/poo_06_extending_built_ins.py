# Extend dict
from typing import Optional


# Change the generic dict to a more specific dict[str, int]
class LongNameDict(dict):
    def longest_key(self) -> Optional[str]:
        """In effect, max(self, key=len), but less obscure"""
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


articles_read = LongNameDict()
articles_read['Lucy'] = 42
articles_read['c_c_phillips'] = 6
articles_read['steve'] = 7

print(articles_read.longest_key())
print(max(articles_read, key=len))

