Whenever you want to check on the current status of things, you may use:
```bash
git status
```

After making changes to your files, you first must *stage* changes using:
```bash
git add .
```
- Using the `.` in the above line means add everything in the current directory (this is like clicking the big + on VS Code's interface)

After everything is staged, you must *commit* with a message using:
```bash
git commit -m "[commit message]"
```
- **Note** you must change the text within the quotations to reflect the changes you made

Finally, to send the changes to the GitHub page, use:
```bash
git push
```