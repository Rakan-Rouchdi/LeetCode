class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        output = [0] * len(temperatures) # initialise our output array and set default to 0 
        stack = [] # append pair [temp, index]
        for i, temp in enumerate(temperatures): # loop through the temperatures and get the index and value
            while stack and temp > stack[-1][0]: # while stack is not empty and our current temp is bigger than the top of the stack and keep popping all the smaller temperatures 
                stackT, stackI = stack.pop(-1) # pop from the stack and unpack the values
                output[stackI] = i - stackI # calculate the difference in days which is difference in indexes
            stack.append([temp, i]) # add our temperature and index to the stack and it waits for a warmer day
        return output # return our output array




        