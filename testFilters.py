import streamlit as st

def main():
    st.title("Main Page")
    if st.button("Go to Hello Page"):
        # Set the URL query parameter to navigate to hello.py
        st.experimental_set_query_params(page="hello")

if __name__ == "__main__":
    main()






# import pandas as pd
# import plotly.express as px
# import streamlit as st
# # import matplotlib.pyplot as plt
# from pandas.api.types import (
#     is_categorical_dtype,
#     is_datetime64_any_dtype,
#     is_numeric_dtype,
#     is_object_dtype,
# )

# st.set_page_config(layout="wide")

# st.title("Milestone Report FY23 Q4")

# def display_prompts_for_region(df):

#     # Display prompts in two columns
#     col1, col2 = st.columns(2)

#     # Prompt 1
#     with col1:
#         st.write("#### Top 5 use cases in the current quarter")
#         st.write(top_use_cases(df))

#     # Prompt 2
#     with col2:
#         st.write("#### Top 5 projects where VR was done in the current quarter")
#         st.write(top_projects_for_VR_completed(df))

#     # Prompt 3
#     with col1:
#         st.write("#### Top 5 projects that were kicked off in the current quarter")
#         st.write(top_projects_for_Kickoff_completed(df))

#     # Prompt 4
#     with col2:
#         st.write("#### Top 5 projects with high burn")
#         st.write(top_projects_for_Highburn(df))

#     # Prompt 5
#     with col1:
#         st.write("#### Top 3 Vertical view")
#         st.write(top_verticals(df))

#     # Prompt 6
#     with col2:
#         st.write("#### Top 3 consultants with high billable effort")
#         st.write(top_3_consultants_highBillableEffort(df))

#     # Prompt 7
#     with col1:
#         st.write("#### Top 3 Consultants with high Adhoc support hours")
#         st.write(top_3_consultants_highAdhocSupportHours(df))

#     with col2:
#         st.write("#### Top 3 FWRs in the current Quarter")
#         st.write(top_FWRs(df))

# def top_use_cases(df):
    
#     # List of excluded activities
#     excluded_activities = ["PM Activities", "Project Kick Off","FWR", "Adhoc Support activities", "Value Realization", "Enablement"]

#     # Filter out rows with excluded activities
#     filtered_df = df[~df["MS:Short_Name"].isin(excluded_activities)]

#     # Group by milestone and sum the hours spent
#     milestone_hours = filtered_df.groupby("MS:Short_Name")["Total Hours"].sum()

#     # Sort the milestones based on hours spent and select the top 5
#     top_5_milestones = milestone_hours.nlargest(5)
#     # top_5_use_cases = [df["Project: Project Name"][0], df["Project: Project Name"][1], df["Project: Project Name"][1], df["Project: Project Name"][1],df["Project: Project Name"][1]]  # Replace this with your actual calculation
#     return top_5_milestones

# # Function to calculate the top 5 milestones based on effort spent (excluding specific milestones)
# def top_projects_for_VR_completed(df):
#     # Filter out rows with excluded activities
#     filtered_df = df[df["MS:Short_Name"].isin(["Value Realization"])]

#     # Group by project name and sum the VR effort spent
#     project_vr_effort = filtered_df.groupby("Project: Project Name")["Total Hours"].sum()

#     # Sort the projects based on VR effort spent and select the top 5
#     top_5_projects_vr_effort = project_vr_effort.nlargest(5)

#     # Display the top 5 projects based on VR effort spent
#     return top_5_projects_vr_effort

# def top_projects_for_Kickoff_completed(df):
#     # Filter out rows with excluded activities
#     filtered_df = df[df["MS:Short_Name"].isin(["Project Kick Off"])]

#     # Group by project name and find the latest kickoff completion date
#     latest_kickoff_completion = filtered_df.groupby("Project: Project Name")["Total Hours"].sum()

#     # Sort the projects based on kickoff completion date and select the top 5
#     top_5_projects_kickoff_completion = latest_kickoff_completion.nlargest(5)

#     # Display the top 5 projects based on kickoff completion date
#     return top_5_projects_kickoff_completion

# def top_projects_for_Highburn(df):
#     filtered_df = df[df["MS:Short_Name"] != "FWR"]

#     # Perform groupby operation on the filtered DataFrame
#     project_effort = filtered_df.groupby("Project: Project Name")["Total Hours"].sum()

#     # Sort the projects based on total effort spent and select the top 5
#     top_5_projects_effort = project_effort.nlargest(5)

#     return top_5_projects_effort

# def top_FWRs(df):
#     # Filter the DataFrame for records with milestone name "FWR"
#     filtered_df = df[df["MS:Short_Name"] == "FWR"]

#     # Group by FWR and calculate total hours
#     fwr_effort = filtered_df.groupby("Project: Project Name")["Total Hours"].sum()

#     # Sort the FWRs based on total effort spent and select the top 3
#     top_3_fwr_effort = fwr_effort.nlargest(3)

#     return top_3_fwr_effort

# def top_verticals(df):
#     # Group by vertical and sum the total effort spent
#     vertical_effort = df.groupby("Vertical")["Total Hours"].sum()

