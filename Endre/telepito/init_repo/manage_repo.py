from construct import Construct
from db_name import DBName
from os import getcwd

# [(domain_name, service_name, schema_name)]
db_param_list = [
    {"domain_name": "core", "service_name": "customer", "schema_name": "customer"},
    {"domain_name": "core", "service_name": "notification_common", "schema_name": "notification_email"},
    {"domain_name": "core", "service_name": "notification_email", "schema_name": "notification_email"},
    {"domain_name": "core", "service_name": "notification_pn", "schema_name": "notification_pn"},
    {"domain_name": "core", "service_name": "notification_wa", "schema_name": "notification_wa"},
    {"domain_name": "core", "service_name": "template", "schema_name": "template"},
    {"domain_name": "core", "service_name": "ticket", "schema_name": "ticket"},
    {"domain_name": "core", "service_name": "vehicle", "schema_name": "vehicle"},
    {"domain_name": "enforcement", "service_name": "detection_image", "schema_name": "detection_image"},
    {"domain_name": "enforcement", "service_name": "detection", "schema_name": "detection"},
    {"domain_name": "enforcement", "service_name": "exemption", "schema_name": "exemption"},
    {"domain_name": "enforcement", "service_name": "visual_check", "schema_name": "visual_check"},
    {"domain_name": "eobu", "service_name": "tariff", "schema_name": "tariff"},
    {"domain_name": "eobu", "service_name": "trip", "schema_name": "trip"},
    {"domain_name": "payment", "service_name": "account_info", "schema_name": "account_info"},
    {"domain_name": "payment", "service_name": "psp_proxy", "schema_name": "psp_proxy"},
    {"domain_name": "payment", "service_name": "retry", "schema_name": "retry"},
    {"domain_name": "payment", "service_name": "transaction", "schema_name": "transaction"},
    {"domain_name": "settlement", "service_name": "psp_clearing", "schema_name": "psp_clearing"},
    {"domain_name": "settlement", "service_name": "tro_clearing", "schema_name": "tro_clearing"}]

git_path = "C:/GIT/MLFF/proba/"

template_path = getcwd() + "/template/"

special_files = ["create-tables.xml", "create-views.xml", "schema-version-0.xml", "install-dmls.xml"]


def create_all_repo():
    # print(os.getcwd())

    # A ciklus az összes Repo létrehozását elvégzi, de ha csak 1 param-al futtatunk le, akkor csak 1-et..
    for param in db_param_list:
        db_name_obj = DBName(**param)
        print(param)
        # print(db_name.domain_name, db_name.service_name, db_name.schema_name, db_name.repo_name, db_name.db_name)
        const = Construct(db_name_obj=db_name_obj, git_path=git_path, template_path=template_path,
                          special_files=special_files)
        # Itt indítjuk a létrehozást!!
        const.create_tree(parent_id=0)


if __name__ == '__main__':
    create_all_repo()
