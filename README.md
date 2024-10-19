# Python RegEx Practice

- `exercises-without-ans.py`: Exercises without answers.
- `exercises-with-ans.py`: My personal solutions to the exercises.

## Takeaways

- The `r` prefix on a string tells Python to treat the backslashes in the string as literal backslashes, rather than interpreting them as escape characters.
    - So instead writing `"\\d+"`, you can write `r"\d+"`

### Common Metacharacters

- `.`: Matches any character except a newline.
- `^`: Anchors the match at the start of the string.
- `$`: Anchors the match at the end of the string.
- `*`: Matches 0 or more repetitions of the preceding element.
- `+`: Matches 1 or more repetitions of the preceding element.
- `?`: Matches 0 or 1 occurrence of the preceding element.
- `{m,n}`: Matches between m and n occurrences of the preceding element.
- `[]`: Matches any character inside the brackets.
- `|`: Acts as an OR operator.
- `()`: Groups expressions and captures matching text.

### Basic Functions
- `re.match()`: Checks for a match only at the beginning of the string.
- `re.search()`: Searches for the first occurrence of the pattern anywhere in the string.
- `re.findall()`: Returns a list of all matches.
- `re.sub():`Replaces matches with a string.

### Matching a literal period

In regular expressions, the period (`.`) is a special metacharacter that matches any single character except a newline. So if you want to match a literal period, you must escape it with a backslash (`\.`).

*Note*: If you're putting a period inside square brackets, it will be treated as a literal character instead of as a metacharacter. 
This is why you don't need an escape character in this instance. Most metacharacters lose their meaning when they're in square brackets.