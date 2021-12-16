from setuptools import find_packages, setup

setup(name='sentiment_analysis',
      packages=['sentiment_analysis'],      
      version='0.2.0',
      description="sentiment analysis library",
      author='Syrine Cheriaa',
      package_data={'sentiment_analysis': ['data/*'],},
      include_package_data=True,
      install_requires=[
        'pandas==1.1.1',
        'transformers==4.12.5',
        'sentencepiece',
        'protobuf',
        'torch@https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp37-cp37m-linux_x86_64.whl',
      

 ]
)