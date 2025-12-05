

import os

# Instructions (Free version simple fix)
instructions = "Fix basic syntax errors and replace tabs with 4 spaces."

# Files / folders to ignore
ignore_dirs = ["node_modules", ".git"]

for root, dirs, files in os.walk("."):
    # Ignore node_modules and .git
    dirs[:] = [d for d in dirs if d not in ignore_dirs]

    for file in files:
        # JS & JSON files fix
        if file.endswith(".js") or file.endswith(".json"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()

            # Simple free fix: tabs → 4 spaces
            fixed_code = code.replace("\t", "    ")

            # Write back fixed code
            with open(path, "w", encoding="utf-8") as f:
                f.write(fixed_code)

print("✅ AI code fix completed for JS/JSON files (Free version)")
