class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        
        numArray = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                numArray[i + j] += digit
                numArray[i + j + 1] += (numArray[i + j] // 10)
                numArray[i + j] = numArray[i + j] % 10

        while numArray[-1] == 0:
            numArray.pop()

        numArray = numArray[::-1]
        answer = "".join(str(num) for num in numArray)

        return answer 