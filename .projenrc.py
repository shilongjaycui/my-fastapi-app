from projen.python import PythonProject

project = PythonProject(
    author_email="shilongjaycui@gmail.com",
    author_name="Jay Cui",
    module_name="my_fastapi_app",
    name="my-fastapi-app",
    version="0.1.0",
)

project.synth()