# 3 无重复字符的最长子串
def lengthOfLongestSubstring(self, s: str) -> int:
    last_appear_dict = {}
    cur_start = 0
    length = 0
    for cur_end, a in enumerate(s):
        # print(last_appear_dict)
        if a in last_appear_dict:
            cur_start = max(cur_start, last_appear_dict[a]) # 比较当前start和字典里面的start位置
        # print("cur_start", cur_start, "end", cur_end)
        length = max(length, (cur_end - cur_start + 1))
        # print("length", length)
        # TODO 注意这里 + 1 字典里面存储的start位置是重复值的后一位
        last_appear_dict[a] = cur_end + 1
    return length

# 5. 最长回文子串
def longestPalindrome(s: str) -> str:
    # 边界条件判断
    if len(s) < 2:
        return s
    start_ind = 0
    longest_length = 0
    string_length = len(s)
    for i in range(string_length):
        # 如果剩余字串长度小于目前找到的最长回文子串的长度，直接种植循环
        if string_length - i <= longest_length / 2:
            break
        left = i
        right = i
        # 如果右侧有值和当前值一样，直接过滤掉
        while(right < string_length -1) and s[right + 1] == s[right]:
            right += 1
        i = right + 1
        # 向两边判断
        while (right < string_length - 1) and left > 0 and s[right+1] == s[left-1]:
            right += 1
            left -= 1
            print(left, right, s[left])
        # 判断是否比现在的长
        if right - left + 1 > longest_length:
            start_ind = left
            longest_length = right - left + 1
    return s[start_ind : start_ind + longest_length]

# 7. 整数反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
def reverse(x: int) -> int:
    y = [1, -1][x < 0] * int(str(abs(x))[::-1])
    return y if y.bit_length() < 32 else 0


if __name__ == '__main__':

    print(longestPalindrome(s='babad'))
    print(longestPalindrome(s='aaa'))