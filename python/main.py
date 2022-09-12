from typing import Set, Tuple

# algorithm on page 76 when joining two tables
def join(r1 : Set[Tuple[str, int]], r2: Set[Tuple[int, str]]) -> Set[Tuple[str,int,str]]:
    r = set()
    for s in r1:
        for t in r2:
            if s[1] == t[0]:
                r.add((s[0],s[1],t[1]))


    return r

# main program
if __name__ == "__main__":
    students = { ('Harry', 1), ('Hermione', 2), ('Ron', 3), ('Draco', 4)}
    enrollments = { (1, 'P140'), (2, 'DA101'), (1, 'DA101'), (3, 'P140')}

    # resulting join
    result = join(students,enrollments)
    print(result)
