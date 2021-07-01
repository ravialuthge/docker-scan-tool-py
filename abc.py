import sys
import pkgutil

def load_all_modules_from_dir(profiles):
    for importer, package_name, _ in pkgutil.iter_modules([profiles]):
        full_package_name = '%s.%s' % (profiles, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name).load_module(full_package_name)
            print (module)

load_all_modules_from_dir('profiles')