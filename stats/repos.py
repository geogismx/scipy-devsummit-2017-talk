# Use the GitHub API to get information on the usage
# of SciPy packages.
# KLOCs is inner source only (e.g. numpy/numpy), counted with 'sloccount'.
from pygithub3 import Github

gh = Github()

# name, user, repo, kloc
# kloc is the inner source (e.g. numpy/numpy) counted with sloccount
repositories = (
    ('matplotlib', 'matplotlib', 'matplotlib', 118),
    ('Nose', 'nose-devs', 'nose', 7),
    ('NumPy', 'numpy', 'numpy', 236),
    ('Pandas', 'pydata', 'pandas', 183),
    ('SciPy', 'scipy', 'scipy', 387),
    ('SymPy', 'sympy', 'sympy', 243)
)

unique_logins = set()
total_kloc = 0
print "Name\tKloc\tcommitters\tstars"
for (name, user, repo, kloc) in repositories:
    contributors = gh.repos.list_contributors(user=user, repo=repo)
    # get the repository object
    r = gh.repos.get(user=user, repo=repo)
    # all committers as login names
    logins = [l.login for l in contributors.all()]
    # update our running totals
    unique_logins.update(logins)
    total_kloc += kloc

    print "[{name}]({homepage})\t{kloc}\t{committers}\t{stars}".format(
        name=name, homepage=r.homepage, kloc=kloc,
        committers=len(logins), stars=r.stargazers_count)

print "Total:\n  {}K lines of code\n  {} contributors.".format(
    total_kloc, len(unique_logins))
