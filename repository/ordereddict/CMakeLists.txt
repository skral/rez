CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezPipInstall)

set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url "C:/dev/rez_installer/${name}/${name}-${version}.tar.gz")

rez_pip_install(
    ${name}
    URL ${url}
)
