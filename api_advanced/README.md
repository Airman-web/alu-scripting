# API Advanced - Reddit API

This project contains Python scripts that interact with the Reddit API to fetch and process data from various subreddits. The project focuses on API fundamentals including pagination, recursive calls, JSON parsing, and data sorting.

## Learning Objectives

By completing this project, you will learn:

- How to read API documentation to find the endpoints you need
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value
- How to handle API rate limits and authentication requirements

## Requirements

### General
- **Editors**: vi, vim, emacs
- **OS**: Ubuntu 14.04 LTS
- **Python Version**: 3.4.3
- All files must end with a new line
- First line of all files: `#!/usr/bin/python3`
- Libraries must be imported in alphabetical order
- Code must follow PEP 8 style guidelines
- All files must be executable
- All modules must have documentation

### Dependencies
- **requests** module (for HTTP requests)

```bash
pip3 install requests
```

## Project Structure

```
api_advanced/
├── README.md
├── 0-subs.py          # Task 0: Get subscriber count
├── 1-top_ten.py       # Task 1: Get top 10 hot posts
├── 2-recurse.py       # Task 2: Recursively get all hot posts
├── 3-count.py         # Task 3: Count keyword occurrences
├── 0-main.py          # Test file for Task 0
├── 1-main.py          # Test file for Task 1
├── 2-main.py          # Test file for Task 2
└── 3-main.py          # Test file for Task 3
```

## Tasks

### Task 0: How many subs?
**File**: `0-subs.py`

Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit.

**Prototype**: `def number_of_subscribers(subreddit)`

**Usage**:
```bash
python3 0-main.py programming
# Output: 756024

python3 0-main.py this_is_a_fake_subreddit
# Output: 0
```

**Key Features**:
- Returns total subscribers count
- Returns 0 for invalid subreddits
- Does not follow redirects

---

### Task 1: Top Ten
**File**: `1-top_ten.py`

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

**Prototype**: `def top_ten(subreddit)`

**Usage**:
```bash
python3 1-main.py programming
# Output: Prints 10 post titles

python3 1-main.py this_is_a_fake_subreddit
# Output: None
```

**Key Features**:
- Prints titles of first 10 hot posts
- Prints "None" for invalid subreddits
- Does not follow redirects

---

### Task 2: Recurse it!
**File**: `2-recurse.py`

Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

**Prototype**: `def recurse(subreddit, hot_list=[])`

**Usage**:
```bash
python3 2-main.py programming
# Output: 932 (total number of hot posts)

python3 2-main.py this_is_a_fake_subreddit
# Output: None
```

**Key Features**:
- Uses recursion (no loops!)
- Implements pagination using Reddit's `after` parameter
- Returns complete list of all hot post titles
- Returns None for invalid subreddits

---

### Task 3: Count it!
**File**: `3-count.py`

Write a recursive function that queries the Reddit API, parses titles of all hot articles, and prints a sorted count of given keywords.

**Prototype**: `def count_words(subreddit, word_list)`

**Usage**:
```bash
python3 3-main.py programming 'python java javascript scala'
# Output:
# java: 27
# javascript: 20
# python: 17
# scala: 4

python3 3-main.py programming 'JavA java'
# Output:
# java: 54
```

**Key Features**:
- Uses recursion with pagination
- Case-insensitive keyword matching
- Counts word occurrences (not just title occurrences)
- Sums duplicate keywords
- Sorts by count (descending), then alphabetically (ascending)
- Ignores punctuation at word boundaries
- Prints nothing for invalid subreddits or no matches

---

## Important Implementation Notes

### Reddit API Considerations

1. **User-Agent Header**: Must set a custom User-Agent to avoid rate limiting
   ```python
   headers = {'User-Agent': 'Mozilla/5.0 (compatible; API-Practice/1.0)'}
   ```

2. **No Redirects**: Use `allow_redirects=False` to properly detect invalid subreddits
   ```python
   response = requests.get(url, headers=headers, allow_redirects=False)
   ```

3. **Pagination**: Reddit API uses the `after` parameter for pagination
   ```python
   params = {'after': after_value, 'limit': 100}
   ```

4. **Rate Limiting**: Reddit has rate limits. The custom User-Agent helps, but avoid making too many requests too quickly.

### API Endpoints Used

- **Subreddit Info**: `https://www.reddit.com/r/{subreddit}/about.json`
- **Hot Posts**: `https://www.reddit.com/r/{subreddit}/hot.json`

## Usage Examples

### Make files executable:
```bash
chmod +x 0-subs.py 1-top_ten.py 2-recurse.py 3-count.py
```

### Run the scripts:
```bash
# Task 0
./0-subs.py programming

# Task 1
./1-top_ten.py programming

# Task 2
./2-recurse.py programming

# Task 3
./3-count.py programming 'python java javascript'
```

### Or with main files:
```bash
python3 0-main.py programming
python3 1-main.py programming
python3 2-main.py programming
python3 3-main.py programming 'python java'
```

## Troubleshooting

### "Too Many Requests" Error
- Ensure you're setting a custom User-Agent header
- Add delays between requests if necessary
- Check Reddit's rate limiting documentation

### Invalid Subreddit Returns Wrong Results
- Make sure `allow_redirects=False` is set
- Check that you're handling 404 and redirect status codes properly

### Recursion Issues
- Ensure you're not using loops for Tasks 2 and 3
- Check that your base case properly handles the `after` parameter being None
- Verify pagination is working correctly

## Resources

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String Parameters](https://en.wikipedia.org/wiki/Query_string)
- [Python Requests Module](https://docs.python-requests.org/)
- [PEP 8 Style Guide](https://pep8.org/)

## Author

**Project**: API Advanced  
**Institution**: ALU  
**Course**: Web Infrastructure  
**Weight**: 1

## License

This project is part of the ALU curriculum.

---

**Repository**: `alu-scripting`  
**Directory**: `api_advanced`