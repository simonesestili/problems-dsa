CHARS = set(ascii_letters + digits + '_')
CATEGORIES = set(("electronics", "grocery", "pharmacy", "restaurant"))
class Solution:
    def validateCoupons(self, code, business, active):
        return [c for b, c, a in sorted(zip(business, code, active)) if a and c and all(x in CHARS for x in c) and b in CATEGORIES]
