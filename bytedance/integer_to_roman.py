class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        m = num // 1000
        if m > 0:
            s += 'M' * m
        num %= 1000
        if num >= 900:
            s += 'CM'
            num -= 900
        elif num >= 500:
            num -= 500
            c = num // 100
            num %= 100
            s += 'D' + c * 'C'
        elif num >= 400:
            num -= 400
            s += 'CD'
        else:
            c = num // 100
            s += c * 'c'
            num %= 100
        
        if num >= 90:
            num -= 90
            s += 'XC'
        elif num >= 50:
            num -= 50
            x = num // 10
            num %= 10
            s += 'L' + x * 'X'
        elif num >= 40:
            num -= 40
            s += 'XL'
        else:
            x = num // 10
            num %= 10
            s += x * 'X'
        
        if num == 9:
            return s + 'IX'
        if num >= 5:
            num -= 5
            return s + 'V' + num * 'I'
        if num == 4:
            return s + 'IV'
        return s + num * 'I'