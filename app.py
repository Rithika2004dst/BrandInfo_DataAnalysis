#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


def load_data():
    choice = input("Do you want to upload a file (f) or enter data manually (m)? [f/m]: ")
    if choice.lower() == 'f':
        file_path = input("Enter the path to your CSV file: ")
        try:
            data = pd.read_csv(file_path)
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    elif choice.lower() == 'm':
        data = input("Enter your data as comma-separated values: ")
        try:
            data = pd.DataFrame([float(i) for i in data.split(',')])
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    else:
        print("Invalid option, please try again.")
        return load_data()


# In[11]:


def analyze_data(data):
    if data is not None:
        print("\nSummary Statistics:")
        print(data.describe())
        try:
            data.plot(kind='line')
            plt.title('Data Analysis')
            plt.xlabel('Index')
            plt.ylabel('Values')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")


# In[12]:


def main():
    data = load_data()
    analyze_data(data)

if __name__ == "__main__":
    main()


# In[ ]:




