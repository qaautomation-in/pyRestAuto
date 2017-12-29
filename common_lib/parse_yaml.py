import yaml
import os


class Yamlparser():
    """
    Initiate this class object with yaml file path
    Usage:
        path = os.path.abspath("../resources/config.yaml")
        obj = Yamlparser(path)
    """

    def __init__(self, file):
        self.file = file

    def get_data(self, root=None, branch=None):
        """
        This method is used to get data from yaml file.
        :param root:
        :param branch:
        :return:
        """
        with open(self.file, 'r') as yamlfile:
            data = yaml.load(yamlfile)
            if root:
                return data[root][branch]
            else:
                return data[branch]

    def put_data(self):
        pass
