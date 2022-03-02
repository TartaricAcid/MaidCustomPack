import os
import shutil
import json


def json_to_lang(project_in, namespace_in, lang_file):
    lang_file_path = "./i18n/{}/assets/{}/lang/{}".format(project_in, namespace_in, lang_file)
    with open(lang_file_path, "r", encoding="utf-8") as file:
        lang_dict = json.load(file)
    if lang_file.endswith(".json") and os.path.isfile(lang_file_path):
        tmp_lang_file_path = "./tmp/{}/assets/{}/lang/{}.lang".format(project_in, namespace_in, lang_file[:-5])
        with open(tmp_lang_file_path, "w", encoding="utf-8") as tmpFile:
            for key, value in lang_dict.items():
                tmpFile.writelines("{}={}\n".format(key, value))


if __name__ == '__main__':
    if not os.path.isdir("./tmp"):
        os.makedirs("./tmp")
    if not os.path.isdir("./tlm_custom_pack"):
        os.makedirs("./tlm_custom_pack")
    for folder in os.listdir("./files"):
        shutil.copytree("./files/{}".format(folder), "./tmp/{}".format(folder))
    for project in os.listdir("./i18n"):
        projectAssetsPath = "./i18n/{}/assets".format(project)
        if not os.path.isdir(projectAssetsPath):
            continue
        for namespace in os.listdir(projectAssetsPath):
            langFolderPath = "./i18n/{}/assets/{}/lang".format(project, namespace)
            if not os.path.isdir(langFolderPath):
                continue
            i18nFolderPath = "./i18n/{}/assets/{}/lang".format(project, namespace)
            if not os.path.isdir(i18nFolderPath):
                os.makedirs(i18nFolderPath)
            for langFile in os.listdir(langFolderPath):
                if langFile != "en_us.json":
                    json_to_lang(project, namespace, langFile)
    for project in os.listdir("./tmp"):
        outPath = "./tlm_custom_pack/{}".format(project)
        projectPath = "./tmp/{}/".format(project)
        shutil.make_archive(outPath, "zip", projectPath)
    shutil.rmtree("./tmp")
