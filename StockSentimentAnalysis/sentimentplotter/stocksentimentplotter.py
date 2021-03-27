import matplotlib.pyplot as plt


def plot(df):
    plt.figure(figsize=(10, 8))

    mean_df = df.groupby(['ticker', 'date']).mean()
    # Unstacking? Not sure what this is
    mean_df = mean_df.unstack()
    # Manipulate the data from and transposing it to key value pairs of dates + compound values
    # .xs is cross section function. Get rid of extra label added to data set
    mean_df = mean_df.xs('compound', axis="columns").transpose()
    # Plot and render chart
    mean_df.plot(kind='line')
    plt.show()