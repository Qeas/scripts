with open('local.conf', 'r') as f:
    lines = f.readlines()
    lines.insert(1, 'REQUIREMENTS_BRANCH=refs/changes/27/454927/1')

with open('local.conf', 'w') as f:
    f.truncate(0)         # truncates the file
    f.seek(0)             # moves the pointer to the start of the file
    f.writelines(lines)
