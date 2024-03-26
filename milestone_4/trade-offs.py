def find_sum(target: int, li: list[int]) -> tuple[int, int]:
    for i in range(len(li)):
        for j in range (i+1, len(li)):
            if li[i] + li[j] == target:
                return (i, j)

print(find_sum(5, [1, 2, 3, 4, 5]))
# Time complexity: O(n^2), where n is the length of the input list; space complexity: O(1)


def find_sum_fast(target: int, li: list[int]) -> tuple[int, int]:
    seen = set()
    for i in range(len(li)):
        complement = target - li[i]
        if complement in seen:
            return li.index(complement), i
        seen.add(li[i])

print(find_sum_fast(5, [1, 2, 3, 4, 5]))
# Time complexity: O(n); space complexity: O(n), as a set 'seen' is used to store the elements of the input