# You Can Fix Me

A practical alternative to LeetCode-style interviews, focusing on real-world debugging and code maintenance skills.

## What is this?

"You Can Fix Me" provides a collection of realistic coding problems that simulate everyday programming scenarios. Instead of implementing algorithms from scratch, you'll work with existing code to identify and fix bugs—a skill that's more relevant to day-to-day development work.

## How it Works

Each problem consists of three key files:
- **fix_me.py**: Contains broken code that you need to fix
- **test_me.py**: Contains tests to verify your solution
- **metadata.json**: Contains problem information and metadata

Problems are organized by programming language and assigned unique identifiers. For example:
```
python/
├── py_001_that_doesnt_add_up/
│   ├── py_001_fix_me.py
│   ├── py_001_test_me.py
│   └── py_001_metadata.json
├── py_002_flippin_wreck/
│   ├── py_002_fix_me.py
│   ├── py_002_test_me.py
│   └── py_002_metadata.json
└── py_003_even_the_odds/
    ├── py_003_fix_me.py
    ├── py_003_test_me.py
    └── py_003_metadata.json
```

## Getting Started

### Option 1: Clone the entire repository
```bash
git clone https://github.com/yourusername/you-can-fix-me.git
cd you-can-fix-me
```

### Option 2: Download a specific folder (for a single language)
You can use sparse checkout to download only a specific folder:

```bash
mkdir you-can-fix-me
cd you-can-fix-me
git init
git remote add origin https://github.com/yourusername/you-can-fix-me.git
git config core.sparseCheckout true
echo "python/" >> .git/info/sparse-checkout  # Replace "python" with the language you want
git pull origin main
```

## How to Solve Problems

1. Navigate to the problem folder you want to solve
2. Open the `fix_me.py` file (or equivalent in your language)
3. Read the problem description in the comments
4. Fix the code inside the function without modifying any code outside the function
5. Run the `test_me.py` file to verify your solution:
   ```bash
   cd python/py_001_that_doesnt_add_up
   python py_001_test_me.py
   ```
6. If the test returns `True`, congratulations! You've fixed the bug correctly

## Contributing

We welcome contributions! If you'd like to add a new problem:

1. Follow the existing folder structure and naming convention
2. Create a new folder with a unique ID in the appropriate language directory
3. Include the three required files:
   - `xxx_fix_me.py`: Contains the buggy code with detailed comments explaining the problem
   - `xxx_test_me.py`: Contains tests to verify the solution
   - `xxx_metadata.json`: Contains problem metadata including difficulty, tags, and description
4. Make sure your problem has a clear bug that can be fixed without modifying test code
5. Submit a pull request with your new problem

## Available Problems

Currently, the repository contains problems for:
- Python

Support for other languages is coming soon.

## License

This project is licensed under the "You Can Fix Me Prosperity License". See the [LICENSE](./LICENSE) file for details.

The license allows free use for individuals and educational purposes but restricts commercial use without permission.
