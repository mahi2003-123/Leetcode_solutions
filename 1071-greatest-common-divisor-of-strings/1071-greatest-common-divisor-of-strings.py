class Solution(object):
    def gcdOfStrings(self, str1, str2):

        # Take the smaller string
        if len(str1) < len(str2):
            small = str1
        else:
            small = str2

        # Try every prefix of the smaller string
        while len(small) > 0:

            if str1.replace(small, "") == "" and str2.replace(small, "") == "":
                return small

            # Remove the last character
            small = small[:-1]

        return ""