import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(filtered_df):
    """
    Plot the DataFrame to a bar graph and save it as PDF and PNG.
    """
    # Extracting the column names and values
    column_names = filtered_df.iloc[:, 0]
    values = filtered_df.iloc[:, 1].astype(float)  # Convert values to float for plotting

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(column_names, values)
    plt.xlabel('X Axis')  # Update x-axis label
    plt.ylabel('Y Axis')  # Update y-axis label
    plt.title('Bar Graph of Filtered DataFrame')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save the plot as PDF
    pdf_file_name = 'plot.pdf'
    plt.savefig(pdf_file_name, format='pdf')
    
    # Save the plot as PNG
    png_file_name = 'plot.png'
    plt.savefig(png_file_name, format='png')

# Path to the Excel file
file_path = "/Users/paullack/Documents01/projects/python/python-projects-for-everyone/pandas/overdose/excel_DOSE_dashboard_output-download.xlsx"

# Number of rows to skip (skip the first five rows)
skip_rows = 5

# Read the second tab ("DOSE_dashboard_output-download") into a DataFrame, ignoring the first five rows
try:
    df = pd.read_excel(file_path, engine='openpyxl', sheet_name="DOSE_dashboard_output-download", skiprows=skip_rows)
    #print("DataFrame created successfully from the second tab, ignoring the first five rows.")
    
    # Prompt the user to enter a state code
    state_code = input("Enter a state code (e.g., AR for Arkansas): ").upper()
    
    # Filter the DataFrame based on the user input in the 1st column
    state_df = df[df.iloc[:, 0].str.contains(state_code)]
    
    # Display the filtered DataFrame for the state code
    #print("\nFiltered DataFrame for state code:", state_code)
    #print(state_df)  # Displaying the entire filtered DataFrame
    
    # Filter state_df further to only include rows where the 24th row contains the string "7Month2MonthAR"
    state_df = state_df[state_df.iloc[:, 23].astype(str).str.contains("7Month2Month", na=False)]
    
    # Display the filtered DataFrame for the specified string in the 25th row
    #print("\nFiltered DataFrame for '7Month2MonthAR' in the 25th row:")
    #print(state_df)  # Displaying the entire filtered DataFrame
    
    # Prompt the user to enter a year
    year = input("Enter a year: ")
    
    # Filter the existing DataFrame based on the user input in the 5th column (Year column)
    filtered_df = state_df[state_df.iloc[:, 4].astype(str).str.contains(year)]
    
    # Display the filtered DataFrame for the year
    #print("\nFiltered DataFrame for year:", year)
    #print(filtered_df)  # Displaying the entire filtered DataFrame
    
    # Keep only the 5th and 11th columns in the filtered DataFrame
    filtered_df = filtered_df.iloc[:, [5, 9]]
    
    # Display the final filtered DataFrame with only the 5th and 10th columns
    #print("\nFinal DataFrame with only the 5th and 10th columns:")
    #print(filtered_df)  # Displaying the entire final DataFrame
    
    plot_graph(filtered_df)
    print("Plot saved as 'plot.pdf' and 'plot.png' in the current directory.")
    
except Exception as e:

    print("Insuffecient Data:", e)
