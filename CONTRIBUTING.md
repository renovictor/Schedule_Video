# Contributing to Video Recorder

First off, thank you for considering contributing to Video Recorder! It's people like you that make Video Recorder such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs if possible**
* **Include your environment details** (OS, Python version, app version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and the expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Follow the Python styleguides
* Include appropriate test cases
* Document new code based on the Documentation Styleguide
* End all files with a newline

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji:
  - 🎨 `:art:` when improving the format/structure of the code
  - 🐛 `:bug:` when fixing a bug
  - 📚 `:books:` when writing docs
  - 🎯 `:dart:` when improving performance
  - ✨ `:sparkles:` when adding a new feature
  - 🗑️ `:wastebasket:` when removing code/files

### Python Styleguide

* Use Python 3.8+ syntax
* Follow PEP 8 guidelines
* Use meaningful variable and function names
* Add comments for complex logic
* Use docstrings for functions and classes
* Maximum line length of 100 characters

Example:
```python
def function_name(param1, param2):
    """
    Clear description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    """
    # Implementation
    pass
```

### Documentation Styleguide

* Use Markdown
* Use clear, concise language
* Include code examples when helpful
* Keep documentation up to date with code changes

## Additional Notes

### Issue and Pull Request Labels

* `bug` - Something isn't working
* `enhancement` - New feature or request
* `documentation` - Improvements or additions to documentation
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed

## Getting Started with Development

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Video_Record.git
   cd Video_Record
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
5. Make your changes
6. Test your changes:
   ```bash
   python main.py
   ```
7. Commit your changes:
   ```bash
   git commit -m "🎨 Description of your changes"
   ```
8. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
9. Create a Pull Request

## Testing

Before submitting a pull request, please:

1. Test on Windows 11
2. Test with Python 3.8+
3. Test with different audio devices
4. Test with both camera and screen recording
5. Test the scheduling feature
6. Check for any error messages in the status log

## Project Structure

```
Video_Record/
├── main.py           # Entry point
├── gui.py            # GUI interface
├── capture.py        # Recording engine
├── scheduler.py      # Scheduling
├── requirements.txt  # Dependencies
└── .github/          # GitHub configuration
```

## Questions?

Feel free to open an issue or reach out if you have any questions!

Thank you for contributing! 🎉

