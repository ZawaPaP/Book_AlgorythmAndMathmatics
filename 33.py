import math
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

#BA, BCの内積が負の場合、BAが最短
#CA, CBの内積が負の場合、CAが最短
#それ以外、外積を使って平行四辺形の面積で求める

BAx = ax - bx
BAy = ay - by
BCx = cx - bx
BCy = cy - by
CAx = ax - cx
CAy = ay - cy
CBx = bx - cx
CBy = by - cy

if (BAx * BCx + BAy * BCy) < 0:
    print(math.sqrt(BAx**2 + BAy**2))
elif (CAx * CBx + CAy * CBy) < 0:
    print(math.sqrt(CAx**2 + CAy**2))
else:
    tmp = abs(BAx * BCy - BAy * BCx)
    BC_size = math.sqrt(BCx**2 + BCy**2)
    print(tmp / BC_size)
