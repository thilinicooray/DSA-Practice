
def needle_in_heystack(haystack, needle):

    if not haystack or len(needle) > len(haystack):
        return -1
    if not needle:
        return 0

    r = 0

    while r < len(haystack):

        if haystack[r] == needle[0]:


            if haystack[r: r+len(needle)] == needle:
                return r

        r += 1

    return -1

print(needle_in_heystack('abccny','ny'))


