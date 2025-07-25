#Taux de convertion
# This script converts time series data into a format suitable for convolutional neural networks.   
import pandas as pd 
import numpy as np
import os
from typing import List, Dict, Any
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
# Load the datasetdf_events = pd.read_csv('events.csv')
df_events = pd.read_csv('events.csv')
total_views = df_events[df_events['event'] == 'view'].shape[0]
total_transactions = df_events[df_events['event'] == 'transaction'].shape[0]
conversion_rate = total_transactions / (total_views *100)
print(f"Total Views: {total_views}, Total Transactions: {total_transactions}, Conversion Rate: {conversion_rate:.2%}")
# Total unique users
total_users = df_events['visitorid'].nunique()
print(f"Total Unique Users: {total_users}")