#     # Sort the verticals based on total effort spent and select the top 3
#     top_3_verticals = vertical_effort.nlargest(3)

#     # Calculate the total effort spent across all verticals
#     total_effort = vertical_effort.sum()

#     # Calculate the percentage of effort spent for each vertical
#     percentage_split = (top_3_verticals / total_effort) * 100

#     # Combine the hours and percentage split into a DataFrame
#     top_verticals_df = pd.DataFrame({
#         "Total Hours": top_3_verticals,
#         "Percentage Split (%)": percentage_split
#     })

#     return top_verticals_df

# def top_3_consultants_highBillableEffort(df):
    

#     # Group by consultant name and sum the billable effort
#     consultant_billable_effort = df.groupby("Resource: Full Name")["Total Hours"].sum()

#     # Sort the consultants based on billable effort and select the top 3
#     top_3_consultants = consultant_billable_effort.nlargest(3)

#     return top_3_consultants

# def top_3_consultants_highAdhocSupportHours(df):
#     # Filter the DataFrame to include only rows with Adhoc support activities
#     adhoc_support_df = df[df["MS:Short_Name"] == "Adhoc Support activities"]

#     # Group by consultant name and sum the effort from Adhoc support activities
#     consultant_adhoc_support_effort = adhoc_support_df.groupby("Resource: Full Name")["Total Hours"].sum()

#     # Sort the consultants based on the effort from Adhoc support activities and select the top 3
#     top_3_consultants_adhoc_support = consultant_adhoc_support_effort.nlargest(3)

#     return top_3_consultants_adhoc_support




# def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
#     """
#     Adds a UI on top of a dataframe to let viewers filter columns

#     Args:
#         df (pd.DataFrame): Original dataframe

#     Returns:
#         pd.DataFrame: Filtered dataframe
#     """








#     columns_to_remove = ["Unnamed: 1", "Assignment: Resource: Resource Manager", "Resource: GDC Resource", 
#                      "Project: Practice: Practice Name", "Project: Region: Region Name", "Budget: DR Number",
#                      "Budget: Budget Name", "Milestone ID", "Milestone Comments", "Planned Hours", 
#                      "Actual Hours Total"]

#     df = df.drop(columns=columns_to_remove)


#     # show_prompts = st.checkbox("Prompts") 

#     if st.checkbox("Show Prompts"):
#         def filter_data(df, selected_region):
#             if selected_region == "All Regions":
#                 new_df = df  # No filtering needed for "All regions"
#                 # st.write("In All regions")
#                 return new_df
#             else:
#                 new_df = df[df['Proj_Region'] == selected_region]
#                 # st.write("Not In All regions")
#                 return new_df

#         regions = ["Americas", "APAC", "EMEA", "All Regions"]
#         selected_region = st.radio("Select region", regions)

#         st.write("##",selected_region)

#         #here the df to be used for filters will be returned. 
#         df_prompts = filter_data(df, selected_region)
#         display_prompts_for_region(df_prompts)
       

#     show_charts = st.checkbox("Charts")
    


#     if show_charts:
#         # Display the charts in one row
#         st.write("## Charts")

#         st.write("### Number of Projects per Region")
        
#         # Calculate the number of unique projects per region
#         unique_projects_per_region = df.groupby("Proj_Region")["Project: Project Name"].nunique().reset_index()
#         unique_projects_per_region = unique_projects_per_region.rename(columns={"Project: Project Name": "Number of Unique Projects"})

#         # Create the bar chart
#         fig = px.bar(unique_projects_per_region, x="Proj_Region", y="Number of Unique Projects", title="")
#         fig.update_layout(xaxis_title="Region", yaxis_title="Number of Projects")

#         # Customize hover text in the bar chart
#         fig.update_traces(
#             hovertemplate="Region: %{x}<br>Total Projects: %{y}"
#         )

#         # Add the total count on the top right of the bar chart
#         total_count = df["Project: Project Name"].nunique()
#         fig.add_annotation(
#             text=f"Total Projects: {total_count}",
#             xref="paper", yref="paper",
#             x=0.95, y=0.95,
#             showarrow=False
#         )

#         st.plotly_chart(fig)
        
#         # Display the second chart (Total number of projects by milestone) as an interactive pie chart using Plotly
#         st.write("### Milestone Distribution")
#         # Group by milestone and sum the hours spent
#         milestone_hours = df.groupby("MS:Short_Name")["Total Hours"].sum()

#         # Modify the labels to include the total hours in brackets
#         milestone_labels = [f"{label} ({hours:.0f} hours)" for label, hours in zip(milestone_hours.index, milestone_hours.values)]

#         # Define a custom color palette
#         custom_palette = px.colors.qualitative.Set1

#         # Create the pie chart
#         fig_pie = px.pie(milestone_hours, names=milestone_labels, values=milestone_hours.values, title="", color_discrete_sequence=custom_palette)

#         # Customize hover text in the pie chart
#         fig_pie.update_traces(
#             hovertemplate="Milestone: %{label}"
#         )

        
#         # Add the total count on the top right of the pie chart
#         total_hours = milestone_hours.sum()
#         fig_pie.add_annotation(
#             text=f"Total Hours: {total_hours:.0f}",
#             xref="paper", yref="paper",
#             x=0.95, y=0.95,
#             showarrow=False
#         )

