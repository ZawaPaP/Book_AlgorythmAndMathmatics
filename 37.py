Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

def cross (ax, ay, bx, by):
    return ax * by - ay * bx

#cross(AB, AC)
ans1 = cross(Bx - Ax, By - Ay, Cx - Ax, Cy - Ay)
#cross(AB, AD)
ans2 = cross(Bx - Ax, By - Ay, Dx - Ax, Dy - Ay)
#cross(CD, CA)
ans3 = cross(Dx - Cx, Dy - Cy, Ax - Cx, Ay - Cy)
#cross(CD, CB)
ans4 = cross(Dx - Cx, Dy - Cy, Bx - Cx, By - Cy)

if ans1 == 0 and ans2 == 0 and ans3 == 0 and ans4 == 0:
    A = (Ax, Ay)
    B = (Bx, By)
    C = (Cx, Cy)
    D = (Dx, Dy)
    if A > B:
        tmp = B
        B = A
        A = tmp
    if C > D:
        tmp = D
        D = C
        C = tmp
    if max(A, C) <= min(B, D):
        print("Yes")
    else:
        print("No")

else:
    IsAB = False
    IsCD = False
    if ans1 >= 0 and ans2 <= 0:
        IsAB = True
    if ans1 <= 0 and ans2 >= 0:
        IsAB = True
    if ans3 >= 0 and ans4 <= 0:
        IsCD = True
    if ans3 <= 0 and ans4 >= 0:
        IsCD = True

    if IsAB == True and IsCD == True:
        print("Yes")
    else:
        print("No")
