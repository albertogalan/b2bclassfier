import pandas as pd
import matplotlib.pyplot as plt
from data_cleaner import clean_data
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D


DATA = 'customer.csv'

# Loads and cleans data
df = clean_data(pd.read_csv(DATA, sep=';'))


# Reducing dimensions to 2 for plotting
def dim_reduce(db):
    pca = PCA(n_components=2)
    db = pca.fit_transform(db)

    return db


# Plots out clusters of segmented customers
def plot_clusters(db, label=None):

    x, y = zip(* db)      # Grabbing coordinates of clusters

    # Creates 3-D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Axes3D.scatter(ax, xs=x, ys=y, c=label)
    plt.title("Market Segmentation of Existing Customers")


if __name__ == "__main__":
    df = dim_reduce(df)

    # Finding clusters of target customers
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(df)
    centers = kmeans.cluster_centers_   # Location of clusters
    labels = kmeans.predict(df)     # Labels for different clusters

    plot_clusters(df, label=labels)
    plt.show()
