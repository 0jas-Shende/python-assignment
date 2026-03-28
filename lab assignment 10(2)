import pandas as pd

# Create DataFrame for 5 states
data = {
    'State': ['State1', 'State2', 'State3', 'State4', 'State5'],
    'Area': [50000, 75000, 62000, 88000, 54000],      # in sq km
    'Population': [5_000_000, 8_500_000, 6_200_000, 9_100_000, 4_800_000]
}

df_states = pd.DataFrame(data)

# Display full table
print("\n🌍 Complete State Data:\n")
print(df_states.to_string(index=False))


# State with largest area
largest_area_state = df_states.loc[df_states['Area'].idxmax()]
print("\n🏞️ State with Largest Area:", largest_area_state['State'])


# State with largest population
largest_pop_state = df_states.loc[df_states['Population'].idxmax()]
print("\n👥 State with Largest Population:", largest_pop_state['State'])


# Add Population Density column
df_states['Density'] = df_states['Population'] / df_states['Area']

print("\n📊 Data with Population Density:\n")
print(df_states.to_string(index=False))


# State with highest population density
highest_density_state = df_states.loc[df_states['Density'].idxmax()]
print("\n🚀 State with Highest Population Density:", highest_density_state['State'])
