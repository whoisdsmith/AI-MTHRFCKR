# GitHub Action_ Markdown Lint

## USER

Create a Github action to

1. lint only markdown files.
2. Check for broken links in the README.md file and move broken links to a new markdown file.

## ASSISTANT

To create a GitHub action that lints markdown files and checks for broken links, you can follow these steps:

1. Create a new folder in your repository named `.github` and inside that folder create another folder named `workflows`.
2. In the `workflows` folder, create a new file named `markdown_lint_and_links_check.yml`.
3. Paste the following content into the `markdown_lint_and_links_check.yml` file:

```yaml
name: Markdown Lint and Broken Links Check

on:
  push:
    branches:
      - main
      - master
  pull_request:
    branches:
      - main
      - master
    paths:
      - '**.md'

jobs:
  markdown-lint:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: 16

    - name: Install and run markdownlint
      run: |
        npm install -g markdownlint-cli
        markdownlint "**/*.md"

  broken-links-check:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Install and run broken-link-checker
      run: |
        sudo apt-get install -y nodejs npm
        npm install -g broken-link-checker
        blc https://github.com/${{ github.repository }}/blob/${{ github.sha }}/README.md -ro --exclude '*.md' --get --filter-level 3 | tee broken_links.log || true

    - name: Move broken links to new markdown file
      run: |
        if [ -s broken_links.log ]; then
          echo "# Broken Links" > broken_links.md
          echo "" >> broken_links.md
          cat broken_links.log | grep 'BROKEN' | awk '{print $1}' | sort | uniq | sed 's/^/- /' >> broken_links.md
          git config --global user.name 'GitHub Actions Bot'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add broken_links.md
          git commit -m "Move broken links to a new markdown file"
          git push
        fi
```

This GitHub action will be triggered on push and pull requests to the `main` and `master` branches. It lints markdown files and checks for broken links in the `README.md` file. If any broken links are found, they will be moved to a new markdown file named `broken_links.md`.

The workflow consists of two jobs:

1. `markdown-lint`: Lints all markdown files except `README.md` using `markdownlint-cli`.
2. `broken-links-check`: Checks for broken links in the `README.md` file using `broken-link-checker` and moves them to a new markdown file.

Remember to replace `main` and `master` with the appropriate branch names if your default branch is different.
