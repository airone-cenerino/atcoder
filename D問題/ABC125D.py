n = int(input())
a = list(map(int, input().split()))  # �������l�����X�g�Ɋi�[
ans = 0

a.sort()
num = 0
#  �}�C�i�X�̌��������Ȃ�S�����ɂ��Ęa���Ƃ�
# ��Ȃ�S�������ɂ��Đ�Βl�������������

for i in range(n):
    if a[i] < 0:
        num += 1

# num�̓}�C�i�X�̐�
a = list(map(abs, a))
if num % 2 == 0:
    print(sum(a))
else:
    a.sort()
    print(sum(a) - a[0]*2)
