class Solution:
    def isNumber(self, s: str) -> bool:
        # ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

        digit, symbol, exp, dec = False, False,False,False
        for c in s:
            if c in '0123456789':
                digit = True
            elif c in '+-':
                if digit or dec or symbol:
                    return False
                else:
                    symbol = True
            elif c in 'eE':
                if not digit or exp:
                    return False
                else:
                    exp = True
                    digit = False
                    symbol = False
                    dec = False
            elif c in ".":
                if dec or exp:
                    return False
                else:
                    dec = True
            else:
                return False
        return digit        
