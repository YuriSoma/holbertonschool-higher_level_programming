#!/usr/bin/python3
"""Defines function that fetches posts"""
import csv
import requests


def fetch_and_print_posts():
    """function fetches and prints"""

    try:
        res = requests.get("https://jsonplaceholder.typicode.com/posts")
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    print("Status Code: {}".format(res.status_code))

    if res.headers.get("Content-Type") == "application/json; charset=utf-8":
        json_data = res.json()
        for post in json_data:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them in a csv file.
    """

    try:
        res = requests.get("https://jsonplaceholder.typicode.com/posts")
    except Exception as e:
        print("Failed to retrieve data")
        return

    json_data = res.json()

    cf = "posts.csv"

    filtered_data = [
        {key: post[key] for key in ('id', 'title', 'body')}
        for post in json_data]

    headers = ['id', 'title', 'body']

    with open(cf, "w", newline="") as file:
        csv_write = csv.DictWriter(file, fieldnames=headers)
        csv_write.writeheader()
        csv_write.writerows(filtered_data)
