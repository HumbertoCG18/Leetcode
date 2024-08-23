# Length of the string A and the pattern B
N = len(A)
M = len(B)
        
# Create a DP table with dimensions (N+1) x (M+1)
# dp[i][j] will be True if A[0:i] matches B[0:j], otherwise False
dp = [[0] * (M + 1) for _ in range(N + 1)]
        
# Base case: An empty pattern matches an empty string
dp[0][0] = 1
        
# Initialize the first row of the DP table
# If B contains '*' at position j, it can potentially match an empty string
for j in range(1, M + 1):
    if B[j - 1] == '*':
            # '*' can represent zero occurrences of the preceding element
            dp[0][j] = dp[0][j - 2]

# Fill the DP table
for i in range(1, N + 1):
    for j in range(1, M + 1):
        # If the current character in B is '*'
        if B[j - 1] == '*':
            # '*' can match zero occurrences of the preceding element
            dp[i][j] = dp[i][j - 2]
                    
        # If the preceding character in B matches the current character in A
        # or if the preceding character in B is '.', '*' can match one or more occurrences
        if B[j - 2] == '.' or A[i - 1] == B[j - 2]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]

        # If the current character in B is '.' or matches the current character in A
        elif B[j - 1] == '.' or A[i - 1] == B[j - 1]:
            # Match the current character in A with the current character in B
            dp[i][j] = dp[i - 1][j - 1]
        
# Return whether the entire string A matches the entire pattern B
return dp[N][M]
        
        