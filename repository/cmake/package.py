name = "cmake"
version = '3.5.1'
authors = ['Kitware']
uuid = "723072b0-ea27-11e5-8fab-0025902178a3"
description = 'Open-Source cross platform'
homepage = 'https://cmake.org'

variants = [['platform-windows', 'arch-AMD64', 'os-windows-6.1.7601.SP1']]


def commands():
    env.PATH.append('{this.root}/bin')
