from projen.python import PythonProject

project = PythonProject(
    author_email="shilongjaycui@gmail.com",
    author_name="Jay Cui",
    module_name="my_fastapi_app",
    name="my-fastapi-app",
    version="0.1.0",
    deps=[
        'pytest@7.4.2',
        'fastapi@0.103.2',
        'uvicorn[standard]@0.23.2',
    ]
)

project.synth()
