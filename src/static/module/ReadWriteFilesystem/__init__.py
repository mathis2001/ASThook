
from static.module.register import ModuleStaticCmd
from utils import Output

@ModuleStaticCmd("list_read_write",
        "list all read and write on filesystem",
        bool)
class ListFuncs:
    """
    Class List ReadWriteFilesystem
    
    To use:
    """
    def __init__(self, package, tmp_dir, args):
        from ..name_file import name_file_node # dependance
        from . import ReadWriteFilesystem
        
        Output.add_printer_callback("tree", "Filesystem", "READ", mprint)
        Output.add_printer_callback("tree", "Filesystem", "WRITE", mprint)


def mprint(arg : list) -> str:
    return f"{arg}"
