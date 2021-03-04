from bs4 import BeautifulSoup
import lxml
import json


class UDTToJSON:

    def __init__(self, input_file: str, output_folder: str):
        self.output_folder = output_folder
        self.soup = self.create_soup(input_file)
        self.datatype_names = [tag["name"] for tag in self.soup.find_all("datatype")]

    def main_command(self):
        for datatype in self.datatype_names:
            self.create_json_from_udt(datatype, self.output_folder)

    def create_soup(self, input_file: str):
        with open(input_file) as data:
            content = data.read()
            soup = BeautifulSoup(content, "lxml")
        return soup

    def create_json_from_udt(self, datatype_name: str, output_directory: str):
        """ This function formats json file, soup should be created before calling this function """
        udt = self.soup.find("datatype", {"name": f"{datatype_name}"})
        udt_members = {member["name"]:
                           {"datatype": member["datatype"],
                            "dimension": member["dimension"],
                            "externalAccess": member["externalaccess"],
                            "radix": member["radix"],
                            "value": None,
                            } for member in udt.find_all("member")}
        # create the file and dump the json in it
        with open(f"{output_directory}/{datatype_name}.json", "w") as outfile:
            json.dump({udt["name"]: udt_members}, outfile, indent=4)