#         st.plotly_chart(fig_pie)


#     modify = st.checkbox("Add filters")
#     # checking if the filters checkbox is enabled
#     if not modify:
#         return df

  
#     # Try to convert datetimes into a standard format (datetime, no timezone)
#     for col in df.columns:
#         if is_object_dtype(df[col]):
#             try:
#                 df[col] = pd.to_datetime(df[col])
#             except Exception:
#                 pass

#         if is_datetime64_any_dtype(df[col]):
#             df[col] = df[col].dt.tz_localize(None)

#     modification_container = st.container()
# # Creating a Streamlit container for the filter controls.
# # It allows users to select columns for filtering and provides different input widgets based
# # on the data type of the column (multiselect, slider, date input, text input, etc.).
#     with modification_container:
#         columns = ["Resource: Full Name",  "Proj_Region","MS:Short_Name","Vertical", "Status", "End Date"]
#         to_filter_columns = st.multiselect("Filter dataframe on", columns )
#         for column in to_filter_columns:
#             left, right = st.columns((1, 20)) #2 columns created with width 1 and 20 respectively
#             left.write("↳")
#             # Treat columns with < 10 unique values as categorical
#             # this is to have unique values in the column as dropdowns for filter selection
#             if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
#                 user_cat_input = right.multiselect(
#                     f"Values for {column}",
#                     df[column].unique(),
#                     default=list(df[column].unique()),
#                 )
#                 df = df[df[column].isin(user_cat_input)]
#             # if numeric, it will add a slider for filtering
#             elif is_numeric_dtype(df[column]):
#                 _min = float(df[column].min())
#                 _max = float(df[column].max())
#                 step = (_max - _min) / 100
#                 user_num_input = right.slider(
#                     f"Values for {column}",
#                     _min,
#                     _max,
#                     (_min, _max),
#                     step=step,
#                 )
#                 df = df[df[column].between(*user_num_input)]
#             # lets us to select dates on the calander
#             elif is_datetime64_any_dtype(df[column]):
#                 user_date_input = right.date_input(
#                     f"Values for {column}",
#                     value=(
#                         df[column].min(),
#                         df[column].max(),
#                     ),
#                 )
#                 if len(user_date_input) == 2:
#                     user_date_input = tuple(map(pd.to_datetime, user_date_input))
#                     start_date, end_date = user_date_input
#                     df = df.loc[df[column].between(start_date, end_date)]
#             # ...

#             elif is_object_dtype(df[column]):
#                 original_column = df[column].copy()  # Make a copy of the original column
                
#                 # Convert column values to lowercase
#                 df[column] = df[column].str.lower()
                
#                 user_text_input = right.text_input(f"Enter substring to be searched in {column}")
#                 # Replace NA or NaN values with an empty string
#                 df[column] = df[column].fillna("").astype(str)

#                 # Filter the DataFrame only for non-NA or non-NaN values and then check for the substring
#                 df_filtered = df[df[column].str.contains(user_text_input.lower())]
                
#                 if user_text_input:
#                     user_text_input = user_text_input.lower()  # Convert user input to lowercase
#                     # Filter the dataframe based on the lowercase column values and user input
#                     df = df_filtered[df_filtered[column].str.contains(user_text_input)]
                    
#                     # Restore the original case of the column values for display
#                     df[column] = original_column[df.index]

# # ...

#             # else:
#             #     user_text_input = right.text_input(
#             #         f"Substring or regex in {column}",
#             #     )
#             #     print("Hello")
#             #     print(user_text_input)
#             #     if user_text_input:
#             #         df = df[df[column].str.contains(user_text_input)]

#     total_hours = df['Total Hours'].sum()
#     total_items = len(df)
#     st.write(f"Total Hours: {total_hours:.2f}")
#     st.write(f"Total Items: {total_items:.2f}")
    
#     return df


# df = pd.read_csv("output_20240205154536.csv")


# st.dataframe(filter_dataframe(df),hide_index=True)



# #................................................................................................................................................................
# # Get the URL parameters
# url_params = st.experimental_get_query_params()

# if "nav" in url_params:
#     if url_params["nav"][0] == "hello":
#         # If the "nav" parameter is set to "hello", display the hello.py page
#         st.title("Hello Page")
#         st.write("Welcome to the Hello Page!")
#         # Add a back button to navigate back to the main page
#         if st.button("Back to Main Page"):
#             st.experimental_set_query_params(nav="main")
#     else:
#         # If the "nav" parameter is set to any other value, display the main page
#         st.title("Main Page")
#         if st.button("Go to Hello Page"):
#             # Set the "nav" parameter to "hello" when the button is clicked
#             st.experimental_set_query_params(nav="hello")
# else:
#     # If the "nav" parameter is not set, display the main page
#     st.title("Main Page")
#     if st.button("Go to Hello Page"):
#         # Set the "nav" parameter to "hello" when the button is clicked
#         st.experimental_set_query_params(nav="hello")
