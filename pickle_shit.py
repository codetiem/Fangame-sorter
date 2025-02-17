import pickle


# data syntax:  data{
#     games:
#     tags:
#     excluded:
# }


def save_data(data):
    file = open("data.pickle ", "wb")
    pickle.dump(data, file)
    file.close()

def load_data():
    file = open("data.pickle ", "rb")
    data = pickle.load(file)
    file.close()
    return data