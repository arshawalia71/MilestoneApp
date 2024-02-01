import pandas as pd
import plotly.express as px
import streamlit as st
# import matplotlib.pyplot as plt
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.set_page_config(layout="wide")

st.title("Filtered Dataframes")




def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """


    show_charts = st.checkbox("Charts")
    modify = st.checkbox("Add filters")

    if show_charts:
        # Display the charts in one row
        st.write("## Charts")

        st.write("### Total Number of Projects by Region")
        region_counts = df["Proj_Region"].value_counts()
        
        fig_bar = px.bar(region_counts, x=region_counts.index, y=region_counts.values, title="Projects by Region")
        fig_bar.update_yaxes(title_text="Total Number of Projects")  # Set y-axis label

        # Customize hover text in the bar chart
        fig_bar.update_traces(
            hovertemplate="Region: %{x}<br>Total Projects: %{y}"
        )

        # Add the total count on the top right of the bar chart
        total_count = df.shape[0]
        fig_bar.add_annotation(
            text=f"Total Projects: {total_count}",
            xref="paper", yref="paper",
            x=0.95, y=0.95,
            showarrow=False
        )

        st.plotly_chart(fig_bar)
        
        # Display the second chart (Total number of projects by milestone) as an interactive pie chart using Plotly
        st.write("### Total Number of Projects by Milestone")
        milestone_counts = df["MS:Short_Name"].value_counts()
        
        # Modify the labels to include count in brackets
        milestone_labels = [f"{label} ({count})" for label, count in zip(milestone_counts.index, milestone_counts.values)]
        
        # Define a custom color palette
        custom_palette = px.colors.qualitative.Set1

        fig_pie = px.pie(milestone_counts, names=milestone_labels, values=milestone_counts.values, title="Milestone Distribution", color_discrete_sequence=custom_palette)
        # Customize hover text in the pie chart
        fig_pie.update_traces(
            hovertemplate="Milestone= %{label}<br>Milestone percent= %{percent}"
        )

        # Add the total count on the top right of the pie chart
        total_count = df.shape[0]
        fig_pie.add_annotation(
            text=f"Total Projects: {total_count}",
            xref="paper", yref="paper",
            x=0.95, y=0.95,
            showarrow=False
        )

        st.plotly_chart(fig_pie)

    # checking if the filters checkbox is enabled
    if not modify:
        return df

  
    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()
# Creating a Streamlit container for the filter controls.
# It allows users to select columns for filtering and provides different input widgets based
# on the data type of the column (multiselect, slider, date input, text input, etc.).
    with modification_container:
        columns = ["Resource: Full Name", "Resource: Manager: Full Name", "Proj_Region","MS:Short_Name", "Status", "End Date"]
        to_filter_columns = st.multiselect("Filter dataframe on", columns )
        for column in to_filter_columns:
            left, right = st.columns((1, 20)) #2 columns created with width 1 and 20 respectively
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            # this is to have unique values in the column as dropdowns for filter selection
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            # if numeric, it will add a slider for filtering
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            # lets us to select dates on the calander
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            # ...

            elif is_object_dtype(df[column]):
                user_text_input = right.text_input(f"Substring or regex in {column}")
                if user_text_input:
                    # Fill NaN values with an empty string
                    df[column] = df[column].fillna("").astype(str)
                    df = df[df[column].str.contains(user_text_input)]

# ...

            # else:
            #     user_text_input = right.text_input(
            #         f"Substring or regex in {column}",
            #     )
            #     print("Hello")
            #     print(user_text_input)
            #     if user_text_input:
            #         df = df[df[column].str.contains(user_text_input)]

    total_hours = df['Total Hours'].sum()
    st.write(f"Total Hours: {total_hours:.2f}")
    return df


df = pd.read_csv("output_20240104162000.csv")


st.dataframe(filter_dataframe(df))