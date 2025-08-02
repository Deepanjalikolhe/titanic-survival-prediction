import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation(df):
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_survival_by_sex(df):
    sns.countplot(x='Survived', hue='Sex', data=df)
    plt.title('Survival by Gender')
    plt.show()