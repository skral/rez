import imp
import os
import shutil
import sys


def build(source_path, build_path, install_path, targets):
    """Import get-pip.py, monkey patches the bootstrap function in order to
    change arguments given to pip. Will remove --upgrade and replace it with
    an install location.

    Doesn't install Wheel by default.
    """

    # If you want to install wheel comment the next line.
    os.environ["PIP_NO_WHEEL"] = '1'

    def _make_dirs(path):
        try:
            os.makedirs(path)
        except OSError:
            pass

    def _copy(src, dest):
        print "copying %s to %s..." % (src, dest)
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)

    def _import_get_pip(path):
        return imp.load_source('get-pip', os.path.join(path, 'get-pip.py'))

    def _sys_exit(*args, **kwargs):
        return

    staging_path = os.path.join(build_path, 'staging')

    dest_path = os.path.join(staging_path, 'python')
    dest_bin_path = os.path.join(staging_path, 'bin')

    _make_dirs(dest_path)
    _make_dirs(dest_bin_path)
    
    args = [
        '--target',
        dest_path,
        '--install-option=--install-scripts=' + dest_bin_path]

    # Extend sys.argv so get-pip will find them
    sys.argv += args

    # Monkey patch sys.exit otherwise get-pip quits python and we can't
    # install the files.
    sys_exit = sys.exit
    sys.exit = _sys_exit

    get_pip = _import_get_pip(source_path)
    get_pip.main()

    sys.exit = sys_exit

    if "install" not in (targets or []):
        return

    # Install
    _copy(staging_path, install_path)
