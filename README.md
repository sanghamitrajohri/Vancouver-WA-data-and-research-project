# Vancouver-WA-data-and-research-project

Here’s the updated **README.md** with the additional context about the project being done under **June Lukuyu at UW**:

---

# **Data Analysis Projects by Sanghamitra Johri**

Welcome to my data analysis repository! This repository contains various projects and analyses focused on **energy consumption**, **census demographics**, and **building characteristics**, among others. These projects are part of my work under **June Lukyu** at the **University of Washington (UW)**. Below is an overview of the contents, methodology, and insights derived from the data.

---

## **Objective**

To analyze energy consumption patterns across zip codes and understand the role of **socioeconomic factors**, **housing characteristics**, and **demographics**.

---

## **Contents**

### **Data Files**
- `building_data/`: Contains datasets related to building square footage and related analyses.
- `census_2020/`: Includes census data, such as population demographics, income, and racial distributions.
- `drive-download-20240809T213923Z-001/`: Additional supporting datasets for metadata exploration.
- `stn_data/`: Station-level data for specific analyses.

### **Scripts**
- `census_data.py`: Python script for analyzing census-related data (e.g., income, demographics).
- `meta_data_analysis.py`: Metadata exploration and pattern identification.
- `stn_data_analysis.py`: Analysis of station-level data (e.g., trends, anomalies).

### **Other Files**
- `README.md`: This document.
- `.gitignore`: Specifies files to ignore in the repository.

---

## **Projects and Insights**

### **1. Energy Consumption Analysis**
- **Objective**: To understand the relationship between energy consumption per capita, median income, and racial demographics across zip codes.
- **Key Insights**:
  - Income is a stronger driver of energy consumption than racial composition.
  - Larger buildings in high-income areas tend to consume more energy.
  - Energy efficiency opportunities exist in low-income areas.

### **2. Census Data Analysis**
- **Objective**: To explore population characteristics, diversity, and socioeconomic factors by zip code.
- **Highlights**:
  - Majority White populations are not directly correlated with energy consumption.
  - Variations in population density and income distribution shape energy use patterns.

### **3. Building Data Analysis**
- **Objective**: To analyze property square footage and its impact on energy consumption.
- **Findings**:
  - Most properties fall between 2000-2500 sqft.
  - Larger properties (>3500 sqft) show higher energy demands.

---

## **How to Use This Repository**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sanghamitrajohri/your-repo-name.git
   ```

2. **Install Dependencies**:
   Ensure Python and required libraries (e.g., `pandas`, `matplotlib`) are installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Scripts**:
   - Execute analysis scripts for specific datasets:
     ```bash
     python census_data.py
     python meta_data_analysis.py
     ```

4. **Visualize Results**:
   - Review generated graphs and insights in the output folder.

---

## **Acknowledgment**

This repository is part of a project supervised by **June Lukyu** at the **University of Washington (UW)**, where we explore the interplay between socioeconomic factors, building characteristics, and energy consumption patterns.

---

## **License**
This repository is open-source and available under the MIT License. Feel free to use or contribute!

---
