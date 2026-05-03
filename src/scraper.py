import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_list = []

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    
    link = job.find("a", string="Apply")
    apply_link = link["href"] if link else "N/A"

    job_list.append([title, company, location, apply_link])

# Save to CSV
with open("jobs.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Company", "Location", "Apply Link"])
    writer.writerows(job_list)

print("Jobs saved successfully!")
