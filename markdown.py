import sys
from marks import marks
import re

markdown_file = sys.argv[1]
output_file = re.sub('.md', '.html', sys.argv[1])
count_marks = 0
current_mark = ""

def increment(s, inc):
    """ Take given [s] string and icrement all the numbers
    in this string by [inc] number """
    return s.replace(str(1), str(inc))


def substring_after(s1, s2):
    """ Find given string [s1] in a string second given string [s2] and return
        everything what is after this string in a line"""
    return s1.partition(s2)[2]


# Render file based on markdown file

with open(markdown_file, "rt") as markdown:
    with open(output_file, "wt") as out:
        for line in markdown:
            output = line

            for i in range(0, len(list(marks))):
                # if re.search(r'\b'+list(marks)[i] + '\b', line):
                if line.startswith(list(marks)[i]):
                    output = substring_after(line, list(marks)[i])
                    # if current_mark != list(marks)[i]:
                    #     count_marks = 0
                    # current_mark = list(marks)[i]
                    count_marks += 1

                    # [Key index],["code block"]
                    before = marks.get(list(marks)[i])[0]
                    before = increment(before, count_marks)

                    after = marks.get(list(marks)[i])[1]
                    after = increment(after, count_marks)

                    output = before + output + after
                    out.write(output)

# Concatenate files

filenames = ['source/start.html', 'tmp/output', 'source/end.html']
with open('index.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
