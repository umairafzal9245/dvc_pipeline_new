import wget


# Download the zipped dataset
url = 'https://drive.google.com/u/0/uc?id=16jsxOsTqeM8-PTrAtY8SdExVwglznFW_&export=download'
file_name = "fake.csv"
wget.download(url, file_name)

url = 'https://drive.google.com/u/0/uc?id=15IEEQ78ViCwVDgUGJjRZHKashPS-o9sg&export=download'
file_name = "true.csv"
wget.download(url, file_name)
