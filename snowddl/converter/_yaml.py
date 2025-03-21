from yaml import SafeDumper, add_representer


class SnowDDLDumper(SafeDumper):
    pass


class YamlFoldedStr(str):
    pass


class YamlLiteralStr(str):
    pass


def folded_str_presenter(dumper: SnowDDLDumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")


def literal_str_presenter(dumper: SnowDDLDumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


add_representer(YamlFoldedStr, folded_str_presenter, Dumper=SnowDDLDumper)
add_representer(YamlLiteralStr, literal_str_presenter, Dumper=SnowDDLDumper)
