# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(A, B):
    A_len = len(A)
    B_len = len(B)
    if A == B:
        return EQUAL
    elif A_len < B_len:
        if A_len == 0:
            return SUBLIST
        else:
            for i in range (B_len - A_len + 1):
                j = 0
                while j < A_len and B[i + j] == A[j]:
                    j += 1
                if j == A_len:
                    return SUBLIST
            return UNEQUAL
    elif A_len > B_len:
        if B_len == 0:
            return SUPERLIST
        else:
            for i in range (A_len - B_len + 1):
                j = 0
                while j < B_len and A[i + j] == B[j]:
                    j += 1
                if j == B_len:
                    return SUPERLIST
            return UNEQUAL
    return UNEQUAL