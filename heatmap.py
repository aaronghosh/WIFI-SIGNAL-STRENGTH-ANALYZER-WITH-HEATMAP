import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the file path of the CSV file
file_path = "C:\\Users\\ASUS\\PycharmProjects\\WIFIANALYZER\\signal_strength.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Define the color map
cmap = sns.color_palette("flare_r", as_cmap=True)

# Create a heatmap of the signal strengths
sns.set_theme()
sns.set(rc={'figure.figsize':(12,10)})
sns.kdeplot(x=df['Timestamp'], y=df['Signal Strength'], cmap=cmap, shade=True, thresh=0.05)

# Save the heatmap as an image file
plt.savefig('signal_strength_heatmap.png')
plt.show()
