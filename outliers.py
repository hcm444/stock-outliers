# function for detecting outliers
def indentify_outliers(row, n_sigmas=3):
    if (row['simple_rtn'] > row['mean'] + 3 * row['std']) or (row['simple_rtn'] < row['mean'] - 3 * row['std']):
        # x > μ + 3σ or x < μ - 3σ
        return 1
    else:
        return 0
