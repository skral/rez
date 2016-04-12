import os.path
import shutil
from subprocess import Popen


def build(source_path, build_path, install_path, targets):

    msi_path = os.path.join(source_path, "VCForPython27.msi").replace("/", "\\")

    if not os.path.exists(msi_path):
        raise Exception('MSI is missing: %s' % msi_path)

    msi_target_dir = os.path.join(build_path, "extract").replace("/", "\\")
    staging = os.path.join(build_path, "staging")

    def _copy(src, dest):
        print "copying %s to %s..." % (src, dest)
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)

    def _execute(cmds):
        print "executing %s..." % cmd
        Popen(cmd).wait()

    def _move(src, dest):
        print "moving %s to %s..." % (src, dest)
        shutil.move(src, dest)

    # Extract
    cmd = ["cmd.exe",
           "/c",
           "start",
           "/wait",
           "msiexec",
           "/a",
           msi_path,
           "/qb",
           "/norestart",
           "TARGETDIR=" + msi_target_dir]
    _execute(cmd)

    # Move to staging
    sub_dir = os.path.join(msi_target_dir, "Microsoft",
                           "Visual C++ for Python", "9.0")
    _move(sub_dir, staging)

    if "install" not in (targets or []):
        return

    # Install
    src = os.path.join(build_path, "staging")
    dest = os.path.join(install_path)
    _copy(src, dest)
