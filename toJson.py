import json
import os

CONVERT_SOURCE = True


def lang_to_dict(file_path):
    lang_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.replace('\r', '').replace('\n', '').replace('\t', '')
            if line.startswith("#"):
                continue
            line_split = line.split("=", 2)
            if len(line_split) == 2:
                lang_dict[line_split[0]] = line_split[1]
    return lang_dict


def lang_to_json(project_in, namespace_in, lang_file):
    lang_file_path = "./files/{}/assets/{}/lang/{}".format(project_in, namespace_in, lang_file)
    if lang_file.endswith(".lang") and os.path.isfile(lang_file_path):
        lang_dict = lang_to_dict(lang_file_path)
        i18n_lang_file_path = "./i18n/{}/assets/{}/lang/{}.json".format(project_in, namespace_in, lang_file[:-5])
        with open(i18n_lang_file_path, "w", encoding="utf-8") as file:
            json.dump(lang_dict, file, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == '__main__':
    for project in os.listdir("./files"):
        projectAssetsPath = "./files/{}/assets".format(project)
        if not os.path.isdir(projectAssetsPath):
            continue
        for namespace in os.listdir(projectAssetsPath):
            langFolderPath = "./files/{}/assets/{}/lang".format(project, namespace)
            if not os.path.isdir(langFolderPath):
                continue
            i18nFolderPath = "./i18n/{}/assets/{}/lang".format(project, namespace)
            if not os.path.isdir(i18nFolderPath):
                os.makedirs(i18nFolderPath)
            if CONVERT_SOURCE:
                lang_to_json(project, namespace, "en_us.lang")
            else:
                for langFile in os.listdir(langFolderPath):
                    lang_to_json(project, namespace, langFile)
