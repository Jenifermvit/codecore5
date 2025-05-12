import random
from typing import List
from parser import Frameglass

def same_order(frameglasses: List[Frameglass]) -> List[Frameglass]:
"""
Returns the frameglasses list as-is (original order).
"""
return frameglasses.copy()

def reverse_order(frameglasses: List[Frameglass]) -> List[Frameglass]:
"""
Returns the frameglasses list in reverse order.
"""
return list(reversed(frameglasses))

def random_order(frameglasses: List[Frameglass]) -> List[Frameglass]:
"""
Returns a randomly shuffled version of the frameglasses list.
"""
shuffled = frameglasses.copy()
random.shuffle(shuffled)
return shuffled

def order_by_tag_count(frameglasses: List[Frameglass]) -> List[Frameglass]:
"""
Returns the frameglasses list sorted by number of tags (descending).
"""
return sorted(frameglasses, key=lambda fg: len(fg.tags), reverse=True)