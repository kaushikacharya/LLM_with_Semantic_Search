import umap
import altair as alt

from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter(action="ignore", category=NumbaDeprecationWarning)
warnings.simplefilter(action="ignore", category=NumbaPendingDeprecationWarning)


def umap_plot(text, emb, n_neighbors=2):
    cols = list(text.columns)
    # UMAP reduces the dimensions from 1024 to 2 dimensions that we can plot
    reducer = umap.UMAP(n_neighbors=n_neighbors)
    umap_embeds = reducer.fit_transform(emb)
    
    # Prepare the data to plot and interactive visualization using Altair
    df_explore = text.copy()
    df_explore["x"] = umap_embeds[:, 0]
    df_explore["y"] = umap_embeds[:, 1]

    # Plot
    chart = alt.Chart(df_explore).mark_circle(size=60).encode(
        x = alt.X("x", scale=alt.Scale(zero=False)),
        y = alt.Y("y", scale=alt.Scale(zero=False)),
        tooltip=cols,
    ).properties(
        width=700,
        height=400
    )

    return chart
