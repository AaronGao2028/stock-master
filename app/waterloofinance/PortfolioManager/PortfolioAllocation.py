def allocate_portfolio (cov_matrix, portfolio):
    sum = 0
    for i in range (len(cov_matrix)):
        for j in range(len(cov_matrix[i])):
            sum = sum + cov_matrix[i][j]
            
    for i in range(len(portfolio)):
        sum_temp = 0
        for j in range(len(cov_matrix[i])):
            sum_temp = cov_matrix[i][j] + sum_temp
        portfolio[i].allocation = sum_temp/sum
        
    return portfolio