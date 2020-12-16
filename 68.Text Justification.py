class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = {}
        cur_len = 0
        cur_line = 1
        for word in words:
            if cur_len + len(word) <= maxWidth:  # last word in a line does not have to have a space after that
                cur_len = cur_len + len(word) + 1  # each word has at least 1 space
                if cur_line in lines.keys():
                    lines[cur_line] = lines[cur_line] + " " + word
                else:
                    lines[cur_line] = word
            else:
                cur_len = len(word) + 1  # 1 space
                cur_line += 1
                lines[cur_line] = word  # +" "

        # now that we kow line for each word, we need to add spaces

        for key, line in lines.items():
            if key != cur_line:  # not the last line

                if len(line.split(" ")) - 1 != 0:  # devision by zero

                    extra = (maxWidth - len(line)) // (len(line.split(" ")) - 1)  # extra space that should be added between each 2 consecutive words
                    not_even = (maxWidth - len(line)) % (len(line.split(" ")) - 1)

                    if (extra > 0 or not_even > 0):
                        new_line = ""
                        tmp = line.split(" ")
                        for i in range(len(tmp) - 1):
                            new_line = new_line + tmp[i] + " " * (extra + 1)
                            if (not_even > 0):
                                new_line = new_line + " "
                                not_even -= 1
                        new_line = new_line + tmp[len(tmp) - 1]
                        lines[key] = new_line

                else:  # if there is only 1 word in the line, add extra spaces at the end of that word
                    new_line = line + " " * (maxWidth - len(line))
                    lines[key] = new_line



            else:  # last line
                line = line + " " * (maxWidth - len(line))
                lines[key] = line  # update line with required extra spaces


        return list(lines.values())




words=["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print (Solution().fullJustify(words , maxWidth))


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print (Solution().fullJustify(words , maxWidth))


words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print (Solution().fullJustify(words , maxWidth))
