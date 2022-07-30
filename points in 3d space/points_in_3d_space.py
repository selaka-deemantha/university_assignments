def main():
    file_name = input("Enter the filename : ")
    file = open(file_name)
    content = file.read()
    points = []
    for i in content.split("\n"):
        points.append(i.split())
    return points


# [[1,2,3],[4,5,6],[7,8,9],[1,5,7]]

def is_colinear(pq, pr, ps):
    if (pq[0] / pr[0]) == (pq[1] / pr[1]) == (pq[2] / pr[2]) and (pq[0] / ps[0]) == (pq[1] / ps[1]) == (pq[2] / ps[2]):
        return True
    else:
        return False


def is_coplanar(pq, pr, ps):
    pr_x_ps = [(pr[1] * ps[2]) - (pr[2] * ps[1]), (pr[2] * ps[0]) - (pr[0] * ps[2]), (pr[0] * ps[1]) - (pr[1] * ps[0])]
    pq_dot_pr_x_ps = (pq[0] * pr_x_ps[0]) + (pq[1] * pr_x_ps[1]) + (pq[2] * pr_x_ps[2])
    if pq_dot_pr_x_ps == 0:
        return True
    else:
        return False


def coplaner_colinear_checker(l):
    pq = []
    pr = []
    ps = []
    for i in range(3):
        pq.append(l[1][i] - l[0][i])
        pr.append(l[2][i] - l[0][i])
        ps.append(l[3][i] - l[0][i])
    if is_colinear(pq, pr, ps):
        print("All points are colinear")
    else:
        if is_coplanar(pq, pr, ps):
            print("On the same plane")
        else:
            print("Not on the same plane")


coplaner_colinear_checker([[1, 2, 3], [4, 5, 5], [7, 8, 8], [6, 6, 1]])
