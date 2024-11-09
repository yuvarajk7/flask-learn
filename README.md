## API Notes

- This project build using python 3.12.7
- Environment created using pyenv
- Mange dependencies using pipenv
- Created Flask project
  - Installed package flask
  - Create Book endpoint contains properties
    - Author
    - title
    - id
  - Create endpoints GET, POST, PUT and DELETE
- Created swagger openapi support
  - Installed the package flassger
  - Separate API Def as per endpoint method and stored in swagger folder
  - Imported Swagger, swag_from
  - Decorated each method using swag_from attribute
  - Add app registration Swagger(app) 