#import the modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
student = pd.read_csv("student.csv")
check = pd.isnull(student["AnnouncementsView"])
check = pd.isnull(student["raisedhands"])
check = pd.isnull(student["VisITedResources"])
check = pd.isnull(student["Discussion"])
student[check]
