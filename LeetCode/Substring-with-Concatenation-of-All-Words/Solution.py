class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = {}

        # Count the frequency of each word
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        result = []

        # Check for each possible offset within word length
        for i in range(word_len):
            left = i
            curr_count = {}
            count = 0

            # Slide window
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    # If word count exceeds, move left pointer
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Check if all words matched
                    if count == len(words):
                        result.append(left)
                else:
                    # Reset window
                    curr_count.clear()
                    count = 0
                    left = j + word_len

        return result
