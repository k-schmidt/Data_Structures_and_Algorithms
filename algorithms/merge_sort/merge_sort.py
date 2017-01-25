class MergeSort:

    def __init__(self, values):
        self.values = values
        self.count = len(values)

    def sort(self):
        self.merge_sort(0, self.count - 1)
        return self.values

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            print(low, mid, high)
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        b = []
        i = low
        j = mid + 1

        print(i, j)
        while i <= mid and j <= high:
            if self.values[i] <= self.values[j]:
                b.append(self.values[i])
                i += 1
            else:
                b.append(self.values[j])
                j += 1

        while i <= mid:
            b.append(self.values[i])
            i += 1

        while j <= high:
            b.append(self.values[j])
            j += 1

        for index, val in enumerate(b):
            self.values[low + index] = val


def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1


def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = len(S) // 2
    S1 = S[:mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)


if __name__ == '__main__':
    ms = MergeSort([5, 3, 4, 2, 1])
    ms.sort()
    print(ms.values)
