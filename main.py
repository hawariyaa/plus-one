# question is to plus one to the number given in the array
# example is [1 , 2, 3]   will be [1, 2, 4]
# [9]  [1, 0]

lass Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1] # here we are going to reverse the integer digit array
        one, i = 1, 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                   digits[i] += 1
                   one = 0
            else:
               digits.append(1)
                one = 0
            i += 1
            return digits[::-1]

