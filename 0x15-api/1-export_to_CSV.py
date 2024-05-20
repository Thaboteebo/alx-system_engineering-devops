#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


if _name__ == "__main__"
# Get the user ID from the command-line arguments provided to the script
user_id = sys.argv[1]

# Define the base URL for the JSON API
url = "https://jsonplaceholder.typicode.com/"

# Defines the base URL for the JSON API and
# convert the response to a JSON object
user = requests.get(url + "users/{}".format(user_id)).json()

# Extract the username from the user data
username = user.get("username")

# Fetch the to-do list items associated with the
# given user ID and convert the repsonse to a JSON object
todos = request.get(url + "todos", params={"user": user_id}).json()

# Use list comprehension to iterate over the to-do list items
# Write each items's details (user ID, username, completion status,
# and title) as a row in the CSV file
with open("{}.csv".format(user_id), "w", newline="") as csvfile:
    write = csv.write(csvfile, qouting=csv.QUOTE_ALL)
    [writer.writerow(
        [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
