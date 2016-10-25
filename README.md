# JobRecommendationKaggle
My solution for https://www.kaggle.com/c/job-recommendation/data

## Algorithm
Our approach will be to try to find how likely a user is to apply for a given job opening, taking into account the
factors:
* How well does the job description match the user profile(based on work experience)
* Demographic information, including – How geographically close is the user to the workplace
* Whether the user is likely to move(based on recent applications)
* Whether the user is currently interested in such jobs(based on recent applications)
* Whether users with similar qualifications are interested in the given opening
For measuring similarity beween qualifications and jobs, we will convert job descriptions and user qualifications to numerical form by using:
* A dictionary to estimate closeness in words
* The user job data to estimate which qualifications correspond to which jobs.
Geographical closeness can be determined using zipcodes.

##Deployment
Download data files apps.tsv, user_history.tsv, users.tsv, jobs.tsv from http://www.kaggle.com/c/job-recommendation/data in this folder

Use either of the commands

python new_apps_maker1.py
python new_apps_maker2.py
python new_apps_maker3.py

To generate the training and test data.
The first one does a 65:35 split with the first 65% examples in training.
The second one does a 50:50 split with the first 50% examples in training.
The third one does a 65:35 random split.

Run script.sh
The results will be written in the file "results"
