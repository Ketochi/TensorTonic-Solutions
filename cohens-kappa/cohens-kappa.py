def cohens_kappa(a,b):
    agreement = sum(1 for y,n in zip(a,b) if y==n)
    length = len(a)
    Po = agreement/length

    categories = set(a) | set(b)
    Pe = sum((a.count(c)/length)*(b.count(c)/length) for c in categories)
    try:
        k = (Po-Pe)/(1-Pe)
        return (k)
    except ZeroDivisionError:
        return(1)