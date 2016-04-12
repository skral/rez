import os.path
import shutil
import zipfile


def build(source_path, build_path, install_path, targets):

    name = "cmake-3.5.1-win32-x86"
    zip_path = os.path.join(source_path, name + ".zip")

    if not os.path.exists(zip_path):
        raise Exception('ZIP is missing: %s' % zip_path)

    extract = os.path.join(build_path, "extract")
    staging = os.path.join(build_path, "staging")

    def _copy(src, dest):
        print "copying %s to %s..." % (src, dest)
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)

    def _extracting(src, dest):
        print "extracting %s..." % src
        with zipfile.ZipFile(src, 'r') as file_:
            file_.extractall(dest)

    def _move(src, dest):
        print "moving %s to %s..." % (src, dest)
        shutil.move(src, dest)

    # Extract
    _extracting(zip_path, extract)

    # Move to staging
    sub_dir = os.path.join(extract, name)
    _move(sub_dir, staging)

    if "install" not in (targets or []):
        return

    # Install
    src = os.path.join(build_path, "staging")
    dest = os.path.join(install_path)
    _copy(src, dest)
