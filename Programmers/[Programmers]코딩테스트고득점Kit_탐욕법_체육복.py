def solution(n, lost, reserve):
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)
    for r_student in set_reserve:
        if r_student-1 in set_lost:
            set_lost.remove(r_student-1)
        elif r_student+1 in set_lost:
            set_lost.remove(r_student+1)
    return n - len(set_lost)