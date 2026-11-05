from pythonforandroid.recipe import PythonRecipe

class CharsetNormalizerRecipe(PythonRecipe):
    version = "2.1.1"
    url = "https://files.pythonhosted.org/packages/py2.py3/c/charset-normalizer/charset-normalizer-{version}-py2.py3-none-any.whl"
    depends = ["python3"]
    site_packages_name = "charset_normalizer"

recipe = CharsetNormalizerRecipe()
