import numpy as np
import scipy.stats as stats


def cohen_d(group1, group2):
    """
    Compute Cohen's d for effect size

        group1: Series or NumPy array
        group2: Series or NumPy array

        returns a floating point number 
    """
    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()

    # Calculate the pooled threshold as shown earlier
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)

    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)

    return d


def welch_t(a, b):
    """ Calculate Welch's t statistic for two samples. """

    numerator = a.mean() - b.mean()

    # “ddof = Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof,
    #  where N represents the number of elements. By default ddof is zero.

    denominator = np.sqrt(a.var(ddof=1)/a.size + b.var(ddof=1)/b.size)

    return np.abs(numerator/denominator)


def welch_df(a, b):
    """ 
    Calculate the effective degrees of freedom for two samples. This function returns the degrees of freedom 
    :params:
        a & b:
            These are the two samples currently being observed
    :return:
        Returns the Welches Degrees of Freedom for the samples observed    
    """

    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size

    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1 / n1)**2/(n1 - 1) + (s2 / n2)**2/(n2 - 1)

    return numerator/denominator


def p_value_welch_ttest(a, b, two_sided=False):
    """Calculates the p-value for Welch's t-test given two samples.
    By default, the returned p-value is for a one-sided t-test. 
    Set the two-sided parameter to True if you wish to perform a two-sided t-test instead.
    """
    t = welch_t(a, b)
    df = welch_df(a, b)

    p = 1-stats.t.cdf(np.abs(t), df)

    if two_sided:
        return 2*p
    else:
        return p
