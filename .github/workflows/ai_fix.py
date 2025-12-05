import os

# Tumhare instructions (free version simple fix)
instructions = "Fix syntax errors and replace tabs with 4 spaces."

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):  # Python files
            path = os.path.join(root, file)
            with open(path, "r") as f:
                code = f.read()

            # Simple "AI-like" fix (free version)
            fixed_code = code.replace("\t", "    ")

            with open(path, "w") as f:
                f.write(fixed_code)

print("✅ AI code fix completed (Free version)")
