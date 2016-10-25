#!/usr/bin/python
"""
Predicts that a user will apply to the most popular jobs in his/her city, and
then to the most popular jobs in his/her state.

Takes about a minute to run.
"""

import csv
from collections import defaultdict as ddict

wd = "" # The directory that the data files are in

print "Recording job locations..."
job_info = {}
with open(wd + "jobs.tsv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t", 
    quoting=csv.QUOTE_NONE, quotechar="")
    reader.next() # burn the header
    for line in reader:
        (Jobid, WindowId, Title, Description, Requirements, City, State, 
        Country, Zip5, StartDate, EndDate) = line
        job_info[str(Jobid)] = [int(WindowId), State, City, 0]
        # The terminal zero is for an application count

print "Counting applications..."
with open(wd + "apps1.tsv") as infile:
    reader = csv.reader(infile, delimiter="\t")
    reader.next() # burn the header
    for line in reader:
        (UserId, WindowID, Split, ApplicationDate, JobId) = line
        job_info[JobId][3] += 1

print "Sorting jobs on based on popularity..."
top_city_jobs = ddict(lambda: ddict(lambda: ddict(list)))
top_state_jobs = ddict(lambda: ddict(list))
for (job_id, (window, State, City, count)) in job_info.items():
    top_city_jobs[window][State][City].append((job_id, count))
    top_state_jobs[window][State].append((job_id, count))
for window in [1, 2, 3, 4, 5, 6, 7]:
    for state in top_city_jobs[window]:
        for city in top_city_jobs[window][state]:
            top_city_jobs[window][state][city].sort(key=lambda x: x[1])
            top_city_jobs[window][state][city].reverse()
    for state in top_state_jobs[window]:
        top_state_jobs[window][state].sort(key=lambda x: x[1])
        top_state_jobs[window][state].reverse()

print "Making predictions..."
with open(wd + "users.tsv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t", 
    quoting=csv.QUOTE_NONE, quotechar="")
    reader.next() # burn the header
    with open("popular_jobs.csv", "w") as outfile:
        outfile.write("UserId, JobIds\n")
        for line in reader:
            (UserId, WindowId, Split, City, State, Country, ZipCode,
            DegreeType, Major, GraduationDate, WorkHistoryCount,
            TotalYearsExperience, CurrentlyEmployed, ManagedOthers,
            ManagedHowMany) = line
            if Split == "Train":
                continue
            top_jobs = top_city_jobs[int(WindowId)][State][City]
            if len(top_jobs) < 150:
                top_jobs += top_state_jobs[int(WindowId)][State]
            top_jobs = top_jobs[0:150]
            outfile.write(str(UserId) + "," + " ".join([x[0] for x in top_jobs]) + "\n")
