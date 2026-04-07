def approximate_pi(n_terms):
  
    for n in range(n_terms):
        pi_approx = (-1)**n / (2*n + 1)
    pi_approx *= 4
    return pi_approx
