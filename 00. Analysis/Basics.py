# Purpose of Analysis
# To solve any problem if we have multiple solutions then the best solution depends on two factors:
#  1. Time Complexity
#  2. Space Complexity

# Time Complexity
# TC(Program) = TC(Compilation) + TC(Running)

# Now, the Compilation Time is based on the compiler(software) which depends on the language in which it is written.
# Whereas, the Run Time is based on the processor (hardware) which depends on the type of processor.

# Types of Analysis:
# 1. Apstriary Analysis --> Depends on both : Language of the Compiler + Type of Processor 
#                           Exact answer
#                           Answers differ from system to system 
# 2. Apriori Analysis -->   Independent of both : Language of the Compiler + Type of Processor 
#                           Approximate answer
#                           Same answer from system to system 

# We will mainly focus on Apriori Analysis

# Apriori Analysis:
# It is the determination of the order of magnitude of the statement.

# # Example 1:

# x = 10 + 20
# print(x)
    
# # TC = O(1)  # Constant Time

# # Example 2:
# def main():
#     x = y + z --> Run once
#     for i in range(0, n): --> Run n times
#         x = y + z   
# # TC = O(n) 

