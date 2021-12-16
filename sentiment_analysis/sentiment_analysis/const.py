import pkg_resources
import os

root_data = pkg_resources.resource_filename('sentiment_analysis', 'data/')
path_checkpoint_file = os.path.join(root_data, 'checkpoint.pth')
path_index_to_target = os.path.join(root_data, 'index_to_target.json')
