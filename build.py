# build.py

from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")

name = "lab2_it"
version = "0.1.0"  # or any version number that corresponds to your project's versioning scheme

default_task = "publish"

@init
def set_properties(project):
    project.depends_on("mockito")  # Add any additional dependencies here
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "src/unittest/python")
    project.set_property("coverage_break_build", False)  # Set to True if you want to fail the build on low coverage

    # Optional: Configure other properties as needed
    # project.set_property("some_property", "some_value")
