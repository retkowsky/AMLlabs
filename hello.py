# Very simple script to demonstrate run in environment
# Print message passed in as environment variable
import os

print(os.environ.get("MESSAGE"))
