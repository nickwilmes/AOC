import requests
import sys

from aocd import get_data


day = int(sys.argv[1])
year = 2020
session = "53616c7465645f5f1239837b0d3bf31f4cccf12a93785cf5c7f67b27d6332a26aa6d7dfa1b566a0b4b718a95dec0e6f2"

with open(f"day{day}.input", "w") as f:
    f.write(get_data(session = session, day = day, year = year))
print("Done")