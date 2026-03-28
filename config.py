import os
from dotenv import load_dotenv
load_dotenv()

LANGUAGE_IDS = {
    "python": 71,
    "javascript": 63,
    "java": 62,
    "cpp": 54,
    "c": 50
}

RAPIDAPI_URL= "https://judge0-ce.p.rapidapi.com/submissions"
headers={
    "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
	"x-rapidapi-host": "judge0-ce.p.rapidapi.com",
	"Content-Type": "application/json"
}

PROBLEMS = [
    {
        "id": 1, "title": "Two Sum", "difficulty": "Easy", "tags": ["Array", "Hash Table"],
        "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.\n\n**Example:**\n```\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\n```",
        "starter_code": {
            "python": "import sys\nnums, target = sys.stdin.read().split('\\n')[:2]\nnums = list(map(int, nums.strip('[]').split(',')))\ntarget = int(target)\n\ndef two_sum(nums, target):\n    # Your code here\n    \nprint(two_sum(nums, target))",
            "javascript": "const lines = require('fs').readFileSync('/dev/stdin','utf8').trim().split('\\n');\nconst nums = JSON.parse(lines[0]);\nconst target = parseInt(lines[1]);\n\nfunction twoSum(nums, target) {\n    // Your code here\n}\nconsole.log(JSON.stringify(twoSum(nums, target)));",
            "java": "import java.util.*;\n\npublic class Main {\n    public static int[] twoSum(int[] nums, int target) {\n        // Your code here\n        return new int[]{};\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line = sc.nextLine().replaceAll(\"[\\\\[\\\\]]\", \"\");\n        int target = sc.nextInt();\n        String[] parts = line.split(\",\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++)\n            nums[i] = Integer.parseInt(parts[i].trim());\n        int[] result = twoSum(nums, target);\n        System.out.println(Arrays.toString(result));\n    }\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\n\nvector<int> two_sum(vector<int>& nums, int target) {\n    // Your code here\n    return {};\n}\n\nint main() {\n    string line;\n    getline(cin, line);\n    int target;\n    cin >> target;\n    vector<int> nums;\n    for (char& c : line) if (c == ',' || c == '[' || c == ']') c = ' ';\n    istringstream ss(line);\n    int x;\n    while (ss >> x) nums.push_back(x);\n    vector<int> result = two_sum(nums, target);\n    cout << \"[\" << result[0] << \", \" << result[1] << \"]\" << endl;\n}",
            "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nvoid two_sum(int* nums, int size, int target, int* out) {\n    // Your code here\n}\n\nint main() {\n    char line[256];\n    fgets(line, sizeof(line), stdin);\n    int target;\n    scanf(\"%d\", &target);\n    int nums[100], size = 0;\n    char* token = strtok(line, \"[],\\n \");\n    while (token) {\n        nums[size++] = atoi(token);\n        token = strtok(NULL, \"[],\\n \");\n    }\n    int out[2];\n    two_sum(nums, size, target, out);\n    printf(\"[%d, %d]\\n\", out[0], out[1]);\n}",
        },
        "test_cases": [
            {"input": "[2,7,11,15]\n9", "expected": "[0, 1]"},
            {"input": "[3,2,4]\n6",     "expected": "[1, 2]"},
        ]
    },
    {
        "id": 2, "title": "Longest Substring Without Repeating Characters", "difficulty": "Medium", "tags": ["String", "Sliding Window"],
        "description": "Given a string `s`, find the length of the longest substring without repeating characters.\n\n**Example:**\n```\nInput: \"abcabcbb\"\nOutput: 3\n```",
        "starter_code": {
            "python": "import sys\ns = sys.stdin.read().strip()\n\ndef length_of_longest_substring(s):\n    # Your code here\n    pass\n\nprint(length_of_longest_substring(s))",
            "javascript": "const s = require('fs').readFileSync('/dev/stdin','utf8').trim();\n\nfunction lengthOfLongestSubstring(s) {\n    // Your code here\n}\nconsole.log(lengthOfLongestSubstring(s));",
            "java": "import java.util.*;\n\npublic class Main {\n    public static int lengthOfLongestSubstring(String s) {\n        // Your code here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String s = sc.nextLine();\n        System.out.println(lengthOfLongestSubstring(s));\n    }\n}",
            "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint length_of_longest_substring(string s) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    string s;\n    getline(cin, s);\n    cout << length_of_longest_substring(s) << endl;\n}",
            "c": "#include <stdio.h>\n#include <string.h>\n\nint length_of_longest_substring(char* s) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    char s[1000];\n    fgets(s, sizeof(s), stdin);\n    s[strcspn(s, \"\\n\")] = 0;\n    printf(\"%d\\n\", length_of_longest_substring(s));\n}",
        },
        "test_cases": [
            {"input": "abcabcbb", "expected": "3"},
            {"input": "bbbbb",    "expected": "1"},
        ]
    }
]