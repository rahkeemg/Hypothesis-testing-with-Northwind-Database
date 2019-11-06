import numpy as np
import scipy.stats as scs
from statsmodels.stats.power import tt_ind_solve_power


def bootstrap_sampling(n=50, pop=None, samp_size=50, replace=True):
    """bootstrap_sampling [summary]
        This function is designed to generate random bootstrap samples with replacements.
    
    Keyword Arguments:
        n {int} -- The amount of samples to generate (default: {50})
        population {[numpy array]} -- This is the population to create random samples from (default: {None})
        samp_size {int}  -- The size/amount of items in the random samples generated (default: {50})
        replace {bool}  -- Flag to determine if the samples should be created with replacements or not
    """
    
    sample_size = samp_size  # sample size
    sample_means = []

    # Bootstrap simulation for sample population of n
    for i in range(n):
        sample = np.random.choice(pop, size=sample_size, replace=replace)
        sample_means.append(np.mean(sample))

    # Recast the sample mean lists as numpy arrays
    return np.array(sample_means)

def normality_test_shapiro(x):
    t, p = scs.shapiro(x)
    if p < 0.05:
        print(f"p = {p}\nTherefore the data is NOT normal")
        return False
    print(f"p = {p}\nTherefore the data is normal")
    return True


def test_equal_variances(x1, x2):
    """
    h0: var_x1 = var_x2
    ha: var_x1 != var_x2
    """
    t, p = scs.levene(x1, x2)
    if p < 0.05:
        print(f"p = {p}\nTherefore the data DOES NOT have equal variances")
        return False
    print(f"p = {p}\nTherefore the data HAS equal variances")
    return True

