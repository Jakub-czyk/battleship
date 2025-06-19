import os
from reports.plotting import plot_hits_over_turns

def test_plot_hits_output():
    hits = [0, 2, 1, 0, 3]
    output_path = "reports/test_plot.png"
    
    plot_hits_over_turns(hits, filename=output_path)
    
    assert os.path.exists(output_path)
    
    os.remove(output_path)
