# Build Order:
# You are give a list of projects and a list of dependencies (Which is a list
# of pair of projects, where the second one is dependent on the first project). All projects
# dependencies must be build before before the project is.
# Find a build order that will allow the project to be built.
# If there is no valid, return an error

# Input:
# a: f
# b: f
# c: 
# d: a, b, c
# e:
# f: 
#
# Output: f, e, a, b, d, c
#
# Invalid Options: cycle dependency, dependency doesn't exists
#
# Best starting options: Projects with no dependencies

import os
import sys

projects = {
    'a': ['f'],
    'b': ['f'],
    'c': [],
    'd': ['a', 'b', 'c'],
    'e': ['f'],
    'f': ['e']
    }


def get_projects_with_no_dependency(projects):
    ready_to_run = [key for key,val in projects.iteritems() if not val]
    map(projects.pop, ready_to_run)
    return ready_to_run

def run_project(project, projects):
    projects_with_dependecy = [key for key,val in projects.iteritems() if project in val]
    for dependency in projects_with_dependecy:
        projects[dependency].remove(project)
    print project

if __name__ == '__main__':
    ready_to_run = get_projects_with_no_dependency(projects)

    if not ready_to_run:
        print 'Circle dependency detected'

    while ready_to_run:
        run_project(ready_to_run.pop(0), projects)
        unblocked = get_projects_with_no_dependency(projects)
        if not unblocked:
            print 'Circle dependency detected'
            break
        ready_to_run.extend(unblocked)
            
