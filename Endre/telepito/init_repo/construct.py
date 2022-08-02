import os
from directory_tree import DirectoryTree
from db_config import DBConf


class Construct:

    def __init__(self, db_name_obj, git_path, template_path, special_files):
        self._git_path = git_path

        self._db_conf = DBConf(db_name_obj)
        self._tree = DirectoryTree(db_name_obj)

        self._repo_path = self._git_path + self._db_conf.repo_name
        self._template_path = template_path
        self._special_files = special_files

        try:  # A Git Repo könyvtár létrehozása belépés előtt, ha szükséges ..
            os.mkdir(self._repo_path)
        except FileExistsError:
            pass
        finally:
            os.chdir(self._repo_path)  # Belépünk a Git könyvtárba..

    # -- tree --
    @property
    def tree(self):
        return self._tree

    # -- template_path --
    @property
    def template_path(self):
        return self._template_path

    # -- special_files --
    @property
    def special_files(self):
        return self._special_files

    # -- create_tree -- generáló folyamat --
    def create_tree(self, parent_id, level=1):
        # Soronként vizsgálom meg, a szülő egyezőséget..
        branch_list = [x for x in self._tree.structure if x["parent_id"] == parent_id]
        path = os.getcwd()

        for x_branch in branch_list:
            os.chdir(path)  # Visszalépünk a kiinduló könyvtárba, a rekurzió miatt is..

            if x_branch.get("type") == "D":
                print(str(level) + level * "  " + x_branch.get("name"))
                try:
                    os.mkdir(x_branch.get("name"))
                except FileExistsError:
                    pass
                finally:
                    os.chdir(x_branch.get("name"))  # Belépünk az új könyvtárba..

                # Rekurzívan, a könyvtáron belüli elemekkel folytatjuk..
                self.create_tree(parent_id=x_branch.get("obj_id"), level=level + 1)

            elif x_branch.get("type") == "F":
                print(str(level) + level * "  " + x_branch.get("name"))
                self.create_file(elem=x_branch)
            else:
                print("HIBÁS!!", x_branch)

    def create_file(self, elem):
        # Nem minden file-t hozunk létre újra, vannak kivételek, amiket nem lehet felül írni!!
        if elem.get("name") in self._special_files:
            try:
                f = open(elem.get("name"), "x", encoding="utf-8")
                self.create_file_body(f, elem)
                f.close()
            except FileExistsError:
                pass
        else:
            f = open(elem.get("name"), "w", encoding="utf-8")
            self.create_file_body(f, elem)
            f.close()

    # file-ok tartalmának létrehozása, template-ek alapján..
    def create_file_body(self, f, elem):
        file_name = elem.get("template")

        with open(self.template_path + file_name, "r", encoding="utf-8") as reader:
            line = reader.readline()
            while line != '':  # The EOF char is an empty string
                for old, new in self._db_conf.replace_list.items():
                    line = line.replace("#" + old + "#", new)
                f.write(line)
                line = reader.readline()

# if __name__ == '__main__':
#     from db_name import DBName
#
#     db_n = DBName(domain_name="core", service_name="customer", schema_name="customer")
#
#     const = Construct(db_name_obj=db_n, git_path="c:/GIT/MLFF/proba/")
#
#     const.create_tree(parent_id=0)
