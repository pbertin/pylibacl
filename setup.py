#!/usr/bin/env python

import distutils, os
from distutils.core import setup, Extension

(u_sysname, u_nodename, u_release, u_version, u_machine) = os.uname()

macros = []
libs = []
if u_sysname == "Linux":
    macros.append(("HAVE_LINUX", None))
    macros.append(("HAVE_LEVEL2", None))
    libs.append("acl")
elif u_sysname == "FreeBSD":
    macros.append(("HAVE_FREEBSD", None))
    libs.append("posix1e")
else:
    raise ValueError("I don't know your system. Please contact the author")

long_desc = """This is a C extension module for Python which
implements POSIX ACLs manipulation. It is a wrapper on top
of the systems's acl C library - see acl(5)."""
version = "0.1"
setup(name="pylibacl",
      version=version,
      description="POSIX.1e ACLs for python",
      long_description=long_desc,
      author="Iustin Pop",
      author_email="iusty@k1024.org",
      url="http://pylibacl.sourceforge.net",
      license="GPL",
      ext_modules=[Extension("posix1e", ["acl.c"],
                             libraries=libs,
                             define_macros=macros,
                             )],
      data_files=[("/usr/share/doc/pylibacl-%s" % version,
                   ["README","IMPLEMENTATION", "PLATFORMS",
                    "posix1e.html", "posix1e.txt"])],
      )