def enrollment_stats(data):

    students = []
    tutions = []

    for u in data:
        students.append(u[1])
        tutions.append(u[-1])

    total_students = sum(students)
    total_tution = sum(tutions)

    students_mean = total_students // len(students)
    tutions_mean = total_tution // len(tutions)

    students_median = sorted(students)[len(students)//2]

    tutions_median = sorted(tutions)[len(tutions)//2]

    information = f"""

    **********************************

    Total Students: {total_students}
    Total tutions: {total_tution}

    Student Mean: {students_mean}
    Student Median: {students_median}

    Tution Mean: {tutions_mean}
    Tution Median: {tutions_median}

    **********************************

    """
    return information


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

print(enrollment_stats(universities))
